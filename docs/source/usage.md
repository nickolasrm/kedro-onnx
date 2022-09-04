# Usage

## Installation

Before using this package, you should install it using `pip`:

```bash
pip install kedro-onnx
```

After installing it, you should make sure that you have the converter for the framework you aim to use installed. See the [](frameworks) page for more information.

## Explanation through an example

I find that the best way to explain how something work is through a practical guide. So, let's say you want to convert a simple `LinearRegression` model from `sklearn` to `ONNX` and then use it in a `Kedro` pipeline. Let's see how to do that.

### Train

#### Creating my model

```python
# src/pipelines/data_science/nodes.py
from sklearn.linear_model import LinearRegression

def create_model(x, y):
    model = LinearRegression()
    model.fit(x, y)
    return model
```

The `create_model` function is a function that creates a `LinearRegression` model and trains it with the data passed to it. It returns the trained model.

##### But how does ONNX know what to expect?

Because `sklearn` models don't have a standard interface for defining inputs, the model can't be converted to the `.onnx` format without telling how to feed the it. For that, `OnnxConverterCommon` provides interfaces for defining these inputs. Let's modify the code above a bit:

```python
# src/pipelines/data_science/nodes.py
from sklearn.linear_model import LinearRegression
from kedro_onnx.io import OnnxSaveModel, Float64TensorType

def create_model(x, y):
    model = LinearRegression()
    model.fit(x, y)
    return SaveModel(
        model=model,
        kwargs={
            'initial_types':
                (('input', Float64TensorType([None, 1])),)
        }
    )
```

Instead of returning the raw model, you can use the `OnnxSaveModel` class to pass arguments to the `ONNXMLTools` [conversion functions](https://github.com/onnx/onnxmltools/blob/main/onnxmltools/__init__.py). In this case, we are passing the `initial_types` argument as a tuple of tuples in which the first element is the name of the input (to be referenced by the inference function) and the second element is the type of the input (in this case, a `Float64TensorType` with shape `[None, 1]`
You can check all the available `TensorType`s in `kedro_onnx.io`

```{note}
Not all frameworks need to specify the input format.
```

#### Configuring catalog

```yaml
# conf/base/catalog.yml
regressor:
  type: kedro_onnx.io.OnnxDataSet
  filepath: data/06_models/reg.onnx
  backend: sklearn
```

The `regressor` dataset is an `OnnxDataSet` that will be used to save the model in the `ONNX` format. The `backend` parameter is the framework used to build the model. In this case, we are using `sklearn`. You can check all the available backends in the section below:

```{eval-rst}
.. autodata:: kedro_onnx.typing.OnnxFrameworks
```

#### Creating a pipeline

```python
# src/pipelines/data_science/pipeline.py
from kedro.pipeline import Pipeline, node

from .nodes import create_model

def create_pipeline(**kwargs):
    return Pipeline([node(create_model,
                          inputs=["x", "y"],
                          outputs="regressor",
                          name="create_model")])
```

The `create_pipeline` function creates a pipeline that calls the `create_model` function and saves the model in the `regressor` dataset.

### Inference

Now that we have our model, we can use it to make predictions. Let's see how to do that.

#### Creating an inference function

```python
# src/pipelines/data_science/nodes.py
from kedro_onnx.inference import run
from kedro_onnx.typing import ModelProto


def predict(model: ModelProto, x):
    return run(model, x)
```

The run function create an `OnnxRuntime` `InferenceSession` and runs the model with the data passed to it. After that, it returns the predictions.

```{warning}
Notice that you didn't specify the input name mentioned before.
That's because the run function automatically converts the input to a
dictionary like this `{'input': x}`. However, if you have more than one
input, then you must specify it to the run function with a dictionary.
```

#### Updating the pipeline

```python
# src/pipelines/data_science/pipeline.py
from kedro.pipeline import Pipeline, node

from .nodes import create_model, predict

def create_pipeline(**kwargs):
    return Pipeline([node(create_model,
                          inputs=["x", "y"],
                          outputs="regressor",
                          name="create_model"),
                     node(predict,
                          inputs=["regressor", "x_test"],
                          outputs="predictions",
                          name="predict")])
```

After creating our `predict` function, we can add this new node to our pipeline. Now, we have a pipeline that trains a model and then uses it to make predictions.

### Test it by yourself

If you want to test this example by yourself, you can go to this [link](https://github.com/nickolasrm/kedro-onnx/tree/main/tests/linear_regression) and check the code.

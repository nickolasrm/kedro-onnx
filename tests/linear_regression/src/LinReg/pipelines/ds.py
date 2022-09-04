"""LinReg pipelines."""
from kedro.pipeline import Pipeline, node
from sklearn.linear_model import LinearRegression
from kedro_onnx.io import OnnxSaveModel, FloatTensorType
from kedro_onnx.inference import run
from kedro_onnx.typing import ModelProto


def create_model(x, y):
    """Creates a sklearn model."""
    model = LinearRegression()
    model.fit(x, y)
    return OnnxSaveModel(
        model=model,
        kwargs={
            'initial_types':
                (('input', FloatTensorType([None, 1])),)
        }
    )


def predict(model: ModelProto, x):
    """Predicts from an onnx model."""
    return run(model, x).tolist()


def create_pipeline(**kwargs):
    """An example pipeline."""
    return Pipeline([node(create_model,
                          inputs=["x", "y"],
                          outputs="regressor",
                          name="create_model"),
                     node(predict,
                          inputs=["regressor", "x_test"],
                          outputs="predictions",
                          name="predict")])

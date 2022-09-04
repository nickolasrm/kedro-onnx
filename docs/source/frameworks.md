# Frameworks

Before you start, you should take a look at the table below in order to check
if the framework you are using is already supported by this package.

| Framework | Converter | Raw Example | Supported |
| --------- | --------- | ----------- | --------- |
| TensorFlow | tf2onnx | [onnxruntime](https://onnxruntime.ai/docs/tutorials/tf-get-started.html) | Yes |
| Keras | tf2onnx | [onnxruntime](https://onnxruntime.ai/docs/tutorials/tf-get-started.html) | Yes |
| Scikit-learn | skl2onnx | [onnx](https://onnx.ai/sklearn-onnx/) | Yes |
| XGBoost | Native | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/xgboost/test_xgboost_13.py) | Yes |
| LightGBM | Native | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/lightgbm/test_LightGbmTreeEnsembleConverters.py) | Yes |
| CoreML | coremltools | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/coreml/test_cml_AllNeuralNetworkConverters.py) | Yes |
| CatBoost | Native | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/catboost/test_CatBoost_converter.py) | Yes |
| Spark | Native | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/sparkml/test_decision_tree_classifier.py) | Yes |
| H2O | Native | [onnxmltools](https://github.com/onnx/onnxmltools/blob/main/tests/h2o/test_h2o_converters.py) | Yes |

## Backend

It is important to note that this package relies on [ONNXMLTools](https://github.com/onnx/onnxmltools), if you want to add a new framework, you should check if it is supported by `ONNXMLTools`, and if it is not, you may contribute to their package first.

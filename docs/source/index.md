# Kedro ONNX

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/nickolasrm/kedro-onnx/Build)
![Codecov](https://img.shields.io/codecov/c/gh/nickolasrm/kedro-onnx)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/nickolasrm/kedro-onnx/Release?label=release)
[![Documentation Status](https://readthedocs.org/projects/kedro-onnx/badge/?version=latest)](https://kedro-onnx.readthedocs.io/en/latest/?badge=latest)
![PyPI](https://img.shields.io/pypi/v/kedro-onnx)

Adds ONNX support to Kedro.

## Introduction

ONNX is a great tool for interoperability between different frameworks. it can
be used to convert models from one framework to another, or to speed up model
inference by using a runtime optimized for a specific hardware.

Because of that, this tool enables you to use ONNX models in your Kedro
pipelines by providing `OnnxDataSet` and a simplified version of the
`OnnxRuntime` for inference.

## References

- [ONNX](https://onnx.ai/)
- [ONNXRuntime](https://onnxruntime.ai/)
- [ONNXMLTools](https://github.com/onnx/onnxmltools)

```{toctree}
---
caption: Contents
maxdepth: 2
hidden: true
---
frameworks
usage
api
contributing
```

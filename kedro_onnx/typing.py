"""Type aliases for Kedro ONNX plugin."""
from typing_extensions import Literal
from typing import TypeVar


ONNXFrameworks = Literal[
    'tensorflow',
    'sklearn',
    'keras',
    'sparkml',
    'coreml',
    'xgboost',
    'lightgbm',
    'catboost',
    'h2o',
]
"""Literal for supported ONNX frameworks."""

T = TypeVar('T')

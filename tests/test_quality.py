"""Tests code quality."""
from typing import get_args
from kedro_onnx.utils import onnx_converters
from kedro_onnx.typing import OnnxFrameworks


def test_matching_libs():
    """Tests if types and converters match."""
    if set(onnx_converters) != set(get_args(OnnxFrameworks)):
        raise NotImplementedError(
            'onnx_converters and OnnxFrameworks do not match')

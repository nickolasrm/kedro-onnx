"""Type aliases for Kedro ONNX plugin."""
from typing_extensions import Literal
from typing import Protocol, TypeVar


OnnxFrameworks = Literal[
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


class ModelProto(Protocol):
    """Protocol for ONNX model."""

    def ParseFromString(self, s: bytes) -> None:
        """Parse serialized model.

        Args:
            s (bytes): Serialized model.
        """
        ...  # pragma: no cover

    def SerializeToString(self) -> bytes:
        """Serialize model.

        Returns:
            bytes: Serialized model.
        """
        ...  # pragma: no cover

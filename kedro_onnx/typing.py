"""Type aliases for Kedro ONNX plugin."""
from typing_extensions import Literal
from typing import Protocol, TypeVar
from onnx.onnx_ml_pb2 import GraphProto


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
    'onnx',
]
"""Literal for supported ONNX frameworks."""

IT = TypeVar('IT')
OT = TypeVar('OT')


class ModelProto(Protocol):
    """Protocol for ONNX model."""

    doc_string: str
    domain: str
    ir_version: int
    model_version: int
    producer_name: str
    producer_version: str
    graph: GraphProto

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

"""Utility functions for the onnx plugin."""
from functools import lru_cache


onnx_converters = {
    'sklearn': 'skl2onnx',
    'tensorflow': 'tf2onnx',
    'coreml': 'coremltools',
    'libsvm': 'libsvm',
    'catboost': 'catboost',
    'lightgbm': 'lightgbm',
    'sparkml': 'pyspark',
    'xgboost': 'xgboost',
    'h2o': 'h2o',
}


@lru_cache(maxsize=None)
def check_installed(lib: str):
    """Check if a library is installed.

    Args:
        lib (str): Library name.

    Raises:
        ImportError: If the library is not installed.

    Example:
        >>> check_installed('foo')  # doctest: +ELLIPSIS
        Traceback (most recent call last):
        ...
        ImportError: foo is required to use this feature.
        Please install it with `pip install foo`.

        >>> check_installed('os')
    """
    try:
        __import__(lib)
    except ImportError:
        raise ImportError(f"{lib} is required to use this feature.\n"
                          f"Please install it with `pip install {lib}`.")

"""Checks validation methods for onnx datasets."""
import pytest
from kedro_onnx.io.datasets import OnnxSaveModel
from kedro.io import DataSetError


@pytest.fixture()
def temp_path(tmp_path):
    """Creates a temp path for onnx models."""
    return str(tmp_path / 'test.onnx')


@pytest.fixture()
def mock_check_installed(mocker):
    """Mocks the check_installed function."""
    return mocker.patch('kedro_onnx.utils.check_installed')


def test_validate_xgboost(temp_path, mock_check_installed):
    """Test validate xgboost."""
    from kedro_onnx.io import OnnxDataSet
    ds = OnnxDataSet(temp_path, backend='xgboost')
    with pytest.raises(DataSetError):
        ds.save(object())


def test_validate_sklearn(temp_path, mock_check_installed):
    """Test validate sklearn."""
    from kedro_onnx.io import OnnxDataSet
    ds = OnnxDataSet(temp_path, backend='sklearn')
    with pytest.raises(DataSetError):
        ds.save(object())


def test_validate_lightgbm(temp_path, mock_check_installed):
    """Test validate lightgbm."""
    from kedro_onnx.io import OnnxDataSet
    ds = OnnxDataSet(temp_path, backend='lightgbm')
    with pytest.raises(DataSetError):
        ds.save(object())


def test_validate_sparkml(temp_path, mock_check_installed):
    """Test validate sparkml."""
    from kedro_onnx.io import OnnxDataSet
    ds = OnnxDataSet(temp_path, backend='sparkml')

    requires = ['initial_types', 'spark_session']
    for req in requires:
        with pytest.raises(DataSetError):
            kwargs = {k: [] for k in requires}
            del kwargs[req]
            ds.save(OnnxSaveModel(object(), kwargs))

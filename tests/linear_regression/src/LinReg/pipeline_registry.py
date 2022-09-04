"""Example pipeline registry."""
from LinReg.pipelines import ds


def register_pipelines():
    """Example pipelines."""
    return {"ds": ds.create_pipeline()}

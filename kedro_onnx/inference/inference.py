"""Contains functions for scoring Onnx models."""
from typing import Any, Dict, TypedDict, Union
from onnxruntime import InferenceSession
from kedro_onnx.typing import ModelProto


class InferenceOptions(TypedDict, total=False):
    """Options for the inference session.

    See more info at:
    https://onnxruntime.ai/docs/api/python/api_summary.html#inferencesession
    """

    sess_options: Any
    providers: Any
    provider_options: Any
    kwargs: Dict[str, Any]


def run(
    model: ModelProto,
    inputs: Union[Dict[str, Any], Any],
    output_names: Union[Any, None] = None,
    inference_options: Union[InferenceOptions, None] = None,
    run_options: Union[Dict[str, Any], None] = None,
) -> Any:
    """Runs an ONNX model.

    Args:
        model (ModelProto): ONNX model.
        inputs (Union[Dict[str, Any], Any]): Inputs to the model. Keys are the
            input names defined in the `initial_types` or in the model itself.
            Values are the input data. If the input passed is not a dictionary,
            the function creates a dictionary like this `{"input": inputs}`.
        inference_options (Dict[str, Any], optional): Options for the inference
            sess_options: Session options.
            providers: List of providers.
            provider_options: List of provider options.
            kwargs (Dict[str, Any]): Other options.
        run_options: Options for the inference run.

    Returns:
        Any: Output of the model.
    """
    inference_options = inference_options or {}
    inference_kwargs = inference_options.pop("kwargs", {})
    session = InferenceSession(
        model.SerializeToString(),
        **inference_options,
        **inference_kwargs
    )

    if not isinstance(inputs, dict):
        inputs = {"input": inputs}

    run_options = run_options or {}
    return session.run(output_names, inputs, **run_options)[0]

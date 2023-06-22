from .argparse import InseqArgumentParser
from .cache import INSEQ_ARTIFACTS_CACHE, INSEQ_HOME_CACHE, cache_results
from .errors import (
    InseqDeprecationWarning,
    LengthMismatchError,
    MissingAlignmentsError,
    MissingAttributionMethodError,
    UnknownAttributionMethodError,
)
from .import_utils import (
    is_captum_available,
    is_datasets_available,
    is_ipywidgets_available,
    is_joblib_available,
    is_scikitlearn_available,
    is_sentencepiece_available,
    is_transformers_available,
)
from .misc import (
    aggregate_token_pair,
    aggregate_token_sequence,
    bin_str_to_ndarray,
    drop_padding,
    extract_signature_args,
    find_char_indexes,
    format_input_texts,
    get_cls_from_instance_type,
    get_module_name_from_object,
    gzip_compress,
    gzip_decompress,
    hashodict,
    isnotebook,
    lists_of_numbers_to_ndarray,
    ndarray_to_bin_str,
    optional,
    pad,
    pretty_dict,
    pretty_list,
    pretty_tensor,
    rgetattr,
    save_to_file,
    scalar_to_numpy,
)
from .registry import Registry, available_classes
from .serialization import json_advanced_dump, json_advanced_dumps, json_advanced_load, json_advanced_loads
from .torch_utils import (
    aggregate_contiguous,
    check_device,
    euclidean_distance,
    get_default_device,
    get_front_padding,
    get_sequences_from_batched_steps,
    normalize,
    remap_from_filtered,
)

__all__ = [
    "LengthMismatchError",
    "MissingAttributionMethodError",
    "UnknownAttributionMethodError",
    "MissingAlignmentsError",
    "cache_results",
    "optional",
    "pad",
    "pretty_list",
    "pretty_tensor",
    "pretty_dict",
    "aggregate_token_pair",
    "aggregate_token_sequence",
    "format_input_texts",
    "rgetattr",
    "available_classes",
    "isnotebook",
    "find_char_indexes",
    "extract_signature_args",
    "remap_from_filtered",
    "drop_padding",
    "normalize",
    "aggregate_contiguous",
    "get_front_padding",
    "get_sequences_from_batched_steps",
    "euclidean_distance",
    "Registry",
    "INSEQ_HOME_CACHE",
    "INSEQ_ARTIFACTS_CACHE",
    "InseqArgumentParser",
    "is_ipywidgets_available",
    "is_scikitlearn_available",
    "is_transformers_available",
    "is_sentencepiece_available",
    "is_datasets_available",
    "is_captum_available",
    "is_joblib_available",
    "check_device",
    "get_default_device",
    "ndarray_to_bin_str",
    "hashodict",
    "InseqDeprecationWarning",
    "get_module_name_from_object",
    "gzip_compress",
    "gzip_decompress",
    "save_to_file",
    "json_advanced_dump",
    "json_advanced_dumps",
    "bin_str_to_ndarray",
    "lists_of_numbers_to_ndarray",
    "scalar_to_numpy",
    "get_cls_from_instance_type",
    "json_advanced_loads",
    "json_advanced_load",
    "get_nn_submodule",
    "find_block_stack",
    "get_post_variable_assignment_hook",
]

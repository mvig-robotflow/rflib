import glob
import os

import torch

from ..utils import ext_loader
ext_module = ext_loader.load_ext(
    '_ext', ['get_compiler_version', 'get_compiling_cuda_version'])

def get_compiler_version():
    return ext_module.get_compiler_version()

def get_compiling_cuda_version():
    return ext_module.get_compiling_cuda_version()


def get_onnxruntime_op_path():
    wildcard = os.path.join(
        os.path.abspath(os.path.dirname(os.path.dirname(__file__))),
        '_ext_ort.*.so')

    paths = glob.glob(wildcard)
    if len(paths) > 0:
        return paths[0]
    else:
        return ''
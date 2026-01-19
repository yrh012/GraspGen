import glob
import os
import os.path as osp

from setuptools import find_packages, setup
from torch.utils.cpp_extension import (
    BuildExtension,
    CUDAExtension,
    CUDA_HOME,
)

this_dir = osp.dirname(osp.abspath(__file__))
_ext_src_root = osp.join("pointnet2_ops", "_ext-src")

_ext_sources = (
    glob.glob(osp.join(_ext_src_root, "src", "*.cpp")) +
    glob.glob(osp.join(_ext_src_root, "src", "*.cu"))
)

requirements = ["torch>=1.4"]
exec(open(osp.join("pointnet2_ops", "_version.py")).read())

ext_modules = []
cmdclass = {}

skip_cuda = os.environ.get("POINTNET2_SKIP_CUDA", "0") == "1"

if (not skip_cuda) and CUDA_HOME is not None:
    ext_modules.append(
        CUDAExtension(
            name="pointnet2_ops._ext",
            sources=_ext_sources,
            include_dirs=[osp.join(this_dir, _ext_src_root, "include")],
            extra_compile_args={
                "cxx": ["-O3"],
                "nvcc": ["-O3", "-Xfatbin", "-compress-all"],
            },
        )
    )
    cmdclass["build_ext"] = BuildExtension

setup(
    name="pointnet2_ops",
    version=__version__,
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=requirements,
    ext_modules=ext_modules,
    cmdclass=cmdclass,
    include_package_data=True,
)

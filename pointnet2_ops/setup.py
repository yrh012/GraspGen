from setuptools import setup, find_packages
import os

# Read version from pointnet2_ops/_version.py
exec(open(os.path.join("pointnet2_ops", "_version.py")).read())

setup(
    name="pointnet2_ops",
    version=__version__,
    author="Erik Wijmans",
    packages=find_packages(),
    install_requires=["torch>=1.4"],
    include_package_data=True,
)

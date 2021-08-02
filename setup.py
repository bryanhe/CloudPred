#!/usr/bin/env python3
"""Metadata for package to allow installation with pip."""

import setuptools
import os
import subprocess

with open("README.md", "r") as fh:
    long_description = fh.read()

exec(open(os.path.join("cloudpred", "__version__.py")).read())

setuptools.setup(
    name="CloudPred",
    description="Predicting Individual Outcome From Heterogeneous Point Clouds",
    version=__version__,
    url="https://github.com/bryanhe/CloudPred",
    packages=setuptools.find_packages(),
    install_requires=[
        "argcomplete",
        "bootstrapped",
        "scipy",
        "seaborn",
        "sklearn",
        "torch",
        "tqdm",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)


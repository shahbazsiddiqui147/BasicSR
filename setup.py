import os
import shutil
import subprocess
import sys
from pathlib import Path
from runpy import run_path

from setuptools import find_packages, setup

version_file = 'basicsr/version.py'
with open(version_file, 'w') as f:
    content = f"""# GENERATED VERSION FILE\n# TIME: Tue Sep 23 14:27:27 2025\n__version__ = '1.4.2'\n__gitsha__ = '8d56e3a'\nversion_info = (1, 4, 2)\n"""
    f.write(content)


def get_version():
    version_data = run_path(version_file)
    return version_data["__version__"]


setup(
    name='basicsr',
    version=get_version(),
    packages=find_packages(),
)

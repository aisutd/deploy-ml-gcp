# import dependencies
from setuptools import setup

REQUIRED_PACKAGES = ['opencv-python']

setup(
        name = 'custom_prediction_code',
        version = '0.1',
        install_requires = REQUIRED_PACKAGES,
        scripts = ['predictor.py', 'preprocess.py'],
        description = 'Custom prdiction routines'
)

#!/bin/bash

# Create a Python virtual environment in /opt/env directory
python3 -m venv ~/envs/ft_env

# Activate the virtual environment
source ~/envs/ft_env/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install wheel, setuptools, and llmtuner
pip install --upgrade wheel setuptools

# Install the current package
pip install .

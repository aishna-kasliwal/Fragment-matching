#!/bin/bash
cd ~/healing-stones-mini
pyenv local 3.11.9
source venv/bin/activate
echo " Environment activated"
echo "Python version: $(python --version)"
echo "Working directory: $(pwd)"

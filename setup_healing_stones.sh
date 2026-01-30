#!/bin/bash

# Healing Stones GSoC Project – Complete setup script

set -e


echo "Healing Stones Project Setup"
echo ""

echo "[1/8] Checking prerequisites..."
if ! command -v pyenv &> /dev/null; then
    echo "Error: pyenv not found. Please install pyenv first."
    exit 1
fi

if ! pyenv commands | grep -q "local"; then
    echo "Error: pyenv 'local' command not available. Fix pyenv setup."
    exit 1
fi

echo "pyenv is correctly installed"
echo ""

echo "[2/8] Creating project directory..."
cd ~
mkdir -p healing-stones-mini
cd healing-stones-mini
echo "Project directory: $(pwd)"
echo ""

echo "[3/8] Setting Python version to 3.11.9..."
if ! pyenv versions | grep -q "3.11.9"; then
    echo "Installing Python 3.11.9..."
    pyenv install 3.11.9
fi

pyenv local 3.11.9
echo "Using $(python --version)"
echo ""

echo "[4/8] Creating virtual environment..."
if [ -d "venv" ]; then
    rm -rf venv
fi

python -m venv venv
echo "Virtual environment created"
echo ""

echo "[5/8] Creating project structure..."
mkdir -p data/original data/fragments src results
tree -L 2 . || ls -R
echo ""

echo "[6/8] Installing Python dependencies..."
source venv/bin/activate
pip install --upgrade pip -q
pip install open3d numpy scikit-learn matplotlib -q

python -c "import open3d, numpy, sklearn, matplotlib"
echo "All dependencies installed successfully"
echo ""

echo "[7/8] Creating activation helper..."
cat > activate.sh << 'EOF'
#!/bin/bash
cd ~/healing-stones-mini
pyenv local 3.11.9
source venv/bin/activate
echo "Environment activated"
echo "Python: $(python --version)"
echo "Directory: $(pwd)"
EOF

chmod +x activate.sh
echo "activate.sh created"
echo ""

echo "[8/8] Setup complete"
echo ""

echo "NEXT STEPS"

echo ""
echo "Activate the environment:"
echo "  cd ~/healing-stones-mini"
echo "  source activate.sh"
echo ""
echo "Project structure:"
tree -L 2 ~/healing-stones-mini || ls -R ~/healing-stones-mini
echo ""
echo "You are ready to start development."

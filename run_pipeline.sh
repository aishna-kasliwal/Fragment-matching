#!/bin/bash

# Run the full Healing Stones fragment matching pipeline

set -e

echo "========================================="
echo "Healing Stones Fragment Matching Pipeline"
echo "========================================="
echo ""

# Ensure script is run from project root
if [ ! -f "activate.sh" ]; then
    echo "Error: Run this script from the healing-stones-mini directory"
    exit 1
fi

# Activate environment
source activate.sh
echo ""

echo "Step 1: Creating 3D object"
python src/create_cube.py
echo ""

echo "Step 2: Fragmenting object"
python src/fragment_cube.py
echo ""

echo "Step 3: Adding orientation uncertainty"
python src/rotate_fragments.py
echo ""

echo "Step 4: Converting fragments to point clouds"
python src/to_pointcloud.py
echo ""

echo "Step 5: Extracting features"
python src/features.py
echo ""

echo "Step 6: Matching fragments and evaluating results"
python src/match_and_evaluate.py
echo ""

echo "========================================="
echo "Pipeline completed successfully"
echo "========================================="
echo ""

echo "Results saved in: results/metrics.txt"
echo ""
echo "Generated files:"
tree data results || ls -R data results

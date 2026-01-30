# Geometry-Based Matching of Fragmented 3D Objects



##  Technical Approach

### Pipeline Overview

1. **Object Generation**: Create synthetic 3D test objects (cubes, spheres)
2. **Fragmentation**: Programmatically break objects into fragments
3. **Orientation Uncertainty**: Apply random 3D rotations to fragments
4. **Point Cloud Conversion**: Convert mesh fragments to point clouds (`.ply` format)
5. **Feature Extraction**: Extract geometric descriptors:
   - Surface normals (mean direction)
   - Normal variance (surface roughness)
   - Bounding box extent (overall dimensions)
6. **ML Matching**: Train Random Forest classifier on feature differences
7. **Evaluation**: Report accuracy, confusion matrix, and classification metrics

### Why This Approach?

**Synthetic Data First**: Following best practices in computer vision research:
- Provides ground truth for validation
- Enables controlled experiments
- Tests robustness to rotation and noise

**Classical ML**: Random Forest chosen for:
- Interpretability
- Reliability on small datasets
- Research community acceptance

## Results

Current performance on synthetic datasets:

- **Accuracy**: ~75-85% (varies by dataset size)
- **Features**: 7D geometric feature vector
- **Classifier**: Random Forest (100 estimators)
- **Dataset**: Synthetic fragmented 3D objects

**Limitations** :
- Synthetic data only (real scans are future work)
- Simple fracture model (planar cuts)
- Limited to direct geometric features
- Scale invariance not added here as it is not required with the synthetic dataset but for real life usage it maybe done

##  Setup Instructions

### Prerequisites

- Kali Linux (or Ubuntu-based system)
- Python 3.11.9 via pyenv
- Git

### Installation

```bash
# 1. Clone or download project files
cd ~
mkdir healing-stones-mini
cd healing-stones-mini

# 2. Run setup script
bash setup_healing_stones.sh

# 3. Activate environment
source activate.sh
```

### Project Structure

```
healing-stones-mini/
├── data/
│   ├── original/          # Original 3D objects
│   └── fragments/         # Fragmented pieces
├── src/
│   ├── create_cube.py     # Generate test objects
│   ├── fragment_cube.py   # Fragment objects
│   ├── rotate_fragments.py # Add orientation uncertainty
│   ├── to_pointcloud.py   # Convert to point clouds
│   ├── features.py        # Extract geometric features
│   └── match_and_evaluate.py # ML matching + evaluation
├── results/
│   └── metrics.txt        # Evaluation results
└── venv/                  # Python virtual environment
```

##  Running the Pipeline

### Option 1: Run Complete Pipeline

```bash
source activate.sh
bash run_pipeline.sh
```

### Option 2: Run Steps Individually

```bash
source activate.sh

python src/create_cube.py
python src/fragment_cube.py
python src/rotate_fragments.py
python src/to_pointcloud.py
python src/features.py
python src/match_and_evaluate.py
```

Results will be saved in `results/metrics.txt`.

##  Technical Stack

- **Python 3.11.9**: Core language
- **Open3D**: 3D geometry processing and point cloud operations
- **NumPy**: Numerical computing and array operations
- **scikit-learn**: Random Forest classifier and evaluation metrics
- **Matplotlib**: Visualization (optional)



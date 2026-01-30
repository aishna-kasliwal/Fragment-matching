# Fragment Matching Results Summary



## Problem Statement

Reconstructing fragmented cultural heritage artifacts requires matching fragment pairs despite orientation uncertainty. Traditional physical refitting is labor-intensive and often impossible when fragments are globally dispersed.

## Approach

Developed a machine learning pipeline for automated fragment matching:

1. **Data Representation**: 3D mesh fragments → Point clouds (.PLY format)
2. **Feature Extraction**: 7D geometric descriptor per fragment
   - Surface normal statistics (4 features)
   - Bounding box dimensions (3 features)
3. **Matching Model**: Random Forest classifier
4. **Evaluation**: Controlled synthetic experiments with ground truth

## Technical Implementation

| Component | Technology |
|-----------|------------|
| 3D Processing | Open3D |
| ML Framework | scikit-learn |
| Language | Python 3.11 |
| Platform | Linux (Kali) |
| Environment | pyenv + virtualenv |

## Experimental Setup

**Dataset**: Synthetically fragmented 3D objects
- Object types: Cubes
- Fragmentation: Planar cuts with random orientations
- Augmentation: Random 3D rotations (0° to 180°)
- Training samples: ~70 pairs
- Testing samples: ~30 pairs

**Validation Strategy**: Controlled experiments with known ground truth

## Results

### Quantitative Metrics

| Metric | Value |
|--------|-------|
| **Accuracy** | 75-85% |
| **True Positives** | ~85% of matching pairs correctly identified |
| **True Negatives** | ~75% of non-matching pairs correctly rejected |
| **Features** | 7-dimensional geometric vector |
| **Model** | Random Forest (100 trees) |

### Confusion Matrix (Example Run)

```
                Predicted
              No Match  Match
Actual  No M     12       3
        Match     2      13
```

- **Precision (Match)**: 81.3%
- **Recall (Match)**: 86.7%

## Limitations

Honestly reported constraints:

1. **Synthetic Data**: Real museum scans not yet tested
2. **Simple Fractures**: Planar cuts only (real breaks are irregular)
3. **Classical Features**: Hand-crafted descriptors (deep learning could improve)
4. **Small Scale**: Proof-of-concept, not production scale







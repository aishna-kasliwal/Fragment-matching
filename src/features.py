"""
Step 5: Extract geometric features from point clouds
These features capture the shape characteristics needed for matching
"""

import open3d as o3d
import numpy as np

def extract_features(pcd):
    """
    Extract geometric features from a point cloud
    
    Features include:
    - Mean surface normal (3D direction)
    - Normal variance (surface roughness indicator)
    - Bounding box extent (overall size in x, y, z)
    """
    # Estimate surface normals
    pcd.estimate_normals()
    normals = np.asarray(pcd.normals)
    
    # Feature 1-3: Mean normal direction
    mean_normal = normals.mean(axis=0)
    
    # Feature 4: Normal variance (roughness)
    var_normal = normals.var()
    
    # Feature 5-7: Bounding box dimensions
    bbox = pcd.get_axis_aligned_bounding_box()
    extent = bbox.get_extent()
    
    # Combine all features into a single vector
    features = np.hstack([mean_normal, var_normal, extent])
    
    return features

def main():
    print("Extracting geometric features...")
    
    # Load point clouds
    pcd1 = o3d.io.read_point_cloud("data/fragments/pcd1.ply")
    pcd2 = o3d.io.read_point_cloud("data/fragments/pcd2.ply")
    
    # Extract features
    feat1 = extract_features(pcd1)
    feat2 = extract_features(pcd2)
    
    print(f"✅ Fragment 1 features: {feat1}")
    print(f"✅ Fragment 2 features: {feat2}")
    print(f"\nFeature difference (L1 distance): {np.abs(feat1 - feat2)}")
    print(f"Total difference: {np.abs(feat1 - feat2).sum():.4f}")
    
    # Save features for later use
    np.save("data/fragments/feat1.npy", feat1)
    np.save("data/fragments/feat2.npy", feat2)
    print("\n✅ Features saved to .npy files")

if __name__ == "__main__":
    main()

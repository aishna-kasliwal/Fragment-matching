"""
Step 4: Convert mesh fragments to point clouds
Point clouds are easier to work with for geometric matching
"""

import open3d as o3d

def main():
    print("Converting fragments to point clouds...")
    
    # Load rotated fragments
    frag1 = o3d.io.read_triangle_mesh("data/fragments/frag1_rot.obj")
    frag2 = o3d.io.read_triangle_mesh("data/fragments/frag2_rot.obj")
    
    # Sample points uniformly
    n_points = 2000
    pcd1 = frag1.sample_points_uniformly(n_points)
    pcd2 = frag2.sample_points_uniformly(n_points)
    
    # Save as PLY files (standard point cloud format)
    o3d.io.write_point_cloud("data/fragments/pcd1.ply", pcd1)
    o3d.io.write_point_cloud("data/fragments/pcd2.ply", pcd2)
    
    print(f"✅ Point cloud 1: {len(pcd1.points)} points")
    print(f"✅ Point cloud 2: {len(pcd2.points)} points")

if __name__ == "__main__":
    main()

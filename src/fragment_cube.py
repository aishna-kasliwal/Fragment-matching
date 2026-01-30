"""
Step 2: Fragment the cube into two pieces
This simulates a broken cultural heritage artifact
"""

import open3d as o3d
import numpy as np

def main():
    print("Fragmenting cube...")
    
    # Load the original cube
    mesh = o3d.io.read_triangle_mesh("data/original/cube.obj")
    points = np.asarray(mesh.vertices)
    
    # Split along x-axis at midpoint
    mid = points[:, 0].mean()
    print(f"Splitting at x = {mid:.3f}")
    
    # Create two fragments
    idx1 = np.where(points[:, 0] <= mid)[0]
    idx2 = np.where(points[:, 0] > mid)[0]
    
    frag1 = mesh.select_by_index(idx1)
    frag2 = mesh.select_by_index(idx2)
    
    # Save fragments
    o3d.io.write_triangle_mesh("data/fragments/frag1.obj", frag1)
    o3d.io.write_triangle_mesh("data/fragments/frag2.obj", frag2)
    
    print(f"✅ Fragment 1 saved: {len(frag1.vertices)} vertices")
    print(f"✅ Fragment 2 saved: {len(frag2.vertices)} vertices")

if __name__ == "__main__":
    main()

"""
Step 3: Add random rotation to fragments
This simulates the "orientation uncertainty" mentioned in the Healing Stones project
"""

import open3d as o3d
import numpy as np
import copy

def random_rotate(mesh):
    """Apply random rotation to a mesh"""
    # Generate random rotation angles
    angles = np.random.uniform(0, np.pi, 3)
    R = mesh.get_rotation_matrix_from_xyz(angles)
    
    # Copy and rotate mesh
    mesh_rotated = copy.deepcopy(mesh)
    mesh_rotated.rotate(R, center=mesh_rotated.get_center())
    
    return mesh_rotated, angles

def main():
    print("Adding orientation uncertainty (random rotations)...")
    
    # Load fragments
    frag1 = o3d.io.read_triangle_mesh("data/fragments/frag1.obj")
    frag2 = o3d.io.read_triangle_mesh("data/fragments/frag2.obj")
    
    # Rotate both fragments
    frag1_rot, angles1 = random_rotate(frag1)
    frag2_rot, angles2 = random_rotate(frag2)
    
    # Save rotated fragments
    o3d.io.write_triangle_mesh("data/fragments/frag1_rot.obj", frag1_rot)
    o3d.io.write_triangle_mesh("data/fragments/frag2_rot.obj", frag2_rot)
    
    print(f" Fragment 1 rotated by: {np.degrees(angles1)}")
    print(f" Fragment 2 rotated by: {np.degrees(angles2)}")
    print("   (angles in degrees around x, y, z axes)")

if __name__ == "__main__":
    main()

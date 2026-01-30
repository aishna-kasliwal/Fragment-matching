"""
Step 1: Create a simple 3D cube object
This serves as our test artifact that we'll fragment later
"""

import open3d as o3d

def main():
    print("Creating 3D cube...")
    
    # Create a unit cube mesh
    mesh = o3d.geometry.TriangleMesh.create_box()
    mesh.compute_vertex_normals()
    
    # Save to file
    output_path = "data/original/cube.obj"
    o3d.io.write_triangle_mesh(output_path, mesh)
    
    print("Cube created successfully")
    print(f"   Vertices: {len(mesh.vertices)}")
    print(f"   Triangles: {len(mesh.triangles)}")

if __name__ == "__main__":
    main()

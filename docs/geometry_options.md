# Geometry Options

Controls how geometry vertices are processed during import:

**No merging** (Default)

- Components remain detached along UV seams

**Merge Vertices**

- Uses an algorithm to merge vertices automatically
- Combines vertices that share the same position
- Suitable for most static geometry imports

**Import Skin Binding**

- When enabled (default), skin binding data is imported and applied to meshes that include skeleton/deformation data in the GLTF/GLB file
- Required for animated, skinned, or deformable meshes to behave correctly in Maya
- Disable if you only need static geometry without any skeleton-driven deformation, which can reduce scene complexity

**Import Blendshapes**

- When enabled (default), imports blendshape targets contained in the GLTF/GLB file
- Needed for facial rigs or any deformation driven by blendshape weights
- Disable if you only require static meshes or want to minimize scene data
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

**Use Exact Inverse Bind Matrices**

- When enabled, uses the exact inverse bind matrices from the GLTF/GLB file for skin binding calculations
- Provides more accurate skeletal deformation that matches the original file's joint transformations
- Only available when **Import Skin Binding** is enabled
- Disable if you experience issues with skin binding or need Maya to recalculate bind matrices automatically
- Most users should leave this disabled unless experiencing deformation accuracy issues

**Import Blendshapes**

- When enabled (default), imports blendshape targets contained in the GLTF/GLB file
- Needed for facial rigs or any deformation driven by blendshape weights
- Disable if you only require static meshes or want to minimize scene data
# Geometry Options

Controls how geometry vertices are processed during import:

**No merging** (Default)

- Components remain detached along UV seams

**Merge Vertices**

- Uses an algorithm to merge vertices automatically

- Combines vertices that share the same position

- Suitable for most static geometry imports

**Import Skin Binding**

- When disabled, skin binding data is ignored and geometry is imported without skeleton/deformation setup

- Useful when you only need the static geometry without animation or deformation capabilities

- When enabled (default), skin binding is imported and applied to geometry that has skeleton/deformation data in the GLTF/GLB file

- Required for animated or skinned meshes to work correctly in Maya
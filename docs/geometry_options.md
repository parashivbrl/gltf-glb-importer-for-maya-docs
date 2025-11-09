# Geometry Options

Controls how geometry vertices are processed during import:

**No merging** (Default)

- Keeps geometry components separate as authored

- Maintains original mesh structure

- Preserves material assignments per mesh

- Components remain detached along UV seams

**Merge Vertices**

- Uses an algorithm to merge vertices automatically

- Combines vertices that share the same position

- Can reduce geometry complexity but may affect color sets

- Suitable for most static geometry imports

**Skip Skin Binding**

- When enabled, skin binding data is ignored and geometry is imported without skeleton/deformation setup

- Useful when you only need the static geometry without animation or deformation capabilities

- When disabled (default), skin binding is imported and applied to geometry that has skeleton/deformation data in the GLTF/GLB file

- Required for animated or skinned meshes to work correctly in Maya
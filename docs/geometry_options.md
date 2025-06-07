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

**Merge Vertices (Alternative Method)**

- An additional option for vertex merging that provides different merging behavior

- Uses Maya's native merge vertices command

- **Note:** Should not be used with files containing rigged animation data or blendshape animations, as it tends to alter vertex data and can break animations.
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
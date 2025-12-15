# File Type Specific Options

The right side of the import dialog contains various import settings organized into collapsible sections. Here we focus on the **File Type Specific Options** which provide specialized controls for glTF/glb imports.

---

## File Type Specific Options

### Material Settings

- **Shader Type**: Set to **"Standard Surface"** (default)
- **Shading Option**: Set to **"Use Normal Data"** (default)
- **Import Ambient Occlusion**: AO will be multiplied with base color texture
- **Import Materials**: Imports materials from the GLB/GLTF file (enabled by default)

---

### Geometry Options

- **No merging**: Discontinuous geometry along the UV boundary/seams (default option)
- **Merge Vertices**: Combines duplicate vertices
- **Import Skin Binding**: Imports skin binding data from the GLB/GLTF file (enabled by default)
- **Use Exact Inverse Bind Matrices**: Uses exact inverse bind matrices for auto-generated assets from platforms like Sketchfab
- **Import Blendshapes**: Imports blendshape targets from the GLB/GLTF file (enabled by default)

---

### Animation Settings

- **Animation FPS**: Set the frame rate for imported animations (default: **"30 fps (NTSC)"**)
- **Import Animations**: Creates Maya keyframes for translation, rotation, and scale animations
- **Import Blendshape Animations**: Imports keyframes for blendshape weights (enabled by default)
- **Open Time Editor Window**: Opens Time Editor window for animation playback and editing

---

### Viewport Options

- **Focus view on imported objects**: Automatically focuses the viewport camera on imported objects
- **Animate framing**: Animates the camera framing to focus on imported objects

---

### Image Extraction

- **Use Relative Path**: Extracts images using relative path
- **Default Location**: Images will be extracted to the project directory/source images by default
  ```
  C:\Users\[User name]\Documents\maya\projects\default\sourceimages\gltf_textures
  ```
- **Relative Extraction**: Images will be extracted relative to GLB/GLTF file location when enabled

---

### UI Options

- **Dock Material_Animation UIs by default**: Automatically docks Material and Animation UI panels to the Maya interface when enabled

---

## Common to All File Types

### General Options

- **Group**: Groups imported objects together
- **Remove duplicate shading networks**: Removes redundant material connections
- **Merge Base Animation Layers**: Combines animation layers during import

---

### Referencing Options

- **Preserve references**: Maintains reference relationships
- **Load Settings**: Choose how to handle saved reference load states
- **Reserve unloaded namespaces**: Keeps namespace reservations

---

### Playback Options

- **Always Override if Scene is Empty**: Automatically overrides playback settings in empty scenes
- **Framerate Import**: Options for handling frame rate differences
- **Animation Range**: Settings for animation timeline handling
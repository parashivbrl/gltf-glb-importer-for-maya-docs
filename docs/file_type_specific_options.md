# File Type Specific Options

The right side of the import dialog contains various import settings organized into collapsible sections. Here we focus on the **File Type Specific Options** which provide specialized controls for glTF/glb imports.

---

## File Type Specific Options

### Material Settings

- **Shader Type**: Set to **"Standard Surface"** (default)
- **Shading Option**: Set to **"Use Normal Data"** (default)
- **Import Ambient Occlusion (AO)**: AO will be multiplied with base color texture
- **Skip Material Creation**: Skips material creation during import

---

### Geometry Options

- **No merging**: Discontinuous geometry along the UV boundary/seams (default option)
- **Merge Vertices**: Combines duplicate vertices
- **Skip Skin Binding**: Skips skin binding during import  

---

### Image Extraction

- **Use Relative Path**: Extracts images using relative path
- **Default Location**: Images will be extracted to the project directory/source images by default
  ```
  C:\Users\[User name]\Documents\maya\projects\default\sourceimages\gltf_textures
  ```
- **Relative Extraction**: Images will be extracted relative to GLB/GLTF file location when enabled

---

### Animation Settings

- **Import Animations**: Creates Maya keyframes for translation, rotation, and scale animations
- **Open Time Editor Window**: Opens Time Editor window for animation playback and editing

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
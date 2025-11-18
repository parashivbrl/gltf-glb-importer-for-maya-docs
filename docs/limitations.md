# Plugin Limitations and Known Issues

## Overview

While the glTF/GLB Importer for Maya successfully handles most files that adhere to the [Khronos glTF 2.0 specifications](https://www.khronos.org/gltf/), there are several known limitations and specific issues that users should be aware of.

> **Note:** For information about compatible assets and workarounds, see the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) guide.

---

## General Plugin Limitations

### Geometry Processing
- **Merge Vertices Side Effects**: When **Merge Vertices** is enabled during import, UVs can fail or distort because vertices that share the same position are de-duplicated, removing the seams needed to keep separate UV shells.
### Blendshape Animations (Maya 2023 and below)
- Blendshape targets and animation curves import, but in Maya 2023 and earlier they may not play back automatically.
- Open the **Time Editor** and use the **Bake** menu options (e.g., *Bake to New Clip*, *Bake to Scene*, *Bake to Scene and Delete*, or *Flatten Layers*) to bake the clips back to standard curves so playback works.
- Maya 2024+ plays the imported blendshape animation without baking.
- For a detailed baking workflow, see **For Assets with Animation Clips** in the [Asset Compatibility and Workarounds guide](compatibility_and_workarounds.md#for-assets-with-animation-clips).
### File Format Constraints
- **glTF Extensions**: Not all Khronos extensions are fully supported
- **Vendor Extensions**: Limited support for vendor-specific extensions

### Maya Integration Limitations
- **Viewport Performance**: Complex scenes with many materials may impact Maya's viewport performance

### Material and Texture Limitations
- **Texture Format Support**: Some texture formats such as .webp and Compressed BasisU images may not be supported
- **Material Complexity**: Advanced PBR features may not have direct Maya equivalents


---

## Sketchfab Asset Import Issues

Sketchfab assets, particularly those that are **automatically generated**, present specific challenges:

### Hierarchical Structure Problems
- **Different Node Hierarchy**: Sketchfab's auto-generated files follow a different hierarchical structure than standard glTF exporters
- **Rigged Asset Import Issues**: Due to the non-standard hierarchy, rigged characters and animated objects may not import properly

### Animation-Specific Problems
- **Skinning Data**: Vertex skinning information may not transfer correctly from Sketchfab's format
- **Animation Curves**: Complex animation curves may be simplified or corrupted during the conversion process

---

## Reporting Issues

If you encounter limitations not listed here, please report them through the [GitHub Issues page](https://github.com/parashivbrl/gltf-glb-importer-for-maya-docs/issues) and provide:

- Maya version and operating system

- Asset source (Sketchfab, custom export, etc.)

- File size and complexity details

- Specific error messages or unexpected behavior

- Sample files (when possible and appropriate)

- Output logs from the Maya Script Editor output window

- Steps to reproduce the issue

---

For the most up-to-date information on plugin improvements and bug fixes, check the project's release notes and documentation updates. 
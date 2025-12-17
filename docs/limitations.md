# Plugin Limitations and Known Issues

## Overview

While the glTF/GLB Importer for Maya successfully handles most files that adhere to the [Khronos glTF 2.0 specifications](https://www.khronos.org/gltf/), there are several known limitations and specific issues that users should be aware of.

> **Note:** For information about compatible assets and workarounds, see the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) guide.

---

## General Plugin Limitations

### Geometry Processing
- **Merge Vertices Side Effects**: When **Merge Vertices** is enabled during import, UV creation can fail in rare edge cases. When it works, UVs are created correctly with proper seams. Without merging, UVs are always created reliably.
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

Sketchfab assets, particularly those that are **automatically generated**, may present specific challenges due to non-standard bind pose configurations:

### Rigged Asset Deformation Issues
- **Skeletal Deformation Accuracy**: Auto-generated files may have non-standard bind pose configurations that can cause deformation issues when imported with default settings
- **Workaround**: Enable the **Use Exact Inverse Bind Matrices** option (available under skin binding settings) to use the exact inverse bind matrices from the glTF/GLB file, which provides more accurate skeletal deformation matching the original file's joint transformations
- **Note**: This option is only available when **Import Skin Binding** is enabled

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
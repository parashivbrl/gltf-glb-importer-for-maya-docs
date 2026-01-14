# Plugin Limitations and Known Issues

## Overview

While the glTF/GLB Importer for Maya successfully handles most files that adhere to the [Khronos glTF 2.0 specifications](https://www.khronos.org/gltf/), there are several known limitations and specific issues that users should be aware of.

> **Note:** For information about compatible assets and workarounds, see the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) guide.

---

## General Plugin Limitations

### Geometry Processing

- **Merge Vertices**: UVs are created correctly even when **Merge Vertices** is enabled. In rare edge cases, UV creation may fail.

### Blendshape Animations (Maya 2023 and below)

- Blendshape targets and animation curves import, but in Maya 2023 and earlier they may not play back automatically.
- Open the **Time Editor** and use the **Bake** menu options (e.g., _Bake to New Clip_, _Bake to Scene_, _Bake to Scene and Delete_, or _Flatten Layers_) to bake the clips back to standard curves so playback works.
- Maya 2024+ plays the imported blendshape animation without baking.
- For a detailed baking workflow, see **For Assets with Animation Clips** in the [Asset Compatibility and Workarounds guide](compatibility_and_workarounds.md#for-assets-with-animation-clips).

### File Format Constraints

- **glTF Extensions**: Not all Khronos extensions are fully supported
- **Vendor Extensions**: Limited support for vendor-specific extensions

### Maya Integration Limitations

- **Viewport Performance**: Complex scenes with many materials may impact Maya's viewport performance

### Material and Texture Limitations

- **Texture Format Support**: `.webp` support is **WIP**. Some texture formats such as Compressed BasisU images may not be supported.
- **Material Complexity**: Advanced PBR features may not have direct Maya equivalents

---

## Sketchfab Asset Import Issues

Sketchfab assets generally import correctly.

In rare edge cases (especially with auto-generated assets that have non-standard bind poses), you may still run into import issues.

### Rigged Asset Deformation Issues

- Rigged Sketchfab assets generally import correctly now.
- In rare edge cases, non-standard bind pose data may still cause deformation issues.
- **Workaround**: Re-import with **Import Skin Binding** enabled. The importer applies inverse bind matrices automatically, so no separate option is required.
- **If Issues Persist**: Use the Blender preprocessing workflow in [Asset Compatibility and Workarounds](compatibility_and_workarounds.md#alternative-blender-preprocessing-workflow)

---

## Reporting Issues

If you encounter limitations not listed here, please join the [Discord server](https://discord.gg/dtSxPaQ2) to report issues, share suggestions, view announcements, and get support.

When reporting issues, please provide:

- Maya version and operating system

- Asset source (Sketchfab, custom export, etc.)

- File size and complexity details

- Specific error messages or unexpected behavior

- Sample files (when possible and appropriate)

- Output logs from the Maya Script Editor output window

- Steps to reproduce the issue

---

For the most up-to-date information on plugin improvements and bug fixes, check the Discord server announcements and documentation updates.

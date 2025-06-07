# Plugin Limitations and Known Issues

## Overview

While the glTF/GLB Importer for Maya successfully handles most files that adhere to the [Khronos glTF 2.0 specifications](https://www.khronos.org/gltf/), there are several known limitations and specific issues that users should be aware of.

> 💡 **For information about compatible assets and workarounds, see the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) guide.**

---

## ⚠️ Sketchfab Asset Import Issues

Sketchfab assets, particularly those that are **automatically generated**, present specific challenges:

### Hierarchical Structure Problems
- **Different Node Hierarchy**: Sketchfab's auto-generated files follow a different hierarchical structure than standard glTF exporters
- **Rigged Asset Import Issues**: Due to the non-standard hierarchy, rigged characters and animated objects may not import properly
- **Bone/Joint Mapping**: The bone structure may not translate correctly to Maya's joint system

### Orientation and Positioning Issues
- **Incorrect Asset Orientation**: Even assets without animation data may be **incorrectly oriented** upon import
- **Coordinate System Differences**: Sketchfab's coordinate system transformations may not align with Maya's expectations
- **Scale Inconsistencies**: Assets may import at unexpected scales due to different unit interpretations

### Animation-Specific Problems
- **Joint-based Animations**: Assets with animations applied directly to joints often encounter import issues
- **Skinning Data**: Vertex skinning information may not transfer correctly from Sketchfab's format
- **Animation Curves**: Complex animation curves may be simplified or corrupted during the conversion process

---

## 🔧 General Plugin Limitations

### File Format Constraints
- **glTF Extensions**: Not all Khronos extensions are fully supported
- **Vendor Extensions**: Limited support for vendor-specific extensions
- **Binary Embedded Data**: Large embedded textures in GLB files may cause memory issues

### Maya Integration Limitations
- **Scene Scale**: Very large or very small assets may not import with appropriate scale
- **Viewport Performance**: Complex scenes with many materials may impact Maya's viewport performance

### Material and Texture Limitations
- **Texture Format Support**: Some texture formats such as .webp and Compressed BasisU images may not be supported
- **Material Complexity**: Advanced PBR features may not have direct Maya equivalents
- **UV Mapping**: Complex UV layouts may not preserve perfectly

### Animation and Rigging Constraints
- **Morph Targets**: Blend shape/morph target support may be limited
- **Complex Rigs**: Multi-layered rigging systems may not import completely
- **Animation Sampling**: High-frequency animations may be resampled during import

---

## 📋 Reporting Issues

If you encounter limitations not listed here, please provide:

- Maya version and operating system

- Asset source (Sketchfab, custom export, etc.)

- File size and complexity details

- Specific error messages or unexpected behavior

- Sample files (when possible and appropriate)

- Output logs from the Maya Script Editor output window

- Steps to reproduce the issue

---

For the most up-to-date information on plugin improvements and bug fixes, check the project's release notes and documentation updates. 
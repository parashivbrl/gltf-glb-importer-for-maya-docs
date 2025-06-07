# Supported Features

This page provides a comprehensive overview of all file formats, extensions, shaders, and image formats supported by the glTF/glb Importer for Maya plugin.

---

## 📁 Supported File Types

The plugin supports the following glTF file formats:

- **glTF** (`.gltf`) - JSON-based 3D scene format
- **glb** (`.glb`) - Binary glTF format with embedded resources

---

## 🔧 Supported Extensions

The plugin supports the following Khronos and vendor extensions:

### Khronos Extensions (KHR_)

| Extension | Description |
|-----------|-------------|
| `KHR_lights_punctual` | Point, spot, and directional lights |
| `KHR_materials_anisotropy` | Anisotropic material reflection |
| `KHR_materials_clearcoat` | Clear coat material layer |
| `KHR_materials_dispersion` | Chromatic dispersion effects |
| `KHR_materials_emissive_strength` | Enhanced emissive material strength |
| `KHR_materials_ior` | Index of refraction for materials |
| `KHR_materials_iridescence` | Iridescent material effects |
| `KHR_materials_sheen` | Fabric-like sheen material properties |
| `KHR_materials_specular` | Specular workflow materials |
| `KHR_materials_transmission` | Light transmission through materials |
| `KHR_materials_unlit` | Unlit/constant color materials |
| `KHR_materials_variants` | Multiple material variants per mesh |
| `KHR_materials_volume` | Transmission volume material properties |
| `KHR_texture_transform` | Texture coordinate transformations |

### Vendor Extensions (EXT_)

| Extension | Description |
|-----------|-------------|
| `EXT_mesh_gpu_instancing` | GPU-based mesh instancing |

---

## 🎨 Supported Shaders

The plugin supports conversion to the following Maya shader types:

- **Standard Surface** - Maya's standard physically-based shader
- **AiStandardSurface** - Arnold renderer's standard surface shader
- **OpenPBR** - Open-source physically-based rendering shader
- **StingrayPBS** - Stingray physically-based shader (only basic material properties: BaseColor, ORM, Normal, Emissive)

---

## 🖼️ Supported Image Formats

The plugin can process the following image formats for textures:

- **JPEG** (`.jpg`, `.jpeg`) - Compressed raster images
- **PNG** (`.png`) - Lossless compressed raster images with transparency support

---

## 📋 Compatibility Notes

- Extension support may vary depending on your Maya version and installed renderers
- Shader support depends on the renderers available in your Maya installation
- Image format support follows Maya's native texture loading capabilities

For specific compatibility issues and workarounds, see the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) page. 
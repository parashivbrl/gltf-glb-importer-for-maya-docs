# Material Settings

When importing GLTF/GLB files, you can configure various material settings to control how materials and geometry are processed.

## Shader Type

Controls which shader system is used for imported materials:

**Standard Surface** (Default)

- Uses Maya's Standard Surface shader for imported materials

- Provides physically-based rendering capabilities

- Compatible with Arnold and other modern renderers

**Arnold**

- Uses Arnold-specific shaders for material import

- Optimized for Arnold renderer workflows

- Best choice when primarily using Arnold for rendering

**OpenPBR**

- Uses OpenPBR (Open Physically Based Rendering) shaders

- Industry-standard for physically-based materials

- Provides cross-platform material compatibility

- **Note:** OpenPBR is not fully implemented in all renderers. Arnold may not render some material properties correctly, and some features may be approximated or unsupported. Consider using Standard Surface or Arnold shaders for production workflows requiring full compatibility.

**Stingray**

- Uses Stingray PBS (Physically Based Shader) materials

- Legacy option for older Maya workflows

- Maintained for backward compatibility

- **Note:** Stingray works only with basic material properties such as BaseColor, ORM (Occlusion/Roughness/Metallic), Normal, and Emission. Advanced material features may not be supported.

## Shading Option

Controls how normals and shading are handled during import:

**Use Normal Data** (Default)

- Preserves the original normal data from the GLTF/GLB file

- Maintains the intended shading as authored in the original model

**Harden edges**

- Converts to Maya's hard edge shading

- Creates sharp edges between faces

- Useful for mechanical or architectural models

**Soften edges**

- Applies Maya's soft edge shading

- Creates smooth transitions between faces

- Better for organic or character models

# Technical Details

## Plugin Usage

Once the plugin is successfully installed, it adds a new file type **"glTF2"** to Maya's import options. This enables users to import GLTF and GLB files directly through Maya's file import system or programmatically using MEL and Python commands.

### MEL Command

```mel
file -import -type "glTF2" -options "shaderType=Standard Surface;shadingOption=Use Normal Data;" "path_to_gltf";
```

### Python Command

```python
import maya.cmds as cmds

cmds.file({file_path}, 
          i=True, 
          type="glTF2",
          options="shaderType=Standard Surface;shadingOption=Use Normal Data;"
          )
```

### Import Options

The plugin supports various import options that can be specified in the `options` parameter as a semicolon-separated string in "key=value" format. **All options are optional** and will use their default values if not specified:

- **shaderType**: Specifies the shader type to use (default: "Standard Surface")
    *Valid values:* "Standard Surface", "Arnold", "OpenPBR", "Stingray"
- **shadingOption**: Controls how shading data is handled (default: "Use Normal Data")
    *Valid values:* 
    - "Use Normal Data", 
    - "Harden Edge", 
    - "Soften Edge"
- **importAO**: Whether to import Ambient Occlusion from ORM texture (R channel) and multiply with base color (default: 0/false)
- **importMaterials**: Whether to import materials/shaders during import (default: 1/true)
- **mergeVertices**: Whether to merge vertices (default: 0/false)
- **importSkinBinding**: Whether to import skin binding (skinCluster creation) during import (default: 1/true)
- **importBlendshapes**: Imports blendshape targets (default: 1/true)
- **animationFPS**: Frame rate for animation import (default: 30)
- **importAnimations**: Whether to import TRS animations from glTF file as Maya keyframes (default: 1/true)
- **importBlendshapeAnimations**: Imports blendshape weight keyframes (default: 1/true)
- **openTimeEditor**: Whether to open the Time Editor after import (default: 0/false)
- **focusView**: Whether to focus the view on imported geometry (default: 1/true)
- **animate**: Whether to animate the import process (default: 1/true)
- **useRelativePath**: Whether to use relative paths for textures (default: 0/false)

#### Options String Format
Options are specified as semicolon-separated key-value pairs: `"key1=value1;key2=value2;key3=value3"`

#### Example with Multiple Options
```mel
file -import -type "glTF2" -namespace "FILE_NAME" -options "shaderType=Standard Surface;mergeVertices=0;shadingOption=Use Normal Data;useRelativePath=0;openTimeEditor=0;importAnimations=1;importBlendshapeAnimations=0;importAO=0;importMaterials=1;importSkinBinding=1;importBlendshapes=1;focusView=1;animate=0;animationFPS=30;" "PATH_TO_GLTF";
```

### Integration with Custom Tools

These commands can be easily integrated into custom Maya tools and pipelines, allowing for automated GLTF/GLB import workflows. The programmatic interface makes it simple to batch process multiple files or incorporate GLTF/GLB import into larger automation scripts.
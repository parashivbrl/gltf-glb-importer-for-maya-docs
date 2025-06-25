# Technical Details

## Plugin Usage

Once the plugin is successfully installed, it adds a new file type **"GLTF/GLB"** to Maya's import options. This enables users to import GLTF and GLB files directly through Maya's file import system or programmatically using MEL and Python commands.

### MEL Command

```mel
file -import -type "GLTF/GLB" -options "shaderType=Standard Surface;shadingOption=Use Normal Data;" {file_path};
```

### Python Command

```python
import maya.cmds as cmds

cmds.file({file_path}, 
          i=True, 
          type="GLTF/GLB",
          options="shaderType=Standard Surface;shadingOption=Use Normal Data;"
          )
```

### Import Options

The plugin supports various import options that can be specified in the `options` parameter as a semicolon-separated string in "key=value" format. **All options are optional** and will use their default values if not specified:

- **shaderType**: Specifies the shader type to use (default: "Standard Surface")
- **mergeVertices**: Whether to merge vertices (default: 0/false)
- **shadingOption**: Controls how shading data is handled (default: "Use Normal Data")
    *Valid values:* 
    - "Use Normal Data", 
    - "Hard edge", 
    - "Soften edge"
- **useRelativePath**: Whether to use relative paths for textures (default: 0/false)
- **openTimeEditor**: Whether to open the Time Editor after import (default: 0/false)

#### Options String Format
Options are specified as semicolon-separated key-value pairs: `"key1=value1;key2=value2;key3=value3"`

#### Example with Multiple Options
```mel
file -import -type "GLTF/GLB" -options "shaderType=Standard Surface;shadingOption=Hard edges (Maya native);mergeVertices=1;useRelativePath=1;" "path/to/file.glb";
```

### Integration with Custom Tools

These commands can be easily integrated into custom Maya tools and pipelines, allowing for automated GLTF/GLB import workflows. The programmatic interface makes it simple to batch process multiple files or incorporate GLTF/GLB import into larger automation scripts.
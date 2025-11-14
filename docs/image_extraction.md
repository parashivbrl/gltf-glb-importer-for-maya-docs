# Image Extraction

When importing glTF/GLB files, you can choose where the extracted texture maps are saved by using the "Use Relative Path" checkbox option.

## Texture Map Save Locations

### Use Relative Path Unchecked (Default)
When the "Use Relative Path" checkbox is **unchecked**, images will be saved in the default Maya sourceimages directory or project directory:

For example:
```
C:\Users\{User name}\Documents\maya\projects\default\sourceimages\gltf_textures
```

### Use Relative Path Checked
When the "Use Relative Path" checkbox is **checked**, texture maps will be saved relative to the location of the imported GLB files.

This option is useful when you want to keep your textures organized alongside your model files or when working with portable project structures.


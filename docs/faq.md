# Frequently Asked Questions (FAQ)

## General Questions

??? question "What is the glTF/glb importer for Maya?"
    The glTF/glb importer for Maya is a plugin that allows you to import glTF (GL Transmission Format) and glb (Binary glTF) files directly into Autodesk Maya. This enables seamless integration of 3D assets that follow the glTF standard into your Maya workflow.

??? question "What versions of Maya are supported?"
    The plugin supports various versions of Maya. Please check the [Dependencies Installation](dependencies_installation.md) page for specific version compatibility information.

## Installation Questions

??? question "Why am I getting installation errors?"
    Common installation issues can be resolved by:

    1. Ensuring you have the correct Maya version
    2. Verifying all dependencies are properly installed
    3. Checking that you have sufficient permissions to install plugins
    4. Following the step-by-step instructions in [Plugin Installation](plugin_installation.md)

??? question "Do I need to install additional dependencies?"
    Yes, the plugin requires certain dependencies to function properly. Please follow the complete guide in [Dependencies Installation](dependencies_installation.md) before installing the plugin.

??? question "Where should I install the plugin files?"
    The plugin should be installed in Maya's plugin directory. Detailed installation paths and instructions are provided in the [Plugin Installation](plugin_installation.md) guide.

## Import Questions

??? question "What file formats are supported?"
    The plugin supports both:
    
    - **.gltf** files (JSON format with external assets)
    - **.glb** files (binary format with embedded assets)

??? question "Why isn't my glTF/glb file importing correctly?"
    Several factors can affect import success:

    1. **File compatibility**: Check [Asset Compatibility and Workarounds](compatibility_and_workarounds.md)
    2. **File format issues**: Ensure your file follows glTF 2.0 specifications
    3. **Missing textures**: Verify all referenced textures are available
    4. **Large file size**: Very large files may require specific settings

??? question "Can I import animations from glTF/glb files?"
    Yes! The plugin supports animation import. Configure your animation settings using the [Animation Settings](animation_settings.md) options before importing.

??? question "How do I handle material variants?"
    Material variants are supported through the [Show Material Variants](show_material_variants.md) feature. This allows you to switch between different material configurations defined in your glTF file.

## Material Questions

??? question "Why don't my materials look correct after import?"
    Material appearance can be affected by:

    1. **Material settings**: Adjust options in [Material Settings](material_settings.md)
    2. **Texture paths**: Ensure textures are properly linked
    3. **Maya's material system**: Some glTF material features may need manual adjustment
    4. **Lighting setup**: Your Maya scene lighting affects material appearance

??? question "Can I extract textures during import?"
    Yes, you can extract and save textures using the [Image Extraction](image_extraction.md) feature. This is particularly useful for glb files where textures are embedded.

??? question "How do I handle PBR materials?"
    The plugin attempts to convert PBR (Physically Based Rendering) materials to Maya-compatible materials. Some manual adjustment may be required for optimal results.

## Performance Questions

??? question "Why is my import taking so long?"
    Import time can be affected by:

    1. **File size**: Larger files take more time to process
    2. **Geometry complexity**: High-poly models require more processing
    3. **Texture resolution**: Large textures increase import time
    4. **Computer specifications**: Available RAM and CPU power

??? question "Can I optimize import performance?"
    Yes, you can improve performance by:

    1. Using appropriate [Geometry Options](geometry_options.md)
    2. Adjusting texture import settings
    3. Using [File Type Specific Options](file_type_specific_options.md)

## Troubleshooting

??? question "The plugin menu doesn't appear in Maya"
    If the [GLB/GLTF Menu](glb_gltf_menu.md) is not visible:

    1. Verify the plugin is properly installed
    2. Check that the plugin is loaded in Maya's Plugin Manager
    3. Restart Maya after installation
    4. Check Maya's script editor for error messages

??? question "I'm getting error messages during import"
    Common solutions:

    1. Check the [Limitations and Known Issues](limitations.md) page
    2. Verify your file meets glTF 2.0 specifications
    3. Try importing a simpler test file first
    4. Check Maya's script editor for detailed error information

??? question "My animations aren't playing correctly"
    Animation issues can often be resolved by:

    1. Checking [Animation Settings](animation_settings.md) configuration
    2. Using [Show Animation Clips](show_animation_clips.md) to manage multiple animations
    3. Verifying timeline settings in Maya
    4. Checking for keyframe import options

## Advanced Usage

??? question "Can I batch import multiple files?"
    The plugin focuses on individual file import. For batch operations, you may need to use Maya's scripting capabilities or import files one at a time.

??? question "How do I handle very large glTF scenes?"
    For large scenes:

    1. Consider splitting the scene into smaller files
    2. Use selective import options
    3. Optimize geometry before import
    4. Monitor Maya's memory usage

??? question "Can I modify import settings after import?"
    Import settings apply during the import process. To change settings, you'll need to re-import the file with new configuration options.

## Getting Help

??? question "Where can I find more technical information?"
    Detailed technical information is available in the [Technical Details](technical_details.md) section.

??? question "How do I report bugs or request features?"
    Please refer to the project repository for information on reporting issues and requesting new features.

??? question "Are there example files I can use for testing?"
    Check the glTF sample repository or create simple test files to verify your installation and understand the import process.

---

*If your question isn't answered here, please check the other documentation pages or refer to the project's issue tracker for additional support.* 
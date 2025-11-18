# Frequently Asked Questions (FAQ)

## General Questions

??? question "What is the glTF/glb importer for Maya?"
    The glTF/glb importer for Maya is a plugin that allows you to import glTF (GL Transmission Format) and glb (Binary glTF) files directly into Autodesk Maya. This enables seamless integration of 3D assets that follow the glTF standard into your Maya workflow.

??? question "What versions of Maya are supported?"
    The plugin supports **Maya 2024 or later**. For Maya 2024, you'll need to install numpy separately. Maya 2025+ includes numpy by default. See the [Dependencies Installation](dependencies_installation.md) page for detailed requirements.

## Installation Questions

??? question "Why am I getting installation errors?"
    Common installation issues can be resolved by:

    1. Ensuring you have the correct Maya version
    2. Verifying all dependencies are properly installed
    3. Checking that you have sufficient permissions to install plugins
    4. Following the step-by-step instructions in [Plugin Installation](plugin_installation.md)

??? question "Do I need to install additional dependencies?"
    **For Maya 2024**: Yes, you need to install numpy. **For Maya 2025+**: No additional dependencies are required as numpy is included by default. Please follow the complete guide in [Dependencies Installation](dependencies_installation.md) for installation instructions.

??? question "Where should I install the plugin files?"
    Extract the downloaded zip and copy the contents of the `scripts` folder to your user-specific Maya `.../scripts` directory, and the contents of the `plug-ins` folder to the matching `.../plug-ins` directory (create it if it does not exist). Refer to the platform-specific steps in [Plugin Installation](plugin_installation.md) for exact paths on Windows, macOS, and Linux.

## Import Questions

??? question "What file formats are supported?"
    The plugin supports both:
    
    - **.gltf** files (JSON format with external assets)
    - **.glb** files (binary format with embedded assets)

??? question "Why isn't my glTF/glb file importing correctly?"
    Several factors can affect import success:

    1. **File compatibility**: Check [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) - Note that Sketchfab auto-generated assets may require preprocessing
    2. **File format issues**: Ensure your file follows glTF 2.0 specifications
    3. **Missing textures**: Verify all referenced textures are available
    4. **Large file size**: Very large files may require specific settings
    5. **Asset source**: Assets from Khronos Sample Assets, Maya/Babylon exporter, or Blender/glTF 2.0 exporter typically work best

??? question "Can I import animations from glTF/glb files?"
    Yes! The plugin supports animation import including skeletal animations, transform-based animations, and morph targets. Configure your animation settings using the [Animation Settings](animation_settings.md) options before importing. You can enable "Open Time Editor Window" to automatically open Maya's Time Editor after import for immediate access to animation clips. You can also use the [Show Animation Clips](show_animation_clips.md) feature to manage multiple animation clips, which are automatically organized in Maya's Time Editor.

??? question "How do I handle material variants?"
    Material variants are supported through the [Show Material Variants](show_material_variants.md) feature. This allows you to switch between different material configurations defined in your glTF file.

## Material Questions

??? question "Why don't my materials look correct after import?"
    Material appearance can be affected by:

    1. **Shader type selection**: Choose the appropriate shader type in [Material Settings](material_settings.md) - Standard Surface (default), Arnold, OpenPBR (Maya 2025+), or Stingray
    2. **Shader limitations**: Note that Stingray only supports basic properties (BaseColor, ORM, Normal, Emissive), and OpenPBR may have rendering limitations with Arnold
    3. **Ambient Occlusion**: Enable "Import Ambient Occlusion" in [Material Settings](material_settings.md) to import AO from ORM texture (R channel) and multiply with base color for added depth
    4. **Texture paths**: Ensure textures are properly linked
    5. **Maya's material system**: Some glTF material features may need manual adjustment
    6. **Lighting setup**: Your Maya scene lighting affects material appearance

??? question "Can I extract textures during import?"
    The importer handles textures differently depending on the file type:
    
    - **GLB files**: The importer needs to extract and save textures using the [Image Extraction](image_extraction.md) feature because textures are embedded in the binary file. By default (when "Use Relative Path" is unchecked), textures are saved to your Maya project's sourceimages directory (e.g., `C:\Users\{User name}\Documents\maya\projects\default\sourceimages\gltf_textures`). When "Use Relative Path" is enabled, textures are saved relative to the GLB file location, which is useful for portable project structures.
    
    - **GLTF files**: Extraction is not needed because textures are external files. The texture image paths will be set relative to the GLTF file location automatically.

??? question "How do I handle PBR materials?"
    The plugin converts PBR (Physically Based Rendering) materials to Maya-compatible materials. You can choose from multiple shader types:
    
    - **Standard Surface** (default): Best for general use with Arnold and other renderers
    - **Arnold**: Optimized for Arnold renderer workflows
    - **OpenPBR** (Maya 2025+): Industry-standard PBR shader, though Arnold may not render all properties correctly
    - **Stingray**: Legacy option, only supports basic material properties (BaseColor, ORM, Normal, Emissive)
    
    Additionally, you can enable "Import Ambient Occlusion" to import AO from ORM texture (R channel) and multiply it with base color for enhanced depth and shadow detail. Some manual adjustment may be required for optimal results depending on your chosen shader type.

## Performance Questions

??? question "Why is my import taking so long?"
    Import time can be affected by:

    1. **File size**: Larger files take more time to process
    2. **Geometry complexity**: High-poly models require more processing
    3. **Texture resolution**: Large textures increase import time
    4. **Complex rigged assets**: Assets with complex rigging and skin binding may take longer due to the complex skin binding process
    5. **Computer specifications**: Available RAM and CPU power

??? question "Can I optimize import performance?"
    Yes, there are several ways to optimize import performance depending on your needs:

    **For Static Geometry (No Animation Needed):**
    - Disable "Import Animations" in [Animation Settings](animation_settings.md) to skip all animation processing
    - Disable "Import Skin Binding" in [Geometry Options](geometry_options.md) to avoid processing skeleton and skinning data, which significantly speeds up imports for complex rigged assets

    **For Geometry Optimization:**
    - Use "Merge Vertices" in [Geometry Options](geometry_options.md) to reduce geometry complexity, which can speed up processing for high-poly models

    **For Material Optimization:**
    - Disable "Import Materials" in [Material Settings](material_settings.md) if you only need geometry and plan to assign materials manually later


    These optimizations are particularly effective for large files, complex rigged assets, or when you only need specific aspects of the imported content.

## Troubleshooting

??? question "The plugin menu doesn't appear in Maya"
    If the [glTF2.0](gltf2_0_menu.md) menu is not visible:

    1. Verify the plugin is properly installed
    2. Check that the plugin is loaded in Maya's Plugin Manager
    3. Restart Maya after installation
    4. Check Maya's script editor for error messages

??? question "I'm getting error messages during import"
    Common solutions:

    1. Check the [Limitations and Known Issues](limitations.md) page
    2. Verify your file meets glTF 2.0 specifications
    3. Try importing a simpler test file first - Test with assets from the [Khronos Sample Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets)
    4. Check Maya's script editor for detailed error information
    5. If importing Sketchfab assets, see [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) for preprocessing steps

??? question "My animations aren't playing correctly"
    Animation issues can often be resolved by:

    1. Checking [Animation Settings](animation_settings.md) configuration — ensure "Import Animations" (and "Import Blendshape Animations" if needed) is enabled
    2. Setting Maya's playback speed to **Real-time** in the Time Slider options so imported FPS is respected
    3. Enabling "Open Time Editor Window" in [Animation Settings](animation_settings.md) to automatically open the Time Editor after import for easier access to animation clips
    4. Using [Show Animation Clips](show_animation_clips.md) to manage multiple animations — all clips are organized in Maya's Time Editor
    5. If you're on Maya 2023 or earlier and blendshape animations don't play, bake the clips via the Time Editor's **Bake** menu as described in the [Asset Compatibility and Workarounds](compatibility_and_workarounds.md#for-assets-with-animation-clips) guide
    6. Verifying timeline settings in Maya
    7. Note: Sketchfab assets with rigged animations may require preprocessing (see [Asset Compatibility and Workarounds](compatibility_and_workarounds.md))

## Advanced Usage

??? question "Can I batch import multiple files?"
    The plugin focuses on individual file import. For batch operations, you can use Maya's scripting capabilities with the programmatic interface. See [Technical Details](technical_details.md) for MEL and Python command examples.

??? question "How do I handle very large glTF scenes?"
    For large scenes:

    1. Consider splitting the scene into smaller files
    2. Use selective import options - Disable "Import Skin Binding" if you don't need animation, or disable "Import Materials" to import geometry only
    3. Optimize geometry before import
    4. Monitor Maya's memory usage
    5. Use "Merge Vertices" option to reduce geometry complexity

??? question "Can I re-export imported glTF/GLB files using Babylon exporter?"
    Yes, but there are important considerations for round-trip workflows:

    1. **Material compatibility**: Use **Stingray** shader when importing if you plan to re-export with Babylon, as Babylon doesn't work well with Standard Surface, Arnold, or OpenPBR shaders
    2. **Animation clips**: If your file has animation clips, you'll need to bake them from Time Editor to scene animation before exporting. See [Asset Compatibility and Workarounds](compatibility_and_workarounds.md) for the complete round-trip workflow
    3. **Material limitations**: Babylon only supports basic material properties with Stingray shader and doesn't support glTF extensions with Stingray

??? question "What's the difference between 'No merging' and 'Merge Vertices' geometry options?"
    - **No merging** (default): Preserves original mesh structure, keeps components separate along UV seams, maintains material assignments per mesh
    - **Merge Vertices**: Automatically combines vertices that share the same position, can reduce geometry complexity but may affect color sets
    - **Import Skin Binding**: When enabled (default), imports skin binding data and applies it to geometry with skeleton/deformation data. When disabled, ignores skin binding data and imports static geometry only - useful when you don't need animation or deformation

??? question "Can I modify import settings after import?"
    Import settings apply during the import process. To change settings, you'll need to re-import the file with new configuration options. However, you can modify materials, apply material variants using [Show Material Variants](show_material_variants.md), and manage animation clips using [Show Animation Clips](show_animation_clips.md) after import.

## Getting Help

??? question "Where can I find more technical information?"
    Detailed technical information is available in the [Technical Details](technical_details.md) section, including programmatic import using MEL and Python commands with all available import options.

??? question "How do I report bugs or request features?"
    You can report bugs or request features through the [GitHub Issues page](https://github.com/parashivbrl/gltf-glb-importer-for-maya-docs/issues). When reporting issues, please include:
    
    1. Maya version and operating system
    2. Asset source (Sketchfab, custom export, etc.)
    3. File size and complexity details
    4. Specific error messages or unexpected behavior
    5. Sample files (when possible and appropriate)
    6. Output logs from the Maya Script Editor
    7. Steps to reproduce the issue

??? question "Are there example files I can use for testing?"
    The [Khronos glTF Sample Assets repository](https://github.com/KhronosGroup/glTF-Sample-Assets) provides official test assets that work well with the plugin. These are recommended for testing your installation and understanding the import process. Assets exported from Maya using Babylon exporter or from Blender using the built-in glTF 2.0 addon also work reliably.

---

*If your question isn't answered here, please check the other documentation pages or refer to the project's issue tracker for additional support.* 
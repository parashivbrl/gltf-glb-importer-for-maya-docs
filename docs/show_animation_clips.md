# Show Animation Clips

The Animation Clips Manager allows you to view and manage animation clips associated with imported GLTF/GLB files. This interface provides an organized way to access different animations contained within your 3D assets.

<video controls preload="metadata" style="width: 100%; max-width: 800px; display: block; margin: 0 auto;">
  <source src="../vid/animation_clips_demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>

*Courtesy by Khronos glTF sample assets*

## Integration with Maya's Time Editor

The plugin leverages Maya's powerful Time Editor to organize and display all compositions and their corresponding animation clips as individual tracks. When you import a GLTF/GLB file, the plugin automatically creates a structured timeline where:

- Each **composition** appears as a main grouping in the Time Editor
- Each **animation clip** within a composition is created in its own track
- The clips in the corresponding tracks are clearly labeled with their respective animation names
- You can easily navigate between different compositions using the dropdown composition selector

This integration provides a familiar and powerful interface for managing complex animation sequences, allowing you to work with imported animations using Maya's native timeline tools.

## Using the Animation Clips Manager

In the Animation Clips Manager, you'll see:

1. **Composition Dropdown**: At the top, select the composition you want to work with from the dropdown menu.

2. **Animation Clips List**: Below the composition selector, you'll see a list of all available animation clips for the selected composition. Each clip represents a different animation sequence defined in the imported gltf file.

3. **Clip Information**: At the bottom, the manager displays how many animation clips are available for the currently selected composition.

## Features

- **Time Editor Integration**: Each animation clip is automatically organized into its own track within a dedicated composition in Maya's Time Editor.
- **Multiple Compositions**: Switch between different compositions using the dropdown to access their respective animation clips
- **Clip Organization**: All animation clips are clearly listed and organized by composition
- **Native Maya Workflow**: Work with imported animations using Maya's familiar timeline interface
- **Easy Access**: Quickly browse through available animations without needing to manually search through the scene

All animation clips are extracted as defined in the GLTF/GLB file, maintaining the original structure and organization of the animations.
# Animation Settings

When importing GLTF/GLB files, you can configure animation settings to control how animations are processed and displayed.

> **Note:** Before previewing imported animation, set Maya's Time Slider playback speed to **Real-time** (`Playback Speed > Real-time`). The other options—**Play Every Frame, Free** and **Play Every Frame, Max Real-time**—ignore the FPS chosen below and can make animation appear too fast or too slow.

## Animation FPS

- Choose the playback rate for imported animations from the dropdown
- Default is **30 fps (NTSC)**, but presets such as 15 fps (Game), 24 fps (Film), 25 fps (PAL), 48 fps (Show), 50 fps (PAL Field), and 60 fps (NTSC Field) are available
- **24 fps** and **30 fps** cover most use cases
- Use this setting to match the project frame rate before importing

## Import Animations

- When enabled (default), brings in all animation data, including skeletal motion, object transforms, and camera animation, creating the corresponding Maya keyframes
- Disable if you only need static meshes and want to avoid adding keys to the scene
- Helpful to leave off when you plan to author new animation in Maya and only use the imported geometry

## Import Blendshape Animations

- When enabled (default), imports blendshape weight keyframes from the GLTF/GLB file
- Required for facial animation or any deformation driven by blendshape curves
- Disable if you only need static blendshape targets without animation to reduce scene keyframe data

## Open Time Editor Window

- When enabled, launches the Maya Time Editor immediately after import so you can inspect and tweak the new animation clips
- Helpful when you expect to edit or retime the imported animation right away
- Disabled by default to avoid interrupting the workflow if you only need the animation loaded into the scene
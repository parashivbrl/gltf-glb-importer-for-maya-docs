# Animation Settings

When importing GLTF/GLB files, you can configure animation settings to control how animations are processed and displayed.

## Import Animations

Controls whether animations are imported from the GLTF/GLB file:

- When enabled (default), creates Maya keyframes for translation, rotation, and scale animations

- Imports all animation data from the file, including bone animations, object transformations, and camera animations

- When disabled, animation data is ignored and only static geometry is imported

- Useful when you only need the static model without animation data

## Open Time Editor Window

Controls whether the Time Editor window opens automatically after import:

- When enabled, the Maya Time Editor window automatically opens when importing animated GLTF/GLB files

- Provides immediate access to view and edit the imported animation clips

- Useful for quickly reviewing and editing imported animations

- When disabled (default), animations are imported but the Time Editor window does not open automatically
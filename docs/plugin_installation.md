# Plugin Installation

<iframe width="100%" height="450" style="max-width: 800px; display: block; margin: 0 auto;" src="https://www.youtube.com/embed/ETs-TUvhtLs" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Plugin Download

- **Get** the plugin from the [Gumroad page](https://bit.ly/4agx5T2).
- **Extract** the downloaded archive to a temporary location.

The archive contains a `gltf2ImporterForMaya/` folder with `PackageContents.xml` and a `Contents` folder. Inside `Contents` there is a `plugin` folder with the actual plugin files:

- `gltf2_importer_plugin.py` — plugin loader
- `gltf2_importer` — plugin Python package/folder
- `extern_draco.dll` — native Draco decoder (Windows only; enables `KHR_draco_mesh_compression`)
- `gltfImportOptions.mel` — UI MEL script

You can install the plugin using either of two methods:

1. **Autodesk Application Plug-in Package (recommended)**: Copy the entire `gltf2ImporterForMaya` package folder to the appropriate `ApplicationPlugins` location for your OS (see the Installation section below).

2. **Manual install (classic method)**: Extract the individual plugin files from `gltf2ImporterForMaya/Contents/plugin/` and manually copy them into your per-user Maya `plug-ins` and `scripts` folders as described in the Manual install sections below.

---

## Installation

### Windows

#### Autodesk Application Plug-in Package format (recommended)

- **Close Maya**: Make sure Maya is not running.
- **Install**: Copy the entire extracted `gltf2ImporterForMaya` package folder into:

  ```
  C:\ProgramData\Autodesk\ApplicationPlugins\gltf2ImporterForMaya
  ```

- The package must contain a top-level `PackageContents.xml` and a `Contents` folder. Inside `Contents` there should be a `plugin` folder which holds the actual plugin files.
- Maya (versions 2022 through 2026) will automatically detect and load the package at startup.
- **Restart Maya** and confirm the `glTF2.0` menu appears and the `glTF2.0 Import` file type is available in Maya's import window.

#### Manual install (legacy, per-user)

- **Close Maya**: Make sure Maya is not running.
- Copy `gltf2_importer_plugin.py` into:

  ```
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\plug-ins
  ```

  Create the `plug-ins` directory if it does not exist.

- Copy the following files into your per-user `scripts` folder:

  - `gltf2_importer` (folder)
  - `extern_draco.dll`
  - `gltfImportOptions.mel`

  Put them into:

  ```
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\scripts
  ```

  Create the `scripts` directory if it does not exist.

- **Restart Maya** and open it again.
- **Enable**: Go to **Windows > Settings/Preferences > Plug-in Manager**, verify `gltf2_importer_plugin.py` loads (Load + Auto Load checked)

#### Updating / Uninstalling

- When updating the plugin, delete any previous installation first.
- Application Plug-in Package install: delete:

  ```
  C:\ProgramData\Autodesk\ApplicationPlugins\gltf2ImporterForMaya
  ```

- Manual/per-user install: delete:

  ```
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\plug-ins\gltf2_importer_plugin.py
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\scripts\gltf2_importer
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\scripts\extern_draco.dll
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\scripts\gltfImportOptions.mel
  ```

---

### macOS

#### Autodesk Application Plug-in Package format (recommended)

- **Close Maya**
- Copy the `gltf2ImporterForMaya` package folder to one of the ApplicationPlugins locations on macOS:

  - Typical (shared for all users):

    ```
    /Users/Shared/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
    ```

  - User-specific (single user):

    ```
    ~/Library/Application Support/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
    ```

  - System-wide (all users):

    ```
    /Library/Application Support/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
    ```

- The package must contain a top-level `PackageContents.xml` and a `Contents` folder (see example structure above).
- Maya (versions 2022 through 2026) will automatically detect and load the package at startup.
- **Restart Maya** and confirm the `glTF2.0` menu appears and the `glTF2.0 Import` file type is available in Maya's import window.

#### Manual install (legacy, per-user)

- **Close Maya**
- Copy `gltf2_importer_plugin.py` into:

  ```
  ~/Library/Preferences/Autodesk/maya/<Maya version>/plug-ins
  ```

  Create the `plug-ins` directory if it does not exist.

- Copy the following into your per-user `scripts` folder:

  - `gltf2_importer` (folder)
  - `gltfImportOptions.mel`

  Put them into:

  ```
  ~/Library/Preferences/Autodesk/maya/<Maya version>/scripts
  ```

  Create the `scripts` directory if it does not exist.

- **Restart Maya**
- **Enable**: In **Windows > Settings/Preferences > Plug-in Manager**, confirm `gltf2_importer_plugin.py` is loaded (Load + Auto Load)

#### Updating / Uninstalling

- When updating the plugin, delete any previous installation first.
- Application Plug-in Package install: delete `gltf2ImporterForMaya` from whichever location you used:

  ```
  /Users/Shared/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
  ~/Library/Application Support/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
  /Library/Application Support/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
  ```

- Manual/per-user install: delete:

  ```
  ~/Library/Preferences/Autodesk/maya/<Maya version>/plug-ins/gltf2_importer_plugin.py
  ~/Library/Preferences/Autodesk/maya/<Maya version>/scripts/gltf2_importer
  ~/Library/Preferences/Autodesk/maya/<Maya version>/scripts/gltfImportOptions.mel
  ```

---

### Linux

#### Autodesk Application Plug-in Package format (recommended)

- **Close Maya**
- Copy the `gltf2ImporterForMaya` package folder to one of these ApplicationPlugins locations:

  - System-wide:

    ```
    /usr/autodesk/ApplicationPlugins/gltf2ImporterForMaya
    ```

  - Per-user:

    ```
    $HOME/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
    ```

- The package must contain a top-level `PackageContents.xml` and a `Contents` folder (see example structure above).
- Maya (versions 2022 through 2026) will automatically detect and load the package at startup.
- **Restart Maya** and confirm the `glTF2.0` menu appears and the `glTF2.0 Import` file type is available in Maya's import window.

#### Manual install (legacy, per-user)

- **Close Maya**
- Copy `gltf2_importer_plugin.py` to:

  ```
  $HOME/maya/<Maya version>/plug-ins
  ```

  Create the `plug-ins` directory if it does not exist:

  ```bash
  mkdir -p $HOME/maya/<Maya version>/plug-ins
  ```

- Copy the support files to your per-user `scripts` folder:

  - `gltf2_importer` (folder)
  - `gltfImportOptions.mel`

  Put them into:

  ```
  $HOME/maya/<Maya version>/scripts
  ```

  Create it if needed:

  ```bash
  mkdir -p $HOME/maya/<Maya version>/scripts
  ```

- **Restart Maya**
- **Enable** in the Plug-in Manager and ensure `gltf2_importer_plugin.py` autoloads

#### Updating / Uninstalling

- When updating the plugin, delete any previous installation first.
- Application Plug-in Package install: delete `gltf2ImporterForMaya` from whichever location you used:

  ```
  /usr/autodesk/ApplicationPlugins/gltf2ImporterForMaya
  $HOME/Autodesk/ApplicationPlugins/gltf2ImporterForMaya
  ```

- Manual/per-user install: delete:

  ```
  $HOME/maya/<Maya version>/plug-ins/gltf2_importer_plugin.py
  $HOME/maya/<Maya version>/scripts/gltf2_importer
  $HOME/maya/<Maya version>/scripts/gltfImportOptions.mel
  ```

If the plugin doesn't appear after installation, follow the Verification steps below to troubleshoot.

## Verification

After installation, you should see the **glTF2.0** menu item in the main maya window and file type **glTF2.0 Import** available in the Maya's native import window.

If the plugin doesn't appear:

1. **Check file locations** - Ensure the scripts and plug-ins files were copied to the correct user folders
2. **Verify plugin status** - Make sure the plugin is enabled in the Plug-in Manager. Should be enabled automaticaly when Maya launches
3. **Restart Maya** - Close and reopen Maya completely
4. **Check for errors** - Look at Maya's Script Editor for any error messages

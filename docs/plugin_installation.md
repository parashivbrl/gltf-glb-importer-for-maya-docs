# Plugin Installation

<iframe width="100%" height="450" style="max-width: 800px; display: block; margin: 0 auto;" src="https://www.youtube.com/embed/0Uzvw5Tr1ys" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Plugin Download

- **Get** the plugin from the [Gumroad page](https://bit.ly/4agx5T2)
- **Extract** the archive to a temporary location
- Inside the zip you will find two folders:
  - `plug-ins/`
  - `scripts/`

You will copy the contents of those folders into Maya's user-specific folders for each platform in the steps below.

---

## Installation

### Windows

- **Close Maya**: Make sure Maya is not running
- **Scripts**: Copy everything inside the extracted `scripts` folder into
  ```
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\scripts
  ```
  Create the `scripts` directory if it does not exist.
- **Plug-ins**: Copy everything inside the extracted `plug-ins` folder into
  ```
  C:\Users\<USER NAME>\Documents\maya\<Maya version>\plug-ins
  ```
  The folder name must be `plug-ins`. Create it if needed.
- **Restart Maya** and open it again
- **Enable**: Go to **Windows > Settings/Preferences > Plug-in Manager**, verify `gltf2_importer_plugin.py` loads automatically (Load + Auto Load checked)

---

### macOS

- **Close Maya**
- **Scripts**: Copy everything inside `scripts` to
  ```
  ~/Library/Preferences/Autodesk/maya/<Maya version>/scripts
  ```
  Use `Cmd+Shift+G` in Finder and enter the path above. Create the `scripts` directory if it is missing.
- **Plug-ins**: Copy everything inside `plug-ins` to
  ```
  ~/Library/Preferences/Autodesk/maya/<Maya version>/plug-ins
  ```
  The folder must be named `plug-ins`. Create it if needed.
- **Restart Maya**
- **Enable**: In **Windows > Settings/Preferences > Plug-in Manager**, confirm `gltf2_importer_plugin.py` is loaded (Load + Auto Load)

---

### Linux

- **Close Maya**
- **Scripts**: Copy everything inside `scripts` to
  ```
  $HOME/maya/<Maya version>/scripts
  ```
  Create the `scripts` directory if it does not exist:
  ```bash
  mkdir -p $HOME/maya/<Maya version>/scripts
  ```
- **Plug-ins**: Copy everything inside `plug-ins` to
  ```
  $HOME/maya/<Maya version>/plug-ins
  ```
  Create it if needed:
  ```bash
  mkdir -p $HOME/maya/<Maya version>/plug-ins
  ```
- **Restart Maya**
- **Enable** in the Plug-in Manager and ensure `gltf2_importer_plugin.py` autoloads

---

## Verification

After installation, you should see the **glTF2.0** menu item in the main maya window and file type **glTF2** available in the Maya's native import window. 

If the plugin doesn't appear:

1. **Check file locations** - Ensure the scripts and plug-ins files were copied to the correct user folders
2. **Verify plugin status** - Make sure the plugin is enabled in the Plug-in Manager. Should be enabled automaticaly when Maya launches
3. **Restart Maya** - Close and reopen Maya completely
4. **Check for errors** - Look at Maya's Script Editor for any error messages
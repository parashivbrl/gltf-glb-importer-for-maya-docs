# Plugin Installation

## Plugin Download

- **Download** the `glbgltfimporter.zip` from the [GitHub releases page](https://github.com/gltf-io/gltf-glb-importer-for-maya/releases)
- **Extract** the downloaded archive to a temporary location

---

## Installation

### Windows

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Scripts**: Copy the contents of the `scripts` folder from the extracted archive and paste them into:
   ```
   C:\Users\[Username]\Documents\maya\[version]\scripts
   ```

3. **Copy Plugins**: Copy the contents of the `plug-ins` folder from the extracted archive and paste them into:
   ```
   C:\Users\[Username]\Documents\maya\[version]\plug-ins
   ```
   > **Note**: If the `plug-ins` directory doesn't exist in your Maya documents folder, create it manually and the name should be "plug-ins" all lowercase.

4. **Restart Maya**: Launch Maya again

5. **Open Plugin Manager**: Go to **Windows > Settings/Preferences > Plug-in Manager**

6. **Enable Plugin**: Find `glbgltfimporter_plugin.py` in the list and enable both Load and Auto Load:

---

### macOS

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Scripts**: Copy the contents of the `scripts` folder from the extracted archive and paste them into:
   ```
   ~/Documents/maya/[version]/scripts
   ```

3. **Copy Plugins**: Copy the contents of the `plug-ins` folder from the extracted archive and paste them into:
   ```
   ~/Documents/maya/[version]/plug-ins
   ```
   > **Note**: If the `plug-ins` directory doesn't exist, create it manually.

4. **Restart Maya**: Launch Maya again

5. **Open Plugin Manager**: Go to **Maya > Preferences > Plug-in Manager** (or **Windows > Settings/Preferences > Plug-in Manager**)

6. **Enable Plugin**: Find `glbgltfimporter_plugin.py` in the list and enable both Load and Auto Load:

---

### Linux

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Scripts**: Copy the contents of the `scripts` folder from the extracted archive and paste them into:
   ```
   ~/maya/[version]/scripts
   ```

3. **Copy Plugins**: Copy the contents of the `plug-ins` folder from the extracted archive and paste them into:
   ```
   ~/maya/[version]/plug-ins
   ```
   > **Note**: If the `plug-ins` directory doesn't exist, create it manually.

4. **Restart Maya**: Launch Maya again

5. **Open Plugin Manager**: Go to **Windows > Settings/Preferences > Plug-in Manager**

6. **Enable Plugin**: Find `glbgltfimporter_plugin.py` in the list and enable both Load and Auto Load:

---

## Verification

After installation, you should see the **GLB/GLTF menu item** in the main maya window and file type **glTF/glb** available in the Maya's native import window. 

If the plugin doesn't appear:

1. **Check file locations** - Ensure that all files were copied to the correct directories
2. **Verify plugin status** - Make sure the plugin is enabled in the Plug-in Manager
3. **Restart Maya** - Close and reopen Maya completely
4. **Check for errors** - Look at Maya's Script Editor for any error messages
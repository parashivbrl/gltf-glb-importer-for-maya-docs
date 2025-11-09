# Plugin Installation

## Plugin Download

**Download** the `gltf2ImporterForMaya_plugin.zip` from any of the below links:

  - [Gumroad page](https://gumroad.com/)
  - [Artstation Marketplace](https://www.artstation.com/marketplace/game-dev/resources/dev-tools/scripts?section=trending&softwares=maya) 
  - [Flipped Normals Marketplace](https://flippednormals.com/explore?tagIds=1&firstCategory=158&secondCategory=228)

**Extract** the downloaded archive to a temporary location

---

## Installation

### Windows

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Scripts**: Copy the entire `gltf2ImporterForMaya` folder from the extracted archive and paste it into:
   ```
   C:\ProgramData\Autodesk\ApplicationPlugins
   ```
4. **Restart Maya**: Launch Maya again

5. The plugin should be enabled automatically

6. **Open Plugin Manager**: Go to **Windows > Settings/Preferences > Plug-in Manager**

6. Find `gltf2_importer_plugin.py` in the list and notice that both Load and Auto Load checkboxes are enabled

---

### macOS

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Plugin Folder**: Copy the entire `gltf2ImporterForMaya` folder from the extracted archive and paste it into one of the following locations:

   **Option A - User-specific installation (Recommended):**
   ```
   ~/Library/Preferences/Autodesk/ApplicationPlugins
   ```
   > **Note:** The `~` symbol represents your home directory. You can access this folder by opening Finder, pressing `Cmd+Shift+G`, and typing `~/Library/Preferences/Autodesk/ApplicationPlugins`

   **Option B - System-wide installation (Requires admin privileges):**
   ```
   /Library/Application Support/Autodesk/ApplicationPlugins
   ```
   > **Note:** This requires administrator access. You may need to use `sudo` in Terminal to copy files here.

3. **Restart Maya**: Launch Maya again

4. The plugin should be enabled automatically

5. **Open Plugin Manager**: Go to **Windows > Settings/Preferences > Plug-in Manager**

6. Find `gltf2_importer_plugin.py` in the list and notice that both Load and Auto Load checkboxes are enabled

---

### Linux

1. **Close Maya**: Close all instances of Maya if currently running

2. **Copy Plugin Folder**: Copy the entire `gltf2ImporterForMaya` folder from the extracted archive and paste it into one of the following locations:

   **Option A - User-specific installation (Recommended):**
   ```
   ~/maya/ApplicationPlugins
   ```
   > **Note:** The `~` symbol represents your home directory. If the `ApplicationPlugins` directory doesn't exist, create it first:
   > ```bash
   > mkdir -p ~/maya/ApplicationPlugins
   > ```

   **Option B - System-wide installation (Requires root privileges):**
   ```
   /usr/autodesk/ApplicationPlugins
   ```
   > **Note:** This requires root access. You may need to use `sudo` to copy files here:
   > ```bash
   > sudo cp -r gltf2ImporterForMaya /usr/autodesk/ApplicationPlugins/
   > ```

3. **Restart Maya**: Launch Maya again

4. The plugin should be enabled automatically

5. **Open Plugin Manager**: Go to **Windows > Settings/Preferences > Plug-in Manager**

6. Find `gltf2_importer_plugin.py` in the list and notice that both Load and Auto Load checkboxes are enabled

---

## Verification

After installation, you should see the **glTF2.0** menu item in the main maya window and file type **glTF2** available in the Maya's native import window. 

If the plugin doesn't appear:

1. **Check file locations** - Ensure that entire `gltf2ImporterForMaya` folder copied to the correct directory
2. **Verify plugin status** - Make sure the plugin is enabled in the Plug-in Manager. Should be enabled automaticaly when Maya launches
3. **Restart Maya** - Close and reopen Maya completely
4. **Check for errors** - Look at Maya's Script Editor for any error messages
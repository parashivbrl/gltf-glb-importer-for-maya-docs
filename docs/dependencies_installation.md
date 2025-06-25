# Dependencies Installation

This guide will help you install the required dependencies for the glTF/GLB importer plugin to work properly with Maya.

---

## System Requirements

| Requirement | Details |
|-------------|---------|
| **Maya Version** | Maya 2022 or later (Python 3 support required) |
| **Operating System** | Windows, macOS, or Linux |
| **Python** | Python 3.7+ (automatically included with Maya 2022+) |

---

## Required Dependencies

The plugin requires the following Python packages:

- **[pygltflib](https://pypi.org/project/pygltflib/)** - Core library for glTF/GLB file handling
- **[DracoPy](https://pypi.org/project/DracoPy/)** - Required for Draco mesh compression support
- **[numpy](https://pypi.org/project/numpy/)** - Required for Maya 2024 and earlier versions only

> **Note:** Maya 2025+ includes numpy by default, so you only need to install pygltflib and DracoPy.

---

## Installation Instructions

### Before You Start

**Important:** Close all instances of Maya before proceeding with the installation.

---

### Windows Installation

1. **Open Command Prompt as Administrator**
   - Press `Win + X` and select "Command Prompt (Admin)" or "Windows PowerShell (Admin)"

2. **Navigate to Maya's bin directory**
   ```
   cd "C:\Program Files\Autodesk\[Maya Version]\bin"
   ```
   
   **Example for Maya 2024:**
   ```
   cd "C:\Program Files\Autodesk\Maya2024\bin"
   ```

3. **Install pygltflib**
   ```
   mayapy -m pip install pygltflib
   ```

4. **Install DracoPy**
   ```
   mayapy -m pip install DracoPy
   ```

5. **Install numpy (Maya 2024 and earlier only)**
   ```
   mayapy -m pip install numpy
   ```

---

### macOS Installation

1. **Open Terminal**
   - Press `Cmd + Space`, type "Terminal", and press Enter

2. **Navigate to Maya's bin directory**
   ```
   cd "/Applications/Autodesk/[Maya Version]/Maya.app/Contents/bin"
   ```
   
   **Example for Maya 2024:**
   ```
   cd "/Applications/Autodesk/Maya2024/Maya.app/Contents/bin"
   ```

3. **Install pygltflib**
   ```
   ./mayapy -m pip install pygltflib
   ```

4. **Install DracoPy**
   ```
   ./mayapy -m pip install DracoPy
   ```

5. **Install numpy (Maya 2024 and earlier only)**
   ```
   ./mayapy -m pip install numpy
   ```

---

### Linux Installation

1. **Open Terminal**
   - Use your preferred method to open a terminal

2. **Navigate to Maya's bin directory**
   ```
   cd /usr/autodesk/[Maya Version]/bin
   ```
   
   **Example for Maya 2024:**
   ```
   cd /usr/autodesk/maya2024/bin
   ```

3. **Install pygltflib (may require sudo)**
   ```
   sudo ./mayapy -m pip install pygltflib
   ```

4. **Install DracoPy (may require sudo)**
   ```
   sudo ./mayapy -m pip install DracoPy
   ```

5. **Install numpy (Maya 2024 and earlier only)**
   ```
   sudo ./mayapy -m pip install numpy
   ```

---

## Verifying Installation

After installation, you can verify that the dependencies are properly installed:

1. **Open Maya**
2. **Open the Script Editor** (Windows → General Editors → Script Editor)
3. **Run the following Python code** inside the Python tab (Not MEL tab):
   ```python
   try:
       import pygltflib
       print("[SUCCESS] pygltflib successfully imported")
   except ImportError:
       print("[ERROR] pygltflib not found")
   
   try:
       import DracoPy
       print("[SUCCESS] DracoPy successfully imported")
   except ImportError:
       print("[ERROR] DracoPy not found")
   
   try:
       import numpy
       print("[SUCCESS] numpy successfully imported")
   except ImportError:
       print("[ERROR] numpy not found")
   ```
You should see the following three lines in the script editor's output:
```
[SUCCESS] pygltflib successfully imported
[SUCCESS] DracoPy successfully imported
[SUCCESS] numpy successfully imported
```

---


## Troubleshooting

### Common Issues

**Problem:** `mayapy` command not found
- **Solution:** Make sure you're in the correct Maya bin directory and that Maya is properly installed

**Problem:** Permission denied on Linux/macOS
- **Solution:** Try using `sudo` before the command

**Problem:** pip not found
- **Solution:** Maya's pip might need to be installed first:
  ```
  ./mayapy -m ensurepip --upgrade
  ```

### Getting Help

If you encounter issues:

1. Check that you're using the correct Maya version path
2. Ensure Maya is completely closed during installation
3. Try running Maya as administrator (Windows) or with sudo (Linux/macOS)
4. Verify your Maya installation includes Python 3 support

---

**Next Step:** Once dependencies are installed, proceed to [Plugin Installation](plugin_installation.md)
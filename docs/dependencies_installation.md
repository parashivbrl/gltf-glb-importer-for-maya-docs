# Dependencies Installation

This guide will help you install the required dependencies for the glTF/GLB importer plugin to work properly with Maya.

---

## System Requirements

| Requirement | Details |
|-------------|---------|
| **Maya Version** | Maya 2022 or later|
| **Operating System** | Windows, macOS, or Linux |
| **Python** | Python 3.7+ (automatically included with Maya 2022+) |

---

## Required Dependencies

The plugin requires the following Python packages:

- **[numpy](https://pypi.org/project/numpy/)** - Required for Maya 2024 and below

> **Note:** Maya 2025+ includes numpy by default.

---

## Installation Steps

To install numpy for Maya, use the following commands based on your operating system. Replace `<Version>` with your Maya version (e.g., `2024`, `2025`).

### On Windows

(from a command window running as Administrator)

```
"C:\Program Files\Autodesk\Maya<Version>\bin\mayapy.exe" -m pip install numpy
```

### On macOS

```
/Applications/Autodesk/maya<Version>/Maya.app/Contents/bin/mayapy -m pip install numpy
```

### On Linux

```
sudo /usr/autodesk/maya<Version>/bin/mayapy -m pip install numpy
```

---


# Dependencies Installation

This guide will help you install the required dependencies for the glTF/GLB importer plugin to work properly with Maya.

---

## System Requirements

| Requirement | Details |
|-------------|---------|
| **Maya Version** | Maya 2024 or later|
| **Operating System** | Windows, macOS, or Linux |
| **Python** | Python 3.7+ (automatically included with Maya 2022+) |

---

## Required Dependencies

The plugin requires the following Python packages:

- **[numpy](https://pypi.org/project/numpy/)** - Required for Maya 2024

> **Note:** Maya 2025+ includes numpy by default.

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

---

**Next Step:** Once dependencies are installed, proceed to [Plugin Installation](plugin_installation.md)
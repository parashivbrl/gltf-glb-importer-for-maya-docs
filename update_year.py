#!/usr/bin/env python3
"""
Script to automatically update the copyright year in mkdocs.yml
"""
import re
from datetime import datetime

def update_copyright_year():
    """Update the copyright year in mkdocs.yml to the current year"""
    current_year = datetime.now().year
    mkdocs_file = 'mkdocs.yml'
    
    try:
        with open(mkdocs_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the copyright year with current year
        # Pattern matches: copyright: YYYY glTF Importer for Maya
        pattern = r'copyright:\s*\d{4}\s+glTF Importer for Maya'
        replacement = f'copyright: {current_year} glTF Importer for Maya'
        
        updated_content = re.sub(pattern, replacement, content)
        
        if updated_content != content:
            with open(mkdocs_file, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated copyright year to {current_year} in {mkdocs_file}")
        else:
            print(f"Copyright year is already {current_year}")
            
    except FileNotFoundError:
        print(f"Error: {mkdocs_file} not found")
    except Exception as e:
        print(f"Error updating copyright year: {e}")

if __name__ == '__main__':
    update_copyright_year()


import os
from pathlib import Path
import re

def natural_sort_key(s):
    """
    Natural sort key function that correctly handles numbers in strings.
    """
    def try_int(text):
        try:
            return int(text)
        except ValueError:
            return text.lower()
    
    # Split on numbers while keeping delimiters
    return [try_int(c) for c in re.split(r'(\d+)', str(s))]

def create_master_md():
    """Create a master markdown file with diagram and organized links."""
    
    # Get the script's directory as absolute path
    script_dir = str(Path(__file__).parent.resolve())
    
    # Check if SVG exists
    svg_file = Path(script_dir) / 'diagram.svg'
    
    # Prepare content list
    content = ["# Literature Review\n"]
    
    if svg_file.exists():
        content.extend([
            "## Overview Diagram\n",
            f'<img src="{svg_file}" alt="Literature Review Overview" width="800"/>\n'
        ])
    
    content.append("## Contents\n")
    
    # Create a dictionary to store folder structure
    folder_structure = {}
    
    # Walk through the directory and store complete paths
    for root, dirs, files in os.walk(script_dir):
        if '__pycache__' in root:
            continue
            
        level = root.replace(script_dir, '').count(os.sep)
        if level > 0:
            # Store complete path information
            path_parts = os.path.relpath(root, script_dir).split(os.sep)
            
            # Get folder name and full path
            folder_name = os.path.basename(root)
            
            # Store markdown files for this folder
            md_files = []
            for file in files:
                if file.endswith('.md') and file != 'master.md':
                    rel_path = os.path.relpath(
                        os.path.join(root, file), 
                        script_dir
                    )
                    display_name = file[:-3]
                    md_files.append((display_name, rel_path))
            
            # Sort files using natural sort
            md_files.sort(key=lambda x: natural_sort_key(x[0]))
            
            # Store folder info with complete path information
            folder_structure[root] = {
                'name': folder_name,
                'level': level,
                'files': md_files,
                'path_parts': path_parts
            }
    
    # Sort folders by their complete path parts
    def folder_sort_key(path):
        parts = folder_structure[path]['path_parts']
        # Create a key for each part of the path
        return [natural_sort_key(part) for part in parts]
    
    # Sort all paths
    all_paths = sorted(folder_structure.keys(), key=folder_sort_key)
    
    # Debug: Print the sorting order
    print("Folder sorting order:")
    for path in all_paths:
        print(f"  {'  ' * (folder_structure[path]['level']-1)}{folder_structure[path]['name']}")
    
    # Add content with indentation
    for folder_path in all_paths:
        folder_info = folder_structure[folder_path]
        level = folder_info['level']
        
        # Calculate indentation
        indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * (level - 1)
        
        # Add folder name as bold text
        content.append(f"{indent}**{folder_info['name']}**\n")
        
        # Add sorted files with indentation
        file_indent = "&nbsp;&nbsp;&nbsp;&nbsp;" * level
        for display_name, rel_path in folder_info['files']:
            content.append(f"{file_indent}- [{display_name}]({rel_path})")
        
        content.append("")  # Add empty line after each folder
    
    # Write master.md in the same directory as the script
    with open(Path(script_dir) / 'master.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(content))

if __name__ == "__main__":
    create_master_md()
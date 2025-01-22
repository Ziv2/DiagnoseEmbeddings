import re
import os
from pathlib import Path

def convert_md_links(input_file: str, github_base_url: str) -> None:
    """
    Convert markdown links in a file to GitHub URLs and save to a new file.
    
    Args:
        input_file (str): Path to the input markdown file
        github_base_url (str): Base URL of your GitHub repository
    """
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return

    # Read the original content
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create output filename
    input_path = Path(input_file)
    output_file = str(input_path.parent / f"{input_path.stem}_github{input_path.suffix}")
    
    # Find all markdown links
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    matches = re.finditer(pattern, content)
    
    # Replace each link
    new_content = content
    for match in matches:
        original_link = match.group(0)  # The entire link [text](path)
        link_path = match.group(2)      # Just the path part
        
        # Convert local path to GitHub URL
        github_path = link_path.replace('\\', '/').replace(' ', '%20')
        if github_path.startswith('./'):
            github_path = github_path[2:]
        new_link = original_link.replace(link_path, f"{github_base_url}/{github_path}")
        
        # Replace in content
        new_content = new_content.replace(original_link, new_link)
    
    # Save the new file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\nCreated new file: {output_file}")
    print(f"Original file '{input_file}' remains unchanged.")

def main():
    # Get input from user
    
    input_file = input("/home/z/Documents/DK_2025/Literature_Review/master.md").strip()
    github_url = input("https://github.com/Ziv2/EmbeddingDiagnostics.git").strip()
    
    # Remove trailing slash if present
    github_url = github_url.rstrip('/')
    
    # Convert the links
    convert_md_links(input_file, github_url)
    end =1 

if __name__ == "__main__":
    main()
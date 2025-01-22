import re
import os
from pathlib import Path

def convert_md_links(input_file: str, github_url: str) -> None:
    print(f"Starting conversion with:")
    print(f"Input file: {input_file}")
    print(f"GitHub URL: {github_url}")
    
    # Ensure the input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return

    # Read the original content
    print("Reading original file...")
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Create output filename
    input_path = Path(input_file)
    output_file = str(input_path.parent / f"{input_path.stem}_github{input_path.suffix}")
    
    # Convert GitHub URL to raw format
    # Remove .git if present
    github_url = github_url.replace('.git', '')
    # Ensure we have the blob/main or blob/master part
    if 'blob' not in github_url:
        github_url = github_url + '/blob/main'
    
    print(f"Using GitHub URL: {github_url}")
    
    # Find all markdown links
    pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
    matches = list(re.finditer(pattern, content))
    print(f"Found {len(matches)} markdown links")
    
    # Replace each link
    new_content = content
    for match in matches:
        original_link = match.group(0)  # The entire link [text](path)
        link_path = match.group(2)      # Just the path part
        
        # Convert local path to GitHub URL
        github_path = link_path.replace('\\', '/').replace(' ', '%20')
        if github_path.startswith('./'):
            github_path = github_path[2:]
        new_link = original_link.replace(link_path, f"{github_url}/{github_path}")
        
        print(f"Converting: {link_path} -> {github_url}/{github_path}")
        
        # Replace in content
        new_content = new_content.replace(original_link, new_link)
    
    # Save the new file
    print(f"Saving to new file: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"\nSuccess! Created new file: {output_file}")
    print(f"Original file '{input_file}' remains unchanged.")

# Now let's run it directly with your values
if __name__ == "__main__":
    # Use your GitHub URL directly
    GITHUB_URL = "https://github.com/Ziv2/EmbeddingDiagnostics"
    
    # Get just the markdown file path
    # input_file = input("Enter the full path to your markdown file (e.g., /home/user/myfile.md): ").strip()
    input_file = input("/home/z/Documents/DK_2025/Literature_Review/master.md").strip()
    # Convert the links
    convert_md_links(input_file, GITHUB_URL)
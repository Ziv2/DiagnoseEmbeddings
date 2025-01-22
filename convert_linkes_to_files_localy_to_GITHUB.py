import re
import os
from pathlib import Path
from typing import List, Tuple

class MDLinkConverter:
    def __init__(self, base_folder: str, github_base_url: str):
        """
        Initialize the converter with base folder path and GitHub repository URL.
        
        Args:
            base_folder (str): Path to the main folder containing MD files
            github_base_url (str): Base URL of your GitHub repository (e.g., 'https://github.com/username/repo/blob/main')
        """
        self.base_folder = Path(base_folder).resolve()
        self.github_base_url = github_base_url.rstrip('/')
        
    def find_md_links(self, content: str) -> List[Tuple[str, str]]:
        """
        Find all markdown links in the content.
        
        Args:
            content (str): Markdown content
            
        Returns:
            List[Tuple[str, str]]: List of tuples containing (original_link, link_path)
        """
        # Match markdown links: [text](path)
        pattern = r'\[([^\]]+)\]\(([^)]+\.md)\)'
        return [(match.group(0), match.group(2)) for match in re.finditer(pattern, content)]
    
    def convert_link_to_github(self, original_file_path: str, link_path: str) -> str:
        """
        Convert a local markdown link to a GitHub URL.
        
        Args:
            original_file_path (str): Path to the file containing the link
            link_path (str): Path in the markdown link
            
        Returns:
            str: GitHub-compatible URL
        """
        # Get absolute paths
        original_dir = Path(original_file_path).parent
        link_absolute = (original_dir / link_path).resolve()
        
        try:
            # Get relative path from base folder
            relative_path = link_absolute.relative_to(self.base_folder)
            # Convert to forward slashes and encode spaces
            github_path = str(relative_path).replace('\\', '/').replace(' ', '%20')
            return f"{self.github_base_url}/{github_path}"
        except ValueError:
            print(f"Warning: Link path {link_path} is outside the base folder")
            return link_path
    
    def process_file(self, file_path: str, output_path: str = None) -> None:
        """
        Process a markdown file and update its links.
        
        Args:
            file_path (str): Path to the markdown file to process
            output_path (str, optional): Path where to save the processed file. 
                                       If None, will append '_github' to the original filename.
        """
        file_path = Path(file_path)
        if output_path is None:
            output_path = file_path.parent / f"{file_path.stem}_github{file_path.suffix}"
        
        # Read the original file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace all markdown links
        links = self.find_md_links(content)
        for original, link_path in links:
            github_url = self.convert_link_to_github(file_path, link_path)
            new_link = original.replace(link_path, github_url)
            content = content.replace(original, new_link)
        
        # Write the updated content
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Processed {file_path} -> {output_path}")

def main():
    # Example usage
    path_base_folder = "/home/z/Documents/DK_2025/Literature_Review"
    base_folder = input(path_base_folder)
    github_url = input("https://github.com/Ziv2/EmbeddingDiagnostics.git")
    # md_file = input("https://github.com/Ziv2/EmbeddingDiagnostics/blob/master/master.md")
    md_file = input("/home/z/Documents/DK_2025/Literature_Review/master.md")
    converter = MDLinkConverter(base_folder, github_url)
    converter.process_file(md_file)
    end = 1

if __name__ == "__main__":
    main()
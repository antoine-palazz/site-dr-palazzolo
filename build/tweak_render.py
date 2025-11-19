"""
Quarto Configuration Tweaker

Dynamically modifies _quarto.yml to render only changed files or all files.

Usage:
    python build/tweak_render.py

Behavior:
    - If 'diff' file exists: Renders only files listed in diff
    - If 'diff' file doesn't exist: Renders all .qmd files in content/

Output:
    - Modified _quarto.yml with updated render list
"""

import glob
import os
import sys
import warnings
from typing import List

# Suppress urllib3 SSL warnings about LibreSSL
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')

try:
    import yaml
except ImportError:
    print("Error: PyYAML package not installed.", file=sys.stderr)
    print("Install it with: pip install PyYAML", file=sys.stderr)
    sys.exit(1)

# Configuration constants
CONFIG_FILE = "_quarto.yml"
DIFF_FILE = "diff"
CONTENT_DIRS = ["le_docteur", "livres", "publications_communications", "autres_activites"]


def load_config(config_path: str) -> dict:
    """
    Load Quarto configuration from YAML file.
    
    Args:
        config_path: Path to _quarto.yml
        
    Returns:
        dict: Parsed YAML configuration
    """
    if not os.path.exists(config_path):
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    
    with open(config_path, "r", encoding="utf-8") as stream:
        return yaml.safe_load(stream)


def get_files_to_render() -> List[str]:
    """
    Determine which files to render.
    
    Returns:
        list: List of file paths to render
    """
    if os.path.exists(DIFF_FILE):
        # Render only changed files
        print(f"Using {DIFF_FILE} to determine files to render...")
        with open(DIFF_FILE, "r", encoding="utf-8") as f:
            lines = f.read().splitlines()
    else:
        # Render all .qmd files
        print("No diff file found. Rendering all .qmd files...")
        lines = glob.glob("content/**/*.qmd", recursive=True)
    
    # Filter to only .qmd files
    qmd_files = [line for line in lines if line.endswith(".qmd")]
    
    # Add index files for each content directory
    index_files = [
        f"content/{dir}/index.qmd" 
        for dir in CONTENT_DIRS 
        if os.path.exists(f"content/{dir}/index.qmd")
    ]
    
    # Add main index
    all_files = qmd_files + index_files + ["index.qmd"]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_files = []
    for file in all_files:
        if file not in seen:
            seen.add(file)
            unique_files.append(file)
    
    return unique_files


def update_config(config: dict, files: List[str]) -> dict:
    """
    Update configuration with new render list.
    
    Args:
        config: Original configuration dictionary
        files: List of files to render
        
    Returns:
        dict: Updated configuration
    """
    # Update book chapters (if applicable)
    if "book" not in config:
        config["book"] = {}
    config["book"]["chapters"] = files
    
    # Update project render list
    # Exclude slides directory
    render_list = files + ["!content/slides/"]
    config["project"]["render"] = render_list
    
    return config


def save_config(config: dict, config_path: str) -> None:
    """
    Save configuration back to YAML file.
    
    Args:
        config: Configuration dictionary
        config_path: Path to save file
    """
    with open(config_path, "w", encoding="utf-8") as outfile:
        yaml.dump(
            config, 
            outfile, 
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False
        )


def main():
    """Main entry point."""
    try:
        print("=" * 60)
        print("Quarto Configuration Tweaker")
        print("=" * 60)
        
        # Load configuration
        config = load_config(CONFIG_FILE)
        
        # Get files to render
        files = get_files_to_render()
        print(f"Files to render: {len(files)}")
        
        # Update configuration
        config = update_config(config, files)
        
        # Save configuration
        save_config(config, CONFIG_FILE)
        
        print("✅ Configuration updated successfully")
        print(f"Modified: {CONFIG_FILE}")
        
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

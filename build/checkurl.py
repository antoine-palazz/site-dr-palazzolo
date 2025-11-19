"""
URL Checker Script

Scans content files for broken URLs and generates a diagnostic report.

Usage:
    python build/checkurl.py

Output:
    diagnostic.csv - CSV file containing failed URLs
"""

import os
import sys
import warnings
import pandas as pd
from pathlib import Path

# Suppress urllib3 SSL warnings about LibreSSL
warnings.filterwarnings('ignore', message='urllib3 v2 only supports OpenSSL')

try:
    from urlchecker.core.check import UrlChecker
except ImportError:
    print("Error: urlchecker package not installed.", file=sys.stderr)
    print("Install it with: pip install urlchecker", file=sys.stderr)
    sys.exit(1)


def check_urls(content_path: str, file_types: list = None) -> dict:
    """
    Check URLs in content files.
    
    Args:
        content_path: Path to content directory
        file_types: List of file extensions to check
        
    Returns:
        dict: Results from URL checker
    """
    if file_types is None:
        file_types = [".qmd", ".py", ".md"]
    
    if not os.path.exists(content_path):
        print(f"Warning: Content path '{content_path}' does not exist", file=sys.stderr)
        return {"failed": []}
    
    checker = UrlChecker(
        path=content_path,
        file_types=file_types,
        print_all=False
    )
    
    checker.run()
    return checker.results


def save_results(results: dict, output_file: str = "diagnostic.csv") -> None:
    """
    Save failed URLs to CSV file.
    
    Args:
        results: Results dictionary from URL checker
        output_file: Path to output CSV file
    """
    if not results.get("failed"):
        print("✅ No broken URLs found!")
        # Create empty CSV with header
        df = pd.DataFrame(columns=["failed"])
    else:
        print(f"⚠️  Found {len(results['failed'])} broken URL(s)")
        df = pd.DataFrame(results["failed"], columns=["failed"])
    
    df.to_csv(output_file, index=False)
    print(f"Results saved to: {output_file}")


def main():
    """Main entry point."""
    # Get current working directory
    base_path = Path.cwd()
    content_path = base_path / "content"
    
    print(f"Checking URLs in: {content_path}")
    print("-" * 50)
    
    try:
        results = check_urls(str(content_path))
        save_results(results)
    except Exception as e:
        print(f"❌ Error during URL checking: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()

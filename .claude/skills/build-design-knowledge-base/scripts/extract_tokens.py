#!/usr/bin/env python3
"""
Extract CSS tokens from CSS files.

This script analyzes CSS files to extract:
- CSS custom properties (--variables)
- Repeated color values
- Repeated spacing values
- Font family declarations
- Common patterns

Usage:
    python extract_tokens.py <path-to-css> --output tokens.json
"""

import re
import json
from pathlib import Path
from collections import Counter
import argparse


def extract_css_variables(css_content):
    """Extract CSS custom properties."""
    pattern = r'--([a-zA-Z0-9-]+)\s*:\s*([^;]+);'
    matches = re.findall(pattern, css_content)
    return {name: value.strip() for name, value in matches}


def extract_colors(css_content):
    """Extract color values (hex, rgb, rgba)."""
    hex_pattern = r'#[0-9a-fA-F]{3,8}\b'
    rgb_pattern = r'rgba?\([^)]+\)'
    
    hex_colors = re.findall(hex_pattern, css_content)
    rgb_colors = re.findall(rgb_pattern, css_content)
    
    all_colors = hex_colors + rgb_colors
    return Counter(all_colors)


def extract_spacing_values(css_content):
    """Extract spacing values (px, rem, em)."""
    pattern = r'(?:margin|padding|gap|width|height):\s*([0-9.]+(?:px|rem|em))'
    values = re.findall(pattern, css_content)
    return Counter(values)


def extract_font_families(css_content):
    """Extract font family declarations."""
    pattern = r'font-family:\s*([^;]+);'
    families = re.findall(pattern, css_content)
    return [f.strip() for f in families]


def extract_border_radius(css_content):
    """Extract border radius values."""
    pattern = r'border-radius:\s*([^;]+);'
    values = re.findall(pattern, css_content)
    return Counter([v.strip() for v in values])


def extract_shadows(css_content):
    """Extract box-shadow values."""
    pattern = r'box-shadow:\s*([^;]+);'
    shadows = re.findall(pattern, css_content)
    return [s.strip() for s in shadows]


def analyze_css_file(css_path):
    """Analyze a CSS file and extract tokens."""
    with open(css_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    results = {
        'css_variables': extract_css_variables(content),
        'colors': dict(extract_colors(content).most_common(20)),
        'spacing': dict(extract_spacing_values(content).most_common(20)),
        'font_families': list(set(extract_font_families(content))),
        'border_radius': dict(extract_border_radius(content).most_common(10)),
        'shadows': list(set(extract_shadows(content)))[:10]
    }
    
    return results


def main():
    parser = argparse.ArgumentParser(description='Extract design tokens from CSS files')
    parser.add_argument('css_path', help='Path to CSS file or directory')
    parser.add_argument('--output', default='tokens.json', help='Output JSON file')
    
    args = parser.parse_args()
    
    css_path = Path(args.css_path)
    
    if css_path.is_file():
        results = analyze_css_file(css_path)
    elif css_path.is_dir():
        results = {}
        for css_file in css_path.glob('**/*.css'):
            file_results = analyze_css_file(css_file)
            results[str(css_file)] = file_results
    else:
        print(f"Error: {css_path} is not a valid file or directory")
        return
    
    with open(args.output, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2)
    
    print(f"Tokens extracted and saved to {args.output}")


if __name__ == '__main__':
    main()

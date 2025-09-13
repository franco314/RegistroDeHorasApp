#!/usr/bin/env python3
"""
Generate Android launcher icons in WebP format for different screen densities.

This script generates launcher icons in the following sizes:
- mdpi (48x48)
- hdpi (72x72) 
- xhdpi (96x96)
- xxhdpi (144x144)
- xxxhdpi (192x192)

Both ic_launcher.webp and ic_launcher_round.webp are generated for each density.
"""

import os
import sys
from PIL import Image, ImageDraw
import argparse

# Define the density configurations
DENSITIES = {
    'mdpi': 48,
    'hdpi': 72,
    'xhdpi': 96,
    'xxhdpi': 144,
    'xxxhdpi': 192
}

def create_simple_icon(size, is_round=False):
    """Create a simple launcher icon with the app theme."""
    # Create a new image with a transparent background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Define colors for a time tracking app
    primary_color = (33, 150, 243, 255)  # Blue
    accent_color = (255, 193, 7, 255)    # Amber
    
    # Create the background shape
    if is_round:
        # Draw a circular background
        draw.ellipse([2, 2, size-2, size-2], fill=primary_color)
    else:
        # Draw a rounded rectangle background
        margin = size // 16
        draw.rounded_rectangle([margin, margin, size-margin, size-margin], 
                             radius=size//8, fill=primary_color)
    
    # Add a clock symbol in the center
    center = size // 2
    clock_size = size // 3
    
    # Clock face
    draw.ellipse([center - clock_size//2, center - clock_size//2, 
                  center + clock_size//2, center + clock_size//2], 
                 fill=(255, 255, 255, 255))
    
    # Clock hands
    hand_length = clock_size // 3
    # Hour hand (pointing to 3 o'clock)
    draw.line([center, center, center + hand_length//2, center], 
              fill=primary_color, width=max(1, size//24))
    # Minute hand (pointing to 12 o'clock)
    draw.line([center, center, center, center - hand_length], 
              fill=primary_color, width=max(1, size//32))
    
    # Center dot
    dot_size = max(2, size//16)
    draw.ellipse([center - dot_size//2, center - dot_size//2,
                  center + dot_size//2, center + dot_size//2], 
                 fill=accent_color)
    
    return img

def generate_icons_from_source(source_path, output_dir):
    """Generate icons from a source image file."""
    try:
        source_img = Image.open(source_path).convert('RGBA')
        print(f"Using source image: {source_path}")
    except Exception as e:
        print(f"Error opening source image: {e}")
        return False
    
    for density, size in DENSITIES.items():
        mipmap_dir = os.path.join(output_dir, f'mipmap-{density}')
        os.makedirs(mipmap_dir, exist_ok=True)
        
        # Generate regular launcher icon
        regular_icon = source_img.resize((size, size), Image.Resampling.LANCZOS)
        regular_path = os.path.join(mipmap_dir, 'ic_launcher.webp')
        regular_icon.save(regular_path, 'WEBP', quality=90)
        print(f"Generated: {regular_path} ({size}x{size})")
        
        # Generate round launcher icon (crop to circle)
        round_icon = source_img.resize((size, size), Image.Resampling.LANCZOS)
        
        # Create a circular mask
        mask = Image.new('L', (size, size), 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse([0, 0, size, size], fill=255)
        
        # Apply the mask to make it circular
        round_icon.putalpha(mask)
        
        round_path = os.path.join(mipmap_dir, 'ic_launcher_round.webp')
        round_icon.save(round_path, 'WEBP', quality=90)
        print(f"Generated: {round_path} ({size}x{size})")
    
    return True

def generate_default_icons(output_dir):
    """Generate default icons when no source image is provided."""
    print("No source image provided. Generating default icons...")
    
    for density, size in DENSITIES.items():
        mipmap_dir = os.path.join(output_dir, f'mipmap-{density}')
        os.makedirs(mipmap_dir, exist_ok=True)
        
        # Generate regular launcher icon
        regular_icon = create_simple_icon(size, is_round=False)
        regular_path = os.path.join(mipmap_dir, 'ic_launcher.webp')
        regular_icon.save(regular_path, 'WEBP', quality=90)
        print(f"Generated: {regular_path} ({size}x{size})")
        
        # Generate round launcher icon
        round_icon = create_simple_icon(size, is_round=True)
        round_path = os.path.join(mipmap_dir, 'ic_launcher_round.webp')
        round_icon.save(round_path, 'WEBP', quality=90)
        print(f"Generated: {round_path} ({size}x{size})")

def main():
    parser = argparse.ArgumentParser(description='Generate Android launcher icons in WebP format')
    parser.add_argument('--source', '-s', help='Source image file (PNG, JPG, etc.)')
    parser.add_argument('--output', '-o', default='./res', help='Output directory (default: ./res)')
    
    args = parser.parse_args()
    
    print("Android Launcher Icon Generator")
    print("=" * 40)
    print(f"Output directory: {args.output}")
    
    if args.source and os.path.exists(args.source):
        success = generate_icons_from_source(args.source, args.output)
        if not success:
            print("Falling back to default icons...")
            generate_default_icons(args.output)
    else:
        if args.source:
            print(f"Source image not found: {args.source}")
        generate_default_icons(args.output)
    
    print("\nIcon generation complete!")
    print("\nGenerated icon sizes:")
    for density, size in DENSITIES.items():
        print(f"  {density:8}: {size}x{size} pixels")

if __name__ == '__main__':
    main()
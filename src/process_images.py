#!/usr/bin/env python3
import os
import subprocess
from pathlib import Path

# Directories
RAW_DIR = Path('assets/01raw')
CLEANED_DIR = Path('assets/02cleaned')
RESIZED_DIR = Path('assets/03resized')

# Ensure that the directories exist
CLEANED_DIR.mkdir(parents=True, exist_ok=True)
RESIZED_DIR.mkdir(parents=True, exist_ok=True)

def process_image(input_image: str):
    """
    Process an image by removing the watermark and then resizing it.
    """
    # Define file paths
    filename = os.path.basename(input_image)
    cleaned_image = CLEANED_DIR / f"{os.path.splitext(filename)[0]}_cleaned.png"
    resized_image = RESIZED_DIR / f"{os.path.splitext(filename)[0]}_resized.png"

    # Check if the image already exists in cleaned and resized directories
    if cleaned_image.exists():
        print(f"Skipping {filename}: already cleaned.")
    else:
        # Run watermark_removal.py to clean the image
        print(f"Processing watermark removal for {filename}...")
        subprocess.run([
            'python3', 'src/watermark_removal.py', 
            '--input', input_image, 
            '--output', str(cleaned_image)
        ])
        print(f"Watermark removed and saved to {cleaned_image}")

    if resized_image.exists():
        print(f"Skipping {filename}: already resized.")
    else:
        # Run resize_wallpaper.py to resize the cleaned image
        print(f"Resizing {filename}...")
        subprocess.run([
            'python3', 'src/resize_wallpaper.py', 
            '--input', str(cleaned_image), 
            '--output', str(resized_image)
        ])
        print(f"Resized image saved to {resized_image}")

def main():
    """
    Main function to process all images in the RAW directory.
    """
    # Process each image in the RAW directory
    for img in RAW_DIR.glob('*.*'):
        print(f"Starting processing for {img.name}...")
        process_image(str(img))

if __name__ == "__main__":
    main()

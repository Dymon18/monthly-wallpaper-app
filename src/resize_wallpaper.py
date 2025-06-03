#!/usr/bin/env python3
import argparse
from PIL import Image, ImageColor

"""
resize_wallpaper.py

Resizes the input image to fit the bottom two-thirds of a target wallpaper size and pads the top third with a specified background color.
Adjust target width, height, and background color using CLI flags.

Usage:
  python resize_wallpaper.py --input in.png --output out.png \
      --width 1080 --height 1920 [--bg "#ff5733"]

Dependencies:
  pillow
"""


def process_image(img: Image.Image, target_w: int, target_h: int, bg_color: str) -> Image.Image:
    """
    Resize the given image to cover the bottom two-thirds of a canvas of size (target_w x target_h),
    pad the top third with bg_color, and return the composed Image.
    """
    # Parse background color to RGB tuple
    bg_rgb = ImageColor.getrgb(bg_color)

    # Compute two-thirds height
    two_thirds_h = int(target_h * 2 / 3)

    # Determine resize dimensions while preserving aspect ratio
    img_ratio = img.width / img.height
    region_ratio = target_w / two_thirds_h
    if img_ratio > region_ratio:
        # Image is wider than region; fit width
        new_w = target_w
        new_h = round(target_w / img_ratio)
    else:
        # Image is taller or narrower; fit height
        new_h = two_thirds_h
        new_w = round(two_thirds_h * img_ratio)

    # Perform resizing
    resized = img.resize((new_w, new_h), Image.LANCZOS)

    # Create canvas and paste resized image
    canvas = Image.new("RGB", (target_w, target_h), bg_rgb)
    paste_x = (target_w - new_w) // 2
    paste_y = target_h // 3
    canvas.paste(resized, (paste_x, paste_y))

    return canvas


def main():
    parser = argparse.ArgumentParser(
        description="Resize image to bottom two-thirds of phone wallpaper and pad top third"
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to input image file"
    )
    parser.add_argument(
        "--width", "-W", type=int, required=True,
        help="Target wallpaper width in pixels"
    )
    parser.add_argument(
        "--height", "-H", type=int, required=True,
        help="Target wallpaper height in pixels"
    )
    parser.add_argument(
        "--bg", "-b", default="#000000",
        help="Background color (hex or name) for the top third"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="Path to save the output image"
    )
    args = parser.parse_args()

    # Open source image
    try:
        img = Image.open(args.input)
    except Exception as e:
        print(f"Error opening input image: {e}")
        return

    # Process image
    result = process_image(img, args.width, args.height, args.bg)

    # Save result
    try:
        result.save(args.output)
        print(f"Saved wallpaper to {args.output}")
    except Exception as e:
        print(f"Error saving output image: {e}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import os
from PIL import Image, ImageColor


"""
resize_wallpaper.py

This script resizes the input image to fit the bottom two-thirds of a target wallpaper size
and pads the top third with a specified background color.

Usage Examples:
  python3 src/resize_wallpaper.py --input assets/01raw/your_image.jpg
  python3 src/resize_wallpaper.py --input assets/01raw/your_image.jpg --output assets/03resized/custom_output.jpg
  python3 src/resize_wallpaper.py --input assets/01raw/your_image.jpg --output assets/03resized/custom_output.jpg --width 1080 --height 1920
  python3 src/resize_wallpaper.py --input assets/01raw/your_image.jpg --output assets/03resized/custom_output.jpg --width 1080 --height 1920 --bg "#FFFFFF"

Dependencies:
  pillow
"""


def resize_image(img: Image.Image, target_w: int, target_h: int) -> Image.Image:
    """
    Resize the image to fit within the bottom two-thirds of the target dimensions, 
    preserving the aspect ratio.
    """
    two_thirds_h = int(target_h * 2 / 3)
    
    img_ratio = img.width / img.height
    region_ratio = target_w / two_thirds_h

    if img_ratio > region_ratio:
        new_w = target_w
        new_h = round(target_w / img_ratio)
    else:
        new_h = two_thirds_h
        new_w = round(two_thirds_h * img_ratio)

    resized_img = img.resize((new_w, new_h), Image.LANCZOS)
    
    return resized_img


def create_canvas(target_w: int, target_h: int, bg_color: str, resized_img: Image.Image) -> Image.Image:
    """
    Create a canvas with the specified background color, paste the resized image on it,
    and return the final image.
    """
    bg_rgb = ImageColor.getrgb(bg_color)
    canvas = Image.new("RGB", (target_w, target_h), bg_rgb)

    paste_x = (target_w - resized_img.width) // 2
    paste_y = target_h // 3
    canvas.paste(resized_img, (paste_x, paste_y))

    return canvas


def process_image(input_img: str, target_w: int, target_h: int, bg_color: str, output_path: str):
    """
    Main image processing function that resizes the image, adds a background, and saves the result.
    """
    try:
        img = Image.open(input_img)
    except Exception as e:
        print(f"Error opening input image: {e}")
        return

    resized_img = resize_image(img, target_w, target_h)
    final_img = create_canvas(target_w, target_h, bg_color, resized_img)

    try:
        final_img.save(output_path)
        print(f"Saved wallpaper to {output_path}")
    except Exception as e:
        print(f"Error saving output image: {e}")


def get_default_output_path(input_img: str) -> str:
    """
    Generate the default output file path using the input image filename,
    saving the result in the 'assets/03resized/' folder.
    """
    input_filename = os.path.splitext(os.path.basename(input_img))[0]  # Get filename without extension
    return f"assets/03resized/{input_filename}_resized.png"


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments and return the parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Resize an image to fit the bottom two-thirds of a phone wallpaper and pad top third with background color."
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to input image file"
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="Path to save the output image (default: 'assets/03resized/[input_filename]_resized.png')"
    )
    parser.add_argument(
        "--width", "-W", type=int, default=1080,
        help="Target wallpaper width in pixels (default: 1080)"
    )
    parser.add_argument(
        "--height", "-H", type=int, default=1920,
        help="Target wallpaper height in pixels (default: 1920)"
    )
    parser.add_argument(
        "--bg", "-b", default="#FFFFFF",
        help="Background color (hex or name) for the top third (default: white)"
    )

    return parser.parse_args()


def main():
    """
    Main entry point for the script. Parses arguments and processes the image accordingly.
    """
    args = parse_arguments()

    if args.output is None:
        args.output = get_default_output_path(args.input)

    process_image(args.input, args.width, args.height, args.bg, args.output)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import os
from PIL import Image, ImageDraw

"""
watermark_removal.py

Allows covering a watermark by drawing a fixed-size rectangle overlay at a specified position.
Adjust the constants for the rectangle's position and size at the top of the script, or fine-tune using CLI flags.

Usage:
  python watermark_removal.py --input assets/01raw/your_image.jpg
  python watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.png
  python watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.png --box_x 150 --box_y 500 --box_w 300 --box_h 80
  python watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.png --box_x 150 --box_y 500 --box_w 300 --box_h 80 --fill_color "255,0,0"
  python watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.png --box_x 100 --box_y 400 --box_w 250 --box_h 60
  python watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/final_output.png --box_x 200 --box_y 600 --box_w 300 --box_h 100 --fill_color "0,255,0"
  python watermark_removal.py --help



Dependencies:
  pillow
"""

# Rectangle parameters (adjust as needed)
BOX_X = 207        # X coordinate (left) of rectangle's top-left corner
BOX_Y = 607        # Y coordinate (top) of rectangle's top-left corner
BOX_WIDTH = 230    # Width of rectangle
BOX_HEIGHT = 32    # Height of rectangle
DEBUG_FILL_COLOR = (255, 255, 255)  # White for final output (use (128,128,128) for debugging)

def cover_watermark(pil_img: Image.Image,
                    box_x: int = BOX_X,
                    box_y: int = BOX_Y,
                    box_w: int = BOX_WIDTH,
                    box_h: int = BOX_HEIGHT,
                    fill_color: tuple = DEBUG_FILL_COLOR) -> Image.Image:
    """
    Cover a fixed region of the image with a solid rectangle.

    Args:
      pil_img: The input PIL image.
      box_x: X coordinate of the rectangle's top-left corner.
      box_y: Y coordinate of the rectangle's top-left corner.
      box_w: Width of the rectangle.
      box_h: Height of the rectangle.
      fill_color: RGB tuple for the rectangle's color.

    Returns:
      A new PIL Image with the rectangle overlay.
    """
    img = pil_img.copy()
    draw = ImageDraw.Draw(img)
    x0, y0 = box_x, box_y
    x1, y1 = box_x + box_w, box_y + box_h
    draw.rectangle([(x0, y0), (x1, y1)], fill=fill_color)
    return img


def process_image(input_img: str, output_img: str, fill_color: tuple):
    """
    Process the image by covering the watermark region with a rectangle.

    Args:
      input_img: Path to the input image file.
      output_img: Path where the output image will be saved.
      fill_color: RGB tuple for the rectangle's fill color.
    """
    try:
        pil_img = Image.open(input_img).convert("RGB")
    except Exception as e:
        print(f"Error opening input image: {e}")
        return

    # Cover watermark region
    cleaned = cover_watermark(pil_img, fill_color=fill_color)

    # Save result
    try:
        cleaned.save(output_img)
        print(f"Saved cleaned image to {output_img}. Adjust parameters at the top of the script to fine-tune.")
    except Exception as e:
        print(f"Error saving output image: {e}")


def parse_arguments() -> argparse.Namespace:
    """
    Parse command-line arguments and return the parsed arguments.
    """
    parser = argparse.ArgumentParser(description="Remove watermark by covering it with a rectangle.")
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to input image file"
    )
    parser.add_argument(
        "--output", "-o", default=None,
        help="Path to save the output image (default: 'assets/02cleaned/[input_filename]_cleaned.png')"
    )
    parser.add_argument(
        "--fill_color", type=str, default=None,
        help="Optional fill color as R,G,B (e.g. 255,255,255) to override debug color"
    )
    
    return parser.parse_args()


def get_default_output_path(input_img: str) -> str:
    """
    Generate the default output file path using the input image filename,
    saving the result in the 'assets/02cleaned/' folder.
    """
    input_filename = os.path.splitext(os.path.basename(input_img))[0]  # Get filename without extension
    return f"assets/02cleaned/{input_filename}_cleaned.png"


def main():
    """
    Main entry point for the script. Parses arguments and processes the image accordingly.
    """
    args = parse_arguments()

    # Generate default output path if not provided
    if args.output is None:
        args.output = get_default_output_path(args.input)

    # Determine fill color
    if args.fill_color:
        try:
            fc = tuple(int(c) for c in args.fill_color.split(","))
            if len(fc) != 3:
                raise ValueError
        except Exception:
            print("Error: --fill_color must be in format R,G,B (e.g. 255,255,255)")
            return
    else:
        fc = DEBUG_FILL_COLOR

    process_image(args.input, args.output, fc)


if __name__ == "__main__":
    main()

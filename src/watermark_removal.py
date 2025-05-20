#!/usr/bin/env python3
"""
watermark_removal.py

Allows covering a watermark by drawing a fixed-size rectangle overlay at a specified position.
Adjust BOX_X, BOX_Y, BOX_WIDTH, and BOX_HEIGHT constants or use CLI flags to fine-tune.
Start with DEBUG_FILL_COLOR=(128,128,128) to visualize, then switch to (255,255,255) for white.

Usage:
  python watermark_removal.py --input in.png --output out.png \
      [--box_x 100] [--box_y 500] [--box_w 300] [--box_h 80] [--fill_color 255,255,255]

Dependencies:
  pillow
"""
import argparse
from PIL import Image, ImageDraw

# Default box parameters (pixels)
BOX_X = 207        # X coordinate (left) of rectangle's top-left corner
BOX_Y = 607        # Y coordinate (top) of rectangle's top-left corner
BOX_WIDTH = 230   # Width of rectangle
BOX_HEIGHT = 32   # Height of rectangle
DEBUG_FILL_COLOR = (255, 255, 255)  # Gray for debugging; set to (255,255,255) for final white


def cover_watermark(pil_img: Image.Image,
                    box_x: int = BOX_X,
                    box_y: int = BOX_Y,
                    box_w: int = BOX_WIDTH,
                    box_h: int = BOX_HEIGHT,
                    fill_color: tuple = DEBUG_FILL_COLOR) -> Image.Image:
    """
    Draw a solid rectangle over a fixed region of the image.

    Args:
      pil_img: Input PIL Image.
      box_x: X coord of top-left corner.
      box_y: Y coord of top-left corner.
      box_w: Width of rectangle.
      box_h: Height of rectangle.
      fill_color: RGB tuple for rectangle color overlay.

    Returns:
      A new PIL Image with the rectangle overlay applied.
    """
    img = pil_img.copy()
    draw = ImageDraw.Draw(img)
    x0, y0 = box_x, box_y
    x1, y1 = box_x + box_w, box_y + box_h
    draw.rectangle([(x0, y0), (x1, y1)], fill=fill_color)
    return img


def main():
    parser = argparse.ArgumentParser(
        description="Cover watermark area with a fixed rectangle overlay"
    )
    parser.add_argument(
        "--input", "-i", required=True,
        help="Path to input image (PNG/JPG)"
    )
    parser.add_argument(
        "--output", "-o", required=True,
        help="Path to save output image"
    )
    parser.add_argument(
        "--box_x", type=int, default=BOX_X,
        help=f"X coord of rectangle top-left (default {BOX_X})"
    )
    parser.add_argument(
        "--box_y", type=int, default=BOX_Y,
        help=f"Y coord of rectangle top-left (default {BOX_Y})"
    )
    parser.add_argument(
        "--box_w", type=int, default=BOX_WIDTH,
        help=f"Rectangle width (default {BOX_WIDTH})"
    )
    parser.add_argument(
        "--box_h", type=int, default=BOX_HEIGHT,
        help=f"Rectangle height (default {BOX_HEIGHT})"
    )
    parser.add_argument(
        "--fill_color", type=str, default=None,
        help="Optional fill color as R,G,B (e.g. 255,255,255) to override debug color"
    )
    args = parser.parse_args()

    # Load image
    pil_img = Image.open(args.input).convert("RGB")

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

    # Cover watermark region
    cleaned = cover_watermark(
        pil_img,
        box_x=args.box_x,
        box_y=args.box_y,
        box_w=args.box_w,
        box_h=args.box_h,
        fill_color=fc
    )

    # Save result
    cleaned.save(args.output)
    print(
        f"Saved cleaned image to {args.output}. "
        "Adjust BOX_X, BOX_Y, BOX_WIDTH, BOX_HEIGHT at top or via flags to fine-tune."
    )


if __name__ == "__main__":
    main()

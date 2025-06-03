> **Author:** Dymon18
> **Date Started:** 2025-05-17
> **Last Edited:** 2025-06-03
> **Access Repo:**
> git clone https://github.com/Dymon18/monthly-wallpaper-app.git
(https://github.com/Dymon18/monthly-wallpaper-app.git)

---
## Usage
1. Activate virtual environment with:
> source venv/bin/activate
2. Deactivate with
> deactivate

watermark_removal.py
Usage Examples:
> python3 src/watermark_removal.py --input assets/01raw/your_image.jpg  
> python3 src/watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.jpg
> python3 src/watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.jpg --box_x 100 --box_y 500 --box_w 300 --box_h 80  
> python3 src/watermark_removal.py --input assets/01raw/your_image.jpg --output assets/02cleaned/custom_output.jpg --box_x 100 --box_y 500 --box_w 300 --box_h 80 --fill_color "255,0,0"

resize_wallpaper.py
> python3 src/resize_wallpaper.py --input assets/02cleaned/your_image.jpg  
> python3 src/resize_wallpaper.py --input assets/02cleaned/your_image.jpg --output assets/03resized/custom_output.jpg  
> python3 src/resize_wallpaper.py --input assets/02cleaned/your_image.jpg --output assets/03resized/custom_output.jpg --width 1080 --height 1920  
> python3 src/resize_wallpaper.py --input assets/02cleaned/your_image.jpg --output assets/03resized/custom_output.jpg --width 1080 --height 1920 --bg "#FFFFFF"

---

## Project Overview

The Monthly Wallpaper Application automatically retrieves or accepts user-uploaded images, then resizes and pads them to fit mobile lock screens. The main image is positioned over the bottom two-thirds of the wallpaper to avoid lock-screen widgets, while the top third is filled with a chosen background color. Users can upload a file or fetch an image from a website, select resolution and color, and download a ready-to-use wallpaper.

## Key Features (MVP)

* **Image Processing:** Resize input image to cover bottom two-thirds and pad the top third with a chosen background color.
* **Input Sources:** User file upload or web-based sourcing (search and fetch from specified websites).
* **Streamlit UI:** Simple web interface for source selection, file upload or query input, resolution and color selection, and one-click download.
* **CLI Support:** Command-line interface for scripting, batch processing, or cron scheduling.

## Architecture & Tech Stack

* **Backend:** Python 3.x with Pillow & Streamlit
* **Image Sourcing Module:** `requests` & `BeautifulSoup` (or `playwright`) for web scraping and download
* **Frontend:** Streamlit app (built-in UI)
* **Database:** None (stateless image processing)
* **Other tools:** Git & GitHub for version control; macOS cron for scheduling;

  * **Testing:** pytest

## Development Roadmap

1. Prototype CLI script (`resize_wallpaper.py`)
2. Build Streamlit UI (`app.py`)
3. Add resolution presets & color picker widget
4. Implement web-sourcing module (`src/image_source.py`)
5. Deploy on Streamlit Cloud
6. (Future) Integrate Unsplash API for automatic image sourcing

## Testing & QA

* **How to run tests:** `pytest tests/`
* **Testing strategy:** Unit tests for core image resizing, padding, and sourcing logic; integration tests for the Streamlit UI upload/query and download flow

## Folder Structure (Proposed)

```
/src
├─ resize_wallpaper.py
├─ image_source.py      # handles upload or web fetch
├─ app.py
├─ assets/
├─ tests/
└─ README.md
```

## END OF README

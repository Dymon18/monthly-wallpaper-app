> **Author:** Dymon18
> **Date Started:** 2025-05-17
> **Last Edited:** 2025-05-17
> **Access Repo:**
git clone https://github.com/Dymon18/monthly-wallpaper-app.git
---

## Project Overview

The Monthly Wallpaper Application automatically resizes and pads images to fit mobile lock screens, positioning the main image at the bottom two-thirds of the wallpaper to avoid lock-screen widgets. Users upload an image, choose the target resolution and background color, and download a ready-to-use wallpaper.

## Key Features (MVP)

* **Image Processing:** Resize input image to cover bottom two-thirds and pad the top third with a chosen background color.
* **Streamlit UI:** Simple web interface for file upload, resolution and color selection, and one-click download.
* **CLI Support:** Command-line interface for batch processing or scheduling via cron.

## Architecture & Tech Stack

* **Backend:** Python 3.x with Pillow & Streamlit
* **Frontend:** Streamlit app (built-in UI)
* **Database:** None (stateless image processing)
* **Other tools:** Git & GitHub for version control; macOS cron for scheduling

## Development Roadmap

1. Prototype CLI script (`resize_wallpaper.py`)
2. Build Streamlit UI (`app.py`)
3. Add resolution presets & color picker widget
4. Deploy on Streamlit Cloud
5. (Future) Integrate Unsplash API for automatic image sourcing

## Testing & QA

* **How to run tests:** `pytest tests/`
* **Testing strategy:** Unit tests for core image resizing and padding logic; integration tests for the Streamlit UI upload/download flow

## Folder Structure (Proposed)

```
/src
├─ resize_wallpaper.py
├─ app.py
├─ assets/
├─ tests/
└─ README.md
```

## END OF README

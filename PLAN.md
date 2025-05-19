### 1. Define Your MVP

Core features:

* **Image Upload:** Single image input via CLI or Streamlit UI.
* **Web Sourcing:** Fetch an image from a specified website via search and link extraction.
* **Image Processing:** Resize to bottom two-thirds of canvas; pad top one-third with selected background color.
* **Download/Save:** Output a processed wallpaper file for immediate use.

The MVP delivers end-to-end functionality without external dependencies beyond Python and required libraries.

### 2. High-Level Architecture

1. **Streamlit UI (`app.py`):** Handles source selection (upload vs. web), file upload or query input, resolution and color inputs, and triggers processing. Presents download link.
2. **Image Sourcing Module (`image_source.py`):** Implements `from_upload()` and `from_web()` functions using Pillow and web-scraping (`requests` + BeautifulSoup or `playwright`) to return a PIL Image.
3. **Processing Module (`resize_wallpaper.py`):** Core logic using Pillow to resize, pad, and save images.
4. **CLI Wrapper:** Exposes sourcing and processing logic via command-line arguments for scripting and scheduling.
5. **Scheduler (cron):** Optional macOS cron job for monthly automation.

### 3. Technology Choices & Rationale

* **Backend:** Python + Pillow & Streamlit

  * *Why:* Rapid prototyping, mature image library, built-in UI widgets, free hosting on Streamlit Cloud.
* **Web Sourcing:** `requests` + `BeautifulSoup` (for static sites) or `playwright` (for JS-driven pages)

  * *Why:* Flexible scraping; easy to add more sources later.
* **Frontend:** Streamlit

  * *Why:* Minimal boilerplate for web UI, integrated file-handling and widgets.
* **Database:** None

  * *Why:* Stateless processing; no persistent storage needed.
* **Other Tools:**

  * **GitHub:** Version control, collaboration, issue tracking.
  * **cron:** Native scheduling on macOS.
  * **pytest:** Testing framework for unit/integration tests.

### 4. Feature Roadmap & Sprints

* **Sprint 1 (1-2 sessions):**

  * Implement `resize_wallpaper.py` with CLI for upload-based processing.
  * Write unit tests for resizing and padding logic.
* **Sprint 2 (1-2 sessions):**

  * Develop `app.py` with Streamlit UI for file upload, resolution and color selection.
  * Integration tests for upload flow.
* **Sprint 3 (1-2 sessions):**

  * Add `image_source.py` module with `from_web()` implementation.
  * Extend CLI and UI to support web sourcing.
  * Write tests for web sourcing logic.
* **Sprint 4 (1-2 sessions):**

  * Deploy to Streamlit Cloud.
  * Create scheduling guide and example cron entry.
  * Finalize documentation (README, PLAN).

### 5. Testing & QA

* **Test Cases:**

  * Standard images (various aspect ratios).
  * Edge cases: extremely tall/narrow images; unsupported file types.
  * Web source: valid queries, no-results scenarios, network errors.
* **QA Tools:** `pytest` for unit and integration tests; manual checks on physical devices and in UI.
* **Strategy:** Unit tests for core functions and sourcing; integration tests via automated scripts; user acceptance testing through manual UI trials.

### 6. Scaling & Future App

* **Scaling Considerations:**

  * Add caching or parallel processing for batch jobs.
  * Containerize application with Docker for consistent deployment.
* **Future Enhancements:**

  * Automatic image sourcing via Unsplash API or other endpoints.
  * Resolution presets for multiple device profiles.
  * Mobile app wrapper (React Native) or browser extension.

### 7. Next Steps

* Update GitHub repo with new module structure.
* Install and configure `playwright` (if needed) or finalize scraping dependencies.
* Implement and test `image_source.py`.
* Extend CLI and UI to include source option and query input.

## END OF PLAN

### 1. Define Your MVP

Core features:

* **Image Upload:** Single image input via CLI or Streamlit UI.
* **Image Processing:** Resize to bottom two-thirds of canvas; pad top one-third with selected background color.
* **Download/Save:** Output a processed wallpaper file for immediate use.

The MVP delivers end-to-end functionality without external dependencies beyond Python and required libraries.

### 2. High-Level Architecture

1. **Streamlit UI (`app.py`):** Handles file upload, resolution and color inputs, and triggers processing function. Presents download link.
2. **Processing Module (`resize_wallpaper.py`):** Core logic using Pillow to resize, pad, and save images.
3. **CLI Wrapper:** Exposes the same processing logic via command-line arguments for scripting and scheduling.
4. **Scheduler (cron):** Optional macOS cron job calling the CLI for monthly automation.

### 3. Technology Choices & Rationale

* **Backend:** Python + Pillow & Streamlit

  * *Why:* Rapid prototyping, mature image library, built-in UI widgets, free hosting on Streamlit Cloud.
* **Frontend:** Streamlit

  * *Why:* Minimal boilerplate for web UI, integrated file-handling and widgets.
* **Database:** None

  * *Why:* Stateless processing; no persistent data storage needed initially.
* **Other Tools:**

  * **GitHub:** Version control, collaboration, issue tracking.
  * **cron:** Native scheduling on macOS for monthly runs.
  * **pytest:** Testing framework for unit/integration tests.

### 4. Feature Roadmap & Sprints

* **Sprint 1 (1 week):**

  * Implement `resize_wallpaper.py` with CLI.
  * Write unit tests for resizing and padding logic.
* **Sprint 2 (1 week):**

  * Develop `app.py` with Streamlit UI (upload, inputs, download).
  * Integration tests for end-to-end flow.
* **Sprint 3 (1 week):**

  * Deploy to Streamlit Cloud.
  * Create scheduling guide and example cron entry.
  * Finalize README and documentation.

### 5. Testing & QA

* **Test Cases:**

  * Standard images (various aspect ratios).
  * Edge cases: extremely tall/narrow images; unsupported file types.
* **QA Tools:** `pytest` for unit and integration tests; manual checks on physical devices.
* **Strategy:** Unit tests for core functions; integration tests via automated script; UAT through manual UI trials.

### 6. Scaling & Future App

* **Scaling Considerations:**

  * Add caching or parallel processing for batch jobs.
  * Dockerize application for consistent deployment.
* **Future Enhancements:**

  * Automatic image sourcing via Unsplash API or predefined folder.
  * Mobile app wrapper (React Native) or browser extension.
  * Resolution presets for multiple device profiles.

### 7. Next Steps

* Initialize GitHub repository and push folder structure.
* Create virtual environment and `requirements.txt`.
* Start coding `resize_wallpaper.py`.
* Draft initial Streamlit scaffold in `app.py`.

## END OF PLAN

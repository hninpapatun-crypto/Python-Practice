# \# Python Practice Projects

# 

# A collection of command-line Python scripts built to practice modular programming, file system management, error handling, and third-party library integration.

# 

# \## Featured Script: `yt\_downloader.py`

# 

# A command-line media utility built with Python and `yt-dlp` that downloads single YouTube videos, extracts MP3 audio, or saves both formats locally.

# 

# \### Key Concepts Practiced

# \- \*\*Modular Function Design:\*\* Separated download progress tracking (`progress\_hook`) and media configuration (`download\_youtube`) from user input handling.

# \- \*\*File System Management:\*\* Used Python's `pathlib.Path` to automatically create output directories and format file paths cleanly across operating systems.

# \- \*\*External Tool \& Post-Processor Integration:\*\* Configured `yt-dlp` with `FFmpeg` for MP4 stream merging and MP3 audio extraction, alongside `Deno` as a JavaScript runtime.

# \- \*\*Input Validation \& Exception Handling:\*\* Implemented fallback defaults for user prompts and handled `yt\_dlp.utils.DownloadError` exceptions gracefully.

# 

# \### Requirements

# \- \*\*Python 3.10+\*\*

# \- \*\*`yt-dlp`\*\* (`pip install yt-dlp`)

# \- \*\*`FFmpeg`\*\* (for merging video/audio streams and converting audio to MP3)

# \- \*\*`Deno`\*\* (JavaScript runtime used by `yt-dlp` for extraction)

# 

# \### How to Run

# 1\. Install the required dependencies:

# &#x20;  ```bash

# &#x20;  pip install yt-dlp


from pathlib import Path
import yt_dlp


def progress_hook(d: dict) -> None:
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "").strip()
        speed = d.get("_speed_str", "").strip()
        eta = d.get("_eta_str", "").strip()
        print(f"\rDownloading: {percent} | Speed: {speed} | ETA: {eta}", end="", flush=True)
    elif d["status"] == "finished":
        print("\nDownload complete. Running post-processing (if needed)...")


def download_youtube(
    url: str,
    mode: str = "video",
    max_height: int = 1080,
    output_dir: str = "downloads",
) -> None:
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    base_opts = {
        "outtmpl": str(out_path / "%(title)s.%(ext)s"),
        "noplaylist": True,
        "progress_hooks": [progress_hook],
    }

    if mode == "audio":
        ydl_opts = {
            **base_opts,
            "format": "bestaudio/best",
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "192",
                }
            ],
        }
    else:
        ydl_opts = {
            **base_opts,
            "format": f"bestvideo[height<={max_height}]+bestaudio/best[height<={max_height}]/best",
            "merge_output_format": "mp4",
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            print(f"Saved: {info.get('title', 'video')}")
    except yt_dlp.utils.DownloadError as exc:
        print(f"\nDownload failed: {exc}")


if __name__ == "__main__":
    video_url = input("Enter YouTube URL: ").strip()
    choice = (
        input("Choose mode ('video', 'audio', or 'both'): ").strip().lower()
        or "video"
    )

    if choice == "audio":
        download_youtube(video_url, mode="audio")
    elif choice == "both":
        res_input = input("Max height for video (e.g., 720, 1080, 1440) [1080]: ").strip()
        max_h = int(res_input) if res_input.isdigit() else 1080
        download_youtube(video_url, mode="video", max_height=max_h)
        download_youtube(video_url, mode="audio")
    else:
        res_input = input("Max height (e.g., 720, 1080, 1440) [1080]: ").strip()
        max_h = int(res_input) if res_input.isdigit() else 1080
        download_youtube(video_url, mode="video", max_height=max_h)

import os
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#Download the video
def download_video():
    print("\nStep 1: Open the Teams recorded meeting video in SharePoint.")
    print("Press Ctrl+Shift+C on the video page, go to Networking, type 'videomanifest' in the filter box, and press F5.")
    video_url = input("Paste the extracted video URL here: ").strip()
    if not video_url:
        print("No URL provided. Exiting.")
        return None
    
    output_filename = input("Enter output filename (without extension, default: 'downloaded_video'): ") or "downloaded_video"
    output_filename += ".mp4"
    
    ffmpeg_cmd = ["ffmpeg", "-i", video_url, "-codec", "copy", output_filename]
    print("\nDownloading video...")
    subprocess.run(ffmpeg_cmd)
    print(f"\nVideo saved as: {output_filename}")
    return output_filename

#Trim the video
def trim_video(input_video):
    start_time = int(input("Enter start time (in seconds) for trimming: "))
    end_time = int(input("Enter end time (in seconds) for trimming: "))
    output_trimmed = input("Enter output trimmed filename (default: 'trimmed_video.mp4'): ") or "trimmed_video.mp4"
    
    print("\nTrimming video...")
    ffmpeg_extract_subclip(input_video, start_time, end_time, targetname=output_trimmed)
    print(f"Trimmed video saved as: {output_trimmed}")

def main():
    video_file = download_video()
    if video_file:
        trim_video(video_file)
    print("\nProcess completed!")

if __name__ == "__main__":
    main()

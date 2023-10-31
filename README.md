# Download and Converter Youtube Videos

This Python application allows users to choose between downloading a YouTube video and translated or just download the audio. It presents a simple graphical interface created using the Tkinter library.

## Prerequisites
- Python 3.x installed on your system
- Install Tkinter.
- Install yt_dlp.
- Install whisper with pytorch=2.0.1.
- Install ffmpeg.

## How to Use
1. **Enter the youtube link into the first entry box.**

    - It is possible to interact with short and long YouTube videos.

2. **Select the desired option:**

    - The first one allows you to download the video.

    - The second is responsible for downloading the video and then generating the `.srt` file **(Transcription)**.

    - The last one simply downloads the audio file of that video.

3. **Click the Submit button.**

    - Once the process is finished, the window will disappear.

## Notes:

- This readme talk about `Youtube.py`.

- It is necessary to consider that it is possible to translate the downloaded video thanks to the `Local.py` script.

- The result will appear on the user's desktop within the **YTDownloader** folder.

---
# Convert and Translate Local Video

This Python application allows users to choose between converting local videos to audio or translating them.

## Prerequisites
- Python 3.x installed on your system
- Install Tkinter.
- Install whisper with pytorch=2.0.1.
- Install ffmpeg.

## How to Use
1. **Select your desired file to translate:**
```
This is the list of input extension files:
        - m4a.
        - mp3.
        - webm.
        - mp4.
        - mpga.
        - wav.
        - mpeg.
``` 
2. **Select the desired option:**

    - The first one translates the detected audio or video language file to a `.mp3` output.

    - The last one just download the audio.

## Notes:

- This readme talk about `Local.py`.

- The result will appear on the user's desktop within the **4to3** folder.

---

# Multioption App

**There is also a script that runs a window that allows you to choose between both applications.**

from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip, concatenate_videoclips
from gtts import gTTS
import os

def generate_video(script, style):
    lines = script.strip().split(".")
    clips = []

    for i, line in enumerate(lines):
        line = line.strip()
        if not line:
            continue

        tts = gTTS(text=line, lang='en')
        audio_path = f"audio_{i}.mp3"
        tts.save(audio_path)

        audioclip = AudioFileClip(audio_path)
        textclip = TextClip(line, fontsize=48, color='white', size=(720, 1280))
        textclip = textclip.set_duration(audioclip.duration).set_position("center")

        video = textclip.set_audio(audioclip)
        clips.append(video)

    final = concatenate_videoclips(clips, method="compose")
    output_path = "final_video.mp4"
    final.write_videofile(output_path, fps=24)
    return output_path

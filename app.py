import gtts
import playsound

gtts.gTTS("Happy New Year. I look forward to working with you again this year.", lang="en").save("en.mp3")
gtts.gTTS("あけましておめでとうございます。今年もよろしくお願いします。", lang="ja").save("ja.mp3")

while True:
    playsound.playsound("en.mp3")
    playsound.playsound("ja.mp3")


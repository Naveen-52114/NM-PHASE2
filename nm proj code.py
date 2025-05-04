from nrclex import NRCLex

text = "I am excited and hopeful about the future!"
emotion = NRCLex(text)

print(emotion.raw_emotion_scores)
print(emotion.top_emotions)

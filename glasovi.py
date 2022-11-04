import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

c = 0
for i in voices:
    print(f'{c}. {i}\n')
    c += 1
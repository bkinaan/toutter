import whisper

print("loading model...")
model = whisper.load_model("base")
print("done loading model")

while True:
    text = input("Waiting for press...")
    result = model.transcribe("sagar.mp3")
    print(result["text"])
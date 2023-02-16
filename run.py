import whisper
from chatgpt_wrapper import ChatGPT

def stt():
    print("loading model...")
    model = whisper.load_model("base")
    print("done loading model")

    result = model.transcribe("sagar.mp3")
    print("transcribed")
    # print(result["text"])
    return result["text"]
        
def chat(text):
    bot = ChatGPT()
    print("calling chatGPT")
    response = bot.ask(text)
    print(response)  # prints the response from chatGPT
    
text = stt();
chat(text)
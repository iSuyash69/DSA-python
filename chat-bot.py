from datetime import datetime
import random 

def greetings():
    responses=["Hello!","Hi there!","Hey!","Hola!"]
    return random.choice(responses)

def farewell():
    responses=["Goodbye!","See you later!","Have a great day!","Bye!"]
    return random.choice(responses)

def respond(message):
    if any(word in message.lower() for word in ["hello","hey","hi"]):
        return greetings()
    elif "how are you?" in message.lower():
        return "I'm just a chatbot, but I'm doing well"
    elif "what is your name?" in message.lower():
        return "My name is Alexa - The Chatbot"
    elif "what is the current time?" in message.lower():
        currentTime=datetime.now().time()
        return str(currentTime)
    elif "what day is today?" in message.lower():
        currentTime=datetime.now().date()
        return str(currentTime)
    else:
        return "I'm sorry, I didn't understand that."

def main():
    print("Chatbot: "+ greetings())
    while True:
        userInput=input("You: ")
        if any(word in userInput.lower() for word in ["bye","see you","tata"]):
            print("Chatbot: "+farewell())
            exit()
        else:
            print("Chatbot: "+respond(userInput))

main()
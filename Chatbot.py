from datetime import datetime

print("=== Rule Based ChatBot ===")
print("Type 'bye' to exit.")

while True:

    user = input("You: ").lower()

    
    if "hello" in user or "hi" in user or "hey" in user:
        print("Bot: Hello! How can I help you?")

    
    elif "how are you" in user:
        print("Bot: I am doing well. Thanks for asking!")

    
    elif "your name" in user or "who are you" in user or "what is your name" in user or "name" in user:
        print("Bot: My name is Shera.")

    
    elif "who created you" in user or "who made you" in user:
        print("Bot: I was created using Python.")

    
    elif "time" in user:
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Bot: Current time is {current_time}")

    
    elif "date" in user or "today" in user:
        current_date = datetime.now().strftime("%d-%m-%Y")
        print(f"Bot: Today's date is {current_date}")

    
    elif "thank" in user:
        print("Bot: You're welcome!")

    
    elif "good morning" in user:
        print("Bot: Good morning!")

    
    elif "good afternoon" in user:
        print("Bot: Good afternoon!")

    
    elif "good evening" in user:
        print("Bot: Good evening!")

    
    elif "help" in user or "what can you do" in user:
        print("Bot: I can answer questions about time, date, greetings and basic information.")

   
    elif "bye" in user or "exit" in user or "quit" in user:
        print("Bot: Goodbye!")
        break

    
    else:
        print("Bot: Sorry, I don't understand that question.")
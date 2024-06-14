def chatbot():
    print("Welcome to the chatbot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "hello":
            print("Chatbot: Hello There!")
        elif user_input.lower() == "how are you":
            print("Chatbot: I'm doing well, thanks for asking!")
        elif user_input.lower() == "what's your name":
            print("Chatbot: I'm just a chatbot, but you can call me 'Chatbot'!")
        elif user_input.lower() == "how can you help me":
            print("Chatbot: i can answer any question and i will provide information about that")
        elif user_input.lower() == "quit":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you please rephrase?")

chatbot()

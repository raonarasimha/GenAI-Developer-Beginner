class ChatBot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello! I am {self.name}. How can I help you today?")

    def __str__(self):
        return f"ChatBot(name='{self.name}')"

if __name__ == "__main__":
    bot = ChatBot("GenAI Helper")
    print(bot)
    bot.greet()

    try:
        user_input = input("Ask me anything: ")
        if not user_input.strip():
            raise ValueError("Input cannot be empty!")
        print(f"You said: {user_input}")
    except ValueError as ve:
        print(f"Error: {ve}") 
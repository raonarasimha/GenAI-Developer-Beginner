class GenAIChatBot:
    def ask(self, prompt):
        return f"[Mocked OpenAI reply to: '{prompt}']"

if __name__ == "__main__":
    bot = GenAIChatBot()
    print("Welcome to the CLI GenAI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        print("Bot:", bot.ask(user_input)) 
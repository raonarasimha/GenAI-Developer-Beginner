class GenAIChatBot:
    def __init__(self, name="GenAI"):
        self.name = name

    def ask(self, prompt):
        # Mocked OpenAI response for demo
        return f"[Mocked OpenAI reply to: '{prompt}']"

if __name__ == "__main__":
    bot = GenAIChatBot()
    user_prompt = input("Enter your prompt: ")
    print("Bot reply:", bot.ask(user_prompt)) 
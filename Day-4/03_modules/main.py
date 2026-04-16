from bot import GenAIChatBot

if __name__ == "__main__":
    bot = GenAIChatBot()
    prompt = input("Enter your prompt: ")
    print("Bot reply:", bot.ask(prompt))

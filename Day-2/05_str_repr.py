class Bot:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My bot's name is {self.name}"

    def __repr__(self):
        return f"Bot(name='{self.name}')"

if __name__ == "__main__":
    bot = Bot("GenAI")
    print(str(bot))      # User-friendly
    print(repr(bot))     # Debug-friendly 
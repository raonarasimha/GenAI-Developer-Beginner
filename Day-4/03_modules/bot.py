class GenAIChatBot:
    def __init__(self, name="GenAI"):
        self.name = name

    def ask(self, prompt):
        return f"[Mocked OpenAI reply to: '{prompt}']"

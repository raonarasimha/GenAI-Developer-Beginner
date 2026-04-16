class Tokenizer:
    def tokenize(self, text):
        return text.split()

class AIEngine:
    def __init__(self, model):
        self.model = model
        self.tokenizer = Tokenizer()

    def process(self, text):
        tokens = self.tokenizer.tokenize(text)
        print(f"Processing with model '{self.model}': {tokens}")

# --- Inheritance Example ---

# Base class
class Model:
    def __init__(self, name):
        self.name = name

    def predict(self, x):
        print(f"Base model '{self.name}' predicting on {x}")

    def describe(self):
        print(f"This is a model named '{self.name}'.")

# Derived class
class AdvancedModel(Model):
    def predict(self, x):
        print(f"Advanced model '{self.name}' making advanced prediction on {x}")

    def show_description(self):
        # Accessing base class method
        self.describe()

if __name__ == "__main__":
    # Composition usage
    engine = AIEngine("gpt-3.5")
    engine.process("Hello world from GenAI!")

    # Inheritance usage
    base = Model("base-model")
    base.predict([1, 2, 3])

    adv = AdvancedModel("advanced-model")
    adv.predict([4, 5, 6])
    adv.show_description()
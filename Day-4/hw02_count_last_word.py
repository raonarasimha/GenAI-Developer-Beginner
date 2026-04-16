if __name__ == "__main__":
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("No input provided.")
    else:
        last_word = sentence.split()[-1]
        print(f"Last word: '{last_word}' has {len(last_word)} characters.") 
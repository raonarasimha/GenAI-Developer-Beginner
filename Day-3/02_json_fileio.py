import json

if __name__ == "__main__":
    data = {"name": "Bob", "score": 95, "passed": True}
    # Write JSON to file
    with open("sample.json", "w") as f:
        json.dump(data, f)
    print("Wrote data to sample.json")

    # Read JSON from file
    with open("sample.json", "r") as f:
        loaded = json.load(f)
    print("Loaded from file:", loaded)

    # Write plain text
    with open("sample.txt", "w") as f:
        f.write("Hello, file!\n")
    print("Wrote to sample.txt")

    # Read plain text
    with open("sample.txt", "r") as f:
        text = f.read()
    print("Read from sample.txt:", text) 
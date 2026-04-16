import requests

if __name__ == "__main__":
    # Example: GET request to a public API (mocked for safety)
    url = "https://api.github.com/"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("GitHub API root:", response.json())
        else:
            print(f"Request failed with status {response.status_code}")
    except Exception as e:
        print("Error making API call:", e) 
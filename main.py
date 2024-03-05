from yt_url import is_valid_youtube_url

# you can try this as well
# from another_folder.yt_url import is_valid_youtube_url

VALID_URL = "https://youtube.com/v?test"
INVALID_URL = "https://google.com/v?test"
INVALID_URL_2 = "random string"

if __name__ == "__main__":
    print(f"Is {VALID_URL} a valid youtube url?")
    print(f"{is_valid_youtube_url(VALID_URL)}\n")

    print(f"Is {INVALID_URL} a valid youtube url?")
    print(f"{is_valid_youtube_url(INVALID_URL)}\n")

    print(f"Is {INVALID_URL_2} a valid youtube url?")
    print(f"{is_valid_youtube_url(INVALID_URL_2)}\n")

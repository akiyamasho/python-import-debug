import re

regex = r"^(http(s)?:\/\/)?((w){3}.)?youtu(be|.be)?(\.com)?\/.+"


def is_valid_youtube_url(url: str):
    url = url.strip()

    if not re.match(regex, url):
        return False

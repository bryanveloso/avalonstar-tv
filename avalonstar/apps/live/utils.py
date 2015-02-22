# -*- coding: utf-8 -*-
import re
import requests


def fetch_stream():
    endpoint = 'https://api.twitch.tv/kraken/streams/avalonstar'
    return requests.get(endpoint).json()


def fetch_status():
    try:
        response = fetch_stream()
        return response['stream']['channel']['status']
    except TypeError:
        return ''


def is_episodic():
    # Let's use the stream's title to determine if a stream is "casual"
    # or not. The current way we determine this is as follows:
    #
    #   - "A☆###": A numbered episode.
    #   - (Anything else.): A casual episode.
    #
    # Because Python is weird, it doesn't detect the white star, so we're not
    # going to bother looking for it.
    pattern = r'^A.\d{3}'
    status = fetch_status()
    return bool(re.match(pattern, status, re.UNICODE))

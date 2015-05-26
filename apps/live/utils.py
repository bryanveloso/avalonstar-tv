# -*- coding: utf-8 -*-
import re
import requests


def fetch_stream():
    endpoint = 'https://api.twitch.tv/kraken/streams/avalonstar'
    json = requests.get(endpoint).json()
    return json.get('stream', {})


def fetch_status():
    try:
        response = fetch_stream()
        return response.get('channel', {}).get('status', '')
    except (AttributeError, TypeError) as e:
        return ''


def is_episodic():
    # Let's use the stream's title to determine if a stream is an episode
    # or not. We use the stream's status to determine this as follows:
    #
    #   - "A☆###": A numbered episode.
    #   - (Anything else.): A casual episode.
    #
    # Because Python is weird, it doesn't detect the white star. We're not
    # going to bother looking for it.
    pattern = r'^A.\d{3}'
    status = fetch_status()
    return bool(re.match(pattern, status, re.UNICODE))


def is_live():
    return bool(fetch_stream())

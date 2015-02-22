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
        return None


def is_episodic():
    pattern = ur'^A\u2606\d{3}'
    regex = re.compile(pattern, re.UNICODE)

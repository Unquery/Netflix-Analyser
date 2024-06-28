import re


def extract_series_name(title):
    return re.sub(r'\:.*|\(.*\)', '', title).strip()


def extract_episode(title):
    return re.sub(r'^.*Season \d+: ', '', title).strip()
#!/usr/bin/env python

import sys
import re
from subprocess import check_output
import random
import requests

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']


def text_to_owo(text):
    """ Converts your text to OwO """
    positive_smileys = ['^w^', 'OuO', 'ÔwÔ']
    neutral_smileys = ['UwU', 'owo', '=w=', 'OwO', 'OwO\'']
    negative_smileys = ['TwT', ';w;', '>w<', '(・`ω\´・)', '*w*']

    sentences = []

    url = "https://sentim-api.herokuapp.com/api/v1/"
    headers = {"Accept": "application/json",
               "Content-Type": "application/json"}
    payload = {'text': text}

    try:
        resp = requests.post(url, headers=headers, json=payload)
        data = resp.json()

        for s in data['sentences']:
            sentences.append(
                {"text": s['sentence'], "sentiment": s['sentiment']['type']})
            sentiment.append(s['sentiment']['type'])
    except:
        sentences = re.split('(?<=[.!?]) +', text)
        sentences = [{"text": s, "sentiment": random.choice(
            ['positive', 'negative', 'neutral'])} for s in sentences]

    for s in sentences:
        s['text'] = s['text'].replace('L', 'W').replace('l', 'w')
        s['text'] = s['text'].replace('R', 'W').replace('r', 'w')

        for v in s['text']:
            if f'n{v}' in s['text']:
                s['text'] = s['text'].replace(f'n{v}', f'ny{v}')
            if f'N{v}' in s['text']:
                s['text'] = s['text'].replace(f'N{v}', 'N{}{}'.format(
                    'Y' if v.isupper() else 'y', v))

        if s["sentiment"] == "positive":
            s['text'] += f" {random.choice(positive_smileys)} "
        if s["sentiment"] == "neutral":
            s['text'] += f" {random.choice(neutral_smileys)} "
        if s["sentiment"] == "negative":
            s['text'] += f" {random.choice(negative_smileys)} "

    return "".join([s['text'] for s in sentences])


commit_msg_filepath = sys.argv[1]

with open(commit_msg_filepath, 'r+', encoding="utf-8") as fh:
    commit_msg = fh.read()

    fh.truncate(0)
    fh.seek(0, 0)
    fh.write(text_to_owo(commit_msg))

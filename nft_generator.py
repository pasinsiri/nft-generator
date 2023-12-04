import numpy as np
import math
import random
import json
import os

N_OBJECT = 10
TARGET_DIR = 'res/vanya'

def gen_json(n: int):
    res = {}
    res['name'] = 'Vanya #{' + '.02d'.format(n + 1)
    res['description'] = 'A cool heroine with unpredictable power'

    attrs = {}
    # keys = ['number', 'emotion', 'power']
    emotion_values = ['ecstatic', 'confident', 'serene', 'worried', 'tense', 'astonished', 'hopeful', 'indifferent', 'elated', 'overwhelmed']
    assert len(emotion_values) == N_OBJECT, f'emotion_values legnth must be {n}'

    power_values = ['superhuman strength', 'mind control', 'teleportation', 'invulnerability', 'telekinesis']
    attrs['number'] = n + 1
    attrs['emotion'] = emotion_values[n]
    attrs['power'] = np.random.choice(power_values)

    res['attributes'] = attrs

    with open(os.path.join(TARGET_DIR, str(n + 1) + '.json'), 'w') as f:
        json.dump(res, f)

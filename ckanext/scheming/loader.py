"""
Load either yaml or json, based on the name of the resource
"""

import json

def load(f):
    if is_yaml(f.name):
        import yaml
        return yaml.load(f)
    return json.load(f)

def loads(s, url):
    if is_yaml(url):
        import yaml
        return yaml.load(s)
    return json.loads(s)

def is_yaml(n):
    n = n.lower()
    return n.endswith('.yaml') or n.endswith('.yml')

def make_request(keys, values):
    if len(keys) != len(values):
        return {}
    else:
        return dict(zip(keys, values))

def typeBasedTransformer(**kwargs):
    transform = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transform[key] = value ** 2
        elif isinstance(value, str):
            transform[key] = value[::-1]
        elif isinstance(value, bool):
            transform[key] = not value
        elif isinstance(value, (list, tuple)):
            transform[key] = value[::-1]
        elif isinstance(value, dict):
            transform[key] = {v: k for k, v in value.items()}
        else:
            transform[key] = value

    return transform
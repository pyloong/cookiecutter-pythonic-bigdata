"""Singleton pattern decorator"""
_instance = {}


def singleton(cls):
    # Create a dictionary to hold the instance objects of the decorated class _instance = {}
    def _singleton(*args, **kwargs):
        # If there is no new object created, the previously created one is returned.
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return _singleton

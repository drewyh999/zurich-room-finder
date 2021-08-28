from config import VERBOSE_MODE

def print_info(*args, **kwargs):
    if not VERBOSE_MODE:
        return
    print(*args, **kwargs)
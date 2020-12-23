import functools

def login_required(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return itcast(*args, **kwargs)
    return wrapper

@login_required
def itcast():
    """itcast python"""
    pass

print(itcast.__name__)
print(itcast.__doc__)
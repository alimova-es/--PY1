import string
from random import sample


def get_random_password(n=8) -> str:
    full_str = string.ascii_lowercase + string.ascii_uppercase + string.digits
    random_password = ''.join(sample(full_str, n))
    return random_password


print(get_random_password())

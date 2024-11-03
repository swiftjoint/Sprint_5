import random
import string


def generate_random_name(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_email(domain="ya.ru", length=10):
    letters = string.ascii_lowercase
    random_name = ''.join(random.choice(letters) for _ in range(length))
    return f"{random_name}@{domain}"


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

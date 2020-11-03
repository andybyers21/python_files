import random
import string


def password(len, chars=string.ascii_letters + string.digits + string.punctuation):
    """ Generate a random password string with user defined amount of characters. """
    return "".join(random.choice(chars) for _ in range(len))


print(password(int(input('How many characters in your password? '))))

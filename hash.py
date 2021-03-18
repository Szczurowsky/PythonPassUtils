import random
import string


class Hash:
    def __init__(self, hash_type, length):
        self.hash_type = hash_type
        self.length = length

    def __call__(self):
        hash_types = [string.ascii_letters, string.ascii_letters + string.digits,
                      string.ascii_letters + string.digits + string.punctuation]
        generated_string = ''.join(random.choice(hash_types[self.hash_type]) for i in range(self.length))
        return generated_string

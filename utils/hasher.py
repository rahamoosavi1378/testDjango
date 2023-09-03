from django.utils.text import slugify
from faker import Faker
import hashlib


class MD5:
    txt = ''

    def __init__(self, txt):
        self.txt = txt

    def md5(self):
        self.txt = hashlib.md5(self.txt.encode()).hexdigest()
        return MD5(self.txt)

    def __str__(self):
        return str(self.txt)


# print(MD5('http://google.com').md5()) # test


class GenSlug:
    def __init__(self):
        self.name = Faker().name()

    def GenSlug(self):
        return slugify(self.name)

    def __str__(self):
        return self.GenSlug()

# print(GenSlug()) # test

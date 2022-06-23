from ast import Return
from random import random
from django.utils.text import slugify

import random
import string



def random_str(n):
    res=''.join(random.choices(string.ascii_uppercase + string.digits,k=n))
    return res

def generate_slug(text):
    new_slug=slugify(text)
    from . import models
    if models.blogmodel.objects.filter(slug=new_slug).exists():
      return generate_slug(text + random_str(5))
    return new_slug    
from urllib.parse import urlencode

import hashlib
from django import template

register = template.Library()


@register.filter
def gravatar(user_email):
    email = user_email.lower().encode('utf-8')
    default = 'robohash'
    size = 256
    url = 'https://www.gravatar.com/avatar/{md5}?{params}'.format(
        md5=hashlib.md5(email).hexdigest(),
        params=urlencode({'d': default, 's': str(size)})
    )
    return url
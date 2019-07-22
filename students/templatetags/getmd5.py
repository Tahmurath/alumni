import re
from django import template
from django.conf import settings
import hashlib

numeric_test = re.compile("^\d+$")
register = template.Library()


def getmd5(value, arg):
    str1 = str(value)
    str12 = str(arg)
    str3 = str1 + 'test' + str12
    return hashlib.md5(str3.encode('utf-8')).hexdigest()


register.filter('getmd5', getmd5)



#{{ user.first_name|getmd5:user.id }}
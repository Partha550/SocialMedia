import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "social.settings")
django.setup()

from django.conf import settings
#  settings.configure()
from django.contrib.auth import get_user_model

User = get_user_model()
import csv

with open("mockdata.csv") as f:
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if i <= 1:
            continue
        first_name = row[0]
        last_name = row[1]
        email = row[2]
        username = row[3]
        password = row[4]
        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()

from datetime import datetime

from django.db import models


class Timer(models.Model):
    timer = models.DateTimeField(default=datetime.now, blank=True)

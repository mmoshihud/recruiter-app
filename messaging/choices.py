from django.db import models


class KindChoices(models.TextChoices):
    PARENT = "PARENT", "Parent"
    CHILD = "CHILD", "Child"

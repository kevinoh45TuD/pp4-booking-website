from django.db import models
from django.contrib.auth.models import User

DAYS = (
    (1, "Monday"),
    (2, "Tuesday"),
    (3, "Wednesday"),
    (4, "Thursday"),
    (5, "Friday"),
    (6, "Saturday"),
    (7, "Friday")
)

TABLE = ((1, "1"),(2, "2"),(3, "3"),(4, "4"),(5, "5"))

# Create your models here.
class Booking(models.Model):
    which_day = models.IntegerField(choices=DAYS)
    which_table = models.IntegerField(choices=TABLE)
    which_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="curr_book")

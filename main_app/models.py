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

MOVIES = (
    (1, "The Good, The Bad and the Ugly"),
    (2, "Planet of the Apes"),
    (3, "Enter the Dragon"),
    (4, "Escape from Alcatraz"),
    (5, "The Godfather"),
    (6, "Night of the Living Dead"),
    (7, "Monty Python and the Holy Grail")
)

AVAIL = ((0, "Booked"), (1, "Available"))

# Create your models here.
class Booking(models.Model):
    which_day = models.IntegerField(choices=DAYS)
    which_table = models.IntegerField(choices=TABLE)
    which_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="curr_book")

class Movies(models.Model):
    pick_day = models.IntegerField(choices=DAYS)
    table_one = models.IntegerField(choices=AVAIL)
    table_two = models.IntegerField(choices=AVAIL)
    table_three = models.IntegerField(choices=AVAIL)
    table_four = models.IntegerField(choices=AVAIL)
    table_five = models.IntegerField(choices=AVAIL)
    which_movie = models.IntegerField(choices=MOVIES)
    which_year = models.IntegerField()
    which_cuisine = models.CharField()

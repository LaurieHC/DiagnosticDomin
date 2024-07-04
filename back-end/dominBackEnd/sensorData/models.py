from django.db import models
from django.utils.translation import gettext_lazy as _

class Direction(models.TextChoices):
    LEFT = "Left", _("Left")
    RIGHT = "Right", _("Right")
    FORWARD = "Forward", _("Forward")
    BACKWARD = "Backward", _("Backward")

class Event(models.TextChoices):
    REGULAR = "Regular", _("Regular")
    IMPACT = "Impact", _("Impact")
    SPEED_BUMP = "Speed bump", _("Speed bump")
    SPINOUT = "Spinout", _("Spinout")
    POTHOLE = "Pot hole", _("Pot hole")

# Create your models here.
class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    vehicle_speed = models.FloatField()
    vehicle_direction = models.CharField(
        "Direction",
        max_length=50,
        choices=Direction.choices,
        default=Direction.FORWARD,
    )
    events = models.CharField(
        "Event",
        max_length=50,
        choices=Event.choices,
        default=Event.REGULAR,
    )
    vehicle_acceleration = models.FloatField()
    

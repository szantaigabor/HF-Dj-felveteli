from django.db import models

# Create your models here.

class SajatUser(models.Model):
    """Model definition for SajatUser."""

    # TODO: Define fields here

    #user = models.OneToOneField(User)

    azonosito=models.CharField(max_length=11)

    class Meta:
        """Meta definition for SajatUser."""

        verbose_name = 'SajatUser'
        verbose_name_plural = 'SajatUsers'

    def __str__(self):
        return self.azonosito
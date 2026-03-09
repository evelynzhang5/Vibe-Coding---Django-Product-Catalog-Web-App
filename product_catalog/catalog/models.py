from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError


class Item(models.Model):
    name = models.CharField(
        max_length=100
    )

    expiry_date = models.DateField()

    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    serial_number = models.CharField(
        max_length=50,
        unique=True
    )

    notes = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def clean(self):
        """
        Custom validation for the model
        """
        if self.expiry_date < timezone.now().date():
            raise ValidationError("Expiry date cannot be in the past.")

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

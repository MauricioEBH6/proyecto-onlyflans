from django.db import models
import uuid


# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug_field = models.SlugField()
    is_private = models.BooleanField()
    precio = models.DecimalField(decimal_places=0, max_digits=10)

    def __str__(self):
        return f"{self.name} - ({self.flan_uuid}) - EsPrivado? = [{self.is_private}]"

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
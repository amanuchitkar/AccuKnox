# Question 3: By default, do Django signals run in the same database transaction as the caller?
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received inside transaction:", transaction.get_autocommit())

# Triggering the signal within a transaction
with transaction.atomic():
    instance = MyModel.objects.create(name="Test")
    print("Instance saved inside transaction:", transaction.get_autocommit())


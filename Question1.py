# Question 1: By default, are Django signals executed synchronously or asynchronously?
import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print("Signal received.")
    time.sleep(5)  
    # Simulating long processing
    print("Signal processing finished.")

# Triggering the signal by saving an instance
instance = MyModel.objects.create(name="Test")
print("Instance saved.")


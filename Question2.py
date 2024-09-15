# Question 2: Do Django signals run in the same thread as the caller?
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from myapp.models import MyModel

@receiver(post_save, sender=MyModel)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal handler running in thread: {threading.current_thread().name}")

# Triggering the signal by saving an instance
instance = MyModel.objects.create(name="Test")
print(f"Instance saved in thread: {threading.current_thread().name}")

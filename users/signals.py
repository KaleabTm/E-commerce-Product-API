# users/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from carts.models import Cart
from django.contrib.auth import get_user_model  # Import this

User = get_user_model()  # Get the actual user model

@receiver(post_save, sender=User)  # Use User model directly here
def create_user_cart(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(user=instance)

from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model): 
    '''
    Wishlist model, for users to keep track of their favourite items for later purchase
    '''
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE,
                                     null=False, blank=False,
                                     related_name='user_wishlist',
                                     default=None)
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.product.name

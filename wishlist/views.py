from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from products.models import Product
from .models import Wishlist
from profiles.models import UserProfile


@login_required
def wishlist(request):
    '''
    A view to render a wishlist
    '''

    user_profile = UserProfile.objects.get(user=request.user)
    user_wishlist = Wishlist.objects.filter(user_profile=user_profile)

    return render(
        request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist})


def add_to_wishlist(request, product_id):
    '''
    A View to add/remove item from the wishlist
    '''

    product = get_object_or_404(Product, pk=product_id)

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        if Wishlist.objects.filter(user_profile=user_profile,product=product).exists():
            Wishlist.objects.get(user_profile=user_profile,product=product).delete()
            messages.success(
                request, f'{product.name} has been removed from your Wishlist.')
        else:
            wishlist_item = Wishlist.objects.create(
                user_profile=user_profile, product=product)
            messages.success(
                request,
                f'{wishlist_item.product.name} added to Wishlist successfully!'
            )
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
    else:
        messages.error(request, 'You need to log in to add item to your Wishlist')
        return HttpResponseRedirect(request.META["HTTP_REFERER"])
        
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse

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
        request, 'wishlist/wishlist.html', {'user_wishlist': user_wishlist}
    )



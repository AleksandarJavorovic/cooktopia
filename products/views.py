from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Case, When, Value, IntegerField
from django.db.models.functions import Lower
from .models import Product, Category, ReviewRating

from .forms import ProductForm, ReviewRatingForm

from checkout.models import Order, OrderLineItem
from profiles.models import UserProfile
from wishlist.models import Wishlist
from django.contrib.auth.models import User, AnonymousUser

from django.contrib.auth import get_user_model

import uuid

User = get_user_model()


def all_products(request):
    """
    A view to render all of the products, sorting and search queries
    """

    products = Product.objects.annotate(
        avg_rating=Avg("reviews__rating"),
        rating_order=Case(
            When(avg_rating=None, then=Value(0)),
            default="avg_rating",
            output_field=IntegerField(),
        ),
    ).all()
    query = None
    categories = None
    sort = None
    direction = None
    product_in_wishlist = False

    if request.GET:

        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            elif sortkey == "rating":
                sortkey = "rating_order"

        if "direction" in request.GET:
            direction = request.GET["direction"]
            if direction == "desc":
                sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!"
                )
                return redirect(reverse("products"))

            queries = (
                Q(name__icontains=query)
                | Q(description__icontains=query)
                | Q(brand__icontains=query)
                | Q(material__icontains=query)
                | Q(country_of_origin__icontains=query)
                | Q(category__name__icontains=query)
            )
            products = products.filter(queries)

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)

    return render(request, "products/product_detail.html", context)


def product_detail(request, product_id):
    """
    A view to render product details and handle review submission
    """

    product = get_object_or_404(
        Product.objects.annotate(
            avg_rating=Avg("reviews__rating")),
        pk=product_id
    )
    reviews = ReviewRating.objects.filter(product_id=product_id).all()
    already_commented = False
    all_items = []
    already_bought = False
    product_in_wishlist = False

    # logic for displaying wishlist button
    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        user_wishlist = Wishlist.objects.filter(user_profile=user_profile)
        wishlists = Wishlist.objects.filter(product=product)
        for wishlist in wishlists:
            if wishlist.user_profile == user_profile:
                product_in_wishlist = True
    else:
        user_wishlist = None

    if request.user.is_authenticated:
        already_commented = ReviewRating.objects.filter(
            product_id=product_id, user=request.user
        ).exists()

    if not isinstance(request.user, AnonymousUser):
        all_items = OrderLineItem.objects.filter(
            order__user_profile__user=request.user
        )

    for item in all_items:
        if product == item.product:
            already_bought = True

    context = {
        "product": product,
        "reviews": reviews,
        "already_commented": already_commented,
        "already_bought": already_bought,
        "product_in_wishlist": product_in_wishlist,
        "user_wishlist": user_wishlist,
    }

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""

    if not request.user.is_superuser:
        messages.error(request, "No, no, no, only store owners can do that!:)")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. The form is invalid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""

    if not request.user.is_superuser:
        messages.error(request, "No, no, no, only store owners can do that!:)")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f"Successfully updated {product.name}!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. The form is invalid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""

    if not request.user.is_superuser:
        messages.error(request, "No, no, no, only store owners can do that!:)")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f"Product:{product.name} has been deleted!")
    return redirect(reverse("products"))


@login_required
def submit_review(request, product_id):
    """
    A view to submit the review/rating
    """
    url = request.META.get("HTTP_REFERER")
    if request.method == "POST":
        try:
            reviews = ReviewRating.objects.get(
                user__id=request.user.id, product__id=product_id
            )
            form = ReviewRatingForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, "Thanks! Your review has been updated.")
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewRatingForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data["subject"]
                data.rating = form.cleaned_data["rating"]
                data.review = form.cleaned_data["review"]
                data.product_id = product_id
                data.user_id = request.user.id
                data.already_commented = True
                data.save()
                messages.success(request, "Thank you! Review submitted.")
                return redirect(url)

from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def shopping_bag_contents(request):

    shopping_bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get("bag", {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        shopping_bag_items.append(
            {
                "item_id": item_id,
                "quantity": quantity,
                "product": product,
            }
        )

    if total < settings.FREE_DELIVERY_TRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_TRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        "shopping_bag_items": shopping_bag_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "free_delivery_delta": free_delivery_delta,
        "free_delivery_treshold": settings.FREE_DELIVERY_TRESHOLD,
        "grand_total": grand_total,
    }

    return context

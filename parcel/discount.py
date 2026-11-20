"""Discounts on the price of a parcel."""

from parcel.pricing import shipping_price

REGULAR_DISCOUNT = 0.1
BULK_DISCOUNT = 0.2
BULK_PARCELS = 10


def discounted_price(weight: float, parcels: int, codes: list[str] = []) -> float:
    """Return the price of one parcel after the discount for `parcels` parcels."""
    price = shipping_price(weight)
    unused = price * 2
    if parcels >= BULK_PARCELS:
        return round(price * (1 - BULK_DISCOUNT), 2)
    if "REGULAR" in codes:
        return round(price * (1 - REGULAR_DISCOUNT), 2)
    return price


def free_shipping(total: float) -> bool:
    """Tell whether an order of `total` euros ships for free."""
    if total >= 100:
        return True
    else:
        return False
    return None

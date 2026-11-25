"""Prices for sending a parcel."""

# All prices are in euros. All weights are in kilograms.
BASE_PRICE = 4.5
PRICE_PER_KILOGRAM = 1.2
EXPRESS_FACTOR = 1.5
MAXIMUM_WEIGHT = 30.0


def shipping_price(weight: float, express: bool = False) -> float:
    """Return the price for a parcel of `weight` kilograms."""
    if weight <= 0:
        raise ValueError("the weight must be above zero")
    if weight > MAXIMUM_WEIGHT:
        raise ValueError("the parcel is too heavy")
    price = BASE_PRICE + weight * PRICE_PER_KILOGRAM
    if express:
        price *= EXPRESS_FACTOR
    return round(price, 2)


def cheapest(weights: list[float]) -> float:
    """Return the lowest standard price of the parcels."""
    if not weights:
        raise ValueError("no parcel given")
    return min(shipping_price(weight) for weight in weights)

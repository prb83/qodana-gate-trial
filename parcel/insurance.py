"""Insurance for a parcel."""

from parcel.pricing import shipping_price

RATE = 0.02
MINIMUM_FEE = 1.0
MAXIMUM_VALUE = 5000.0


def insurance_fee(value: float) -> float:
    """Return the fee for insuring a parcel worth `value` euros."""
    if value <= 0:
        raise ValueError("the value must be above zero")
    if value > MAXIMUM_VALUE:
        raise ValueError("the value is too high to insure")
    return max(MINIMUM_FEE, round(value * RATE, 2))


def insured_price(weight: float, value: float, express: bool = False) -> float:
    """Return the price of a parcel with its insurance fee."""
    price = shipping_price(weight, express)
    return round(price + insurance_fee(value), 2)


def claim(value: float, damaged: bool) -> float:
    """Return the amount that the insurance pays for a parcel."""
    if not damaged:
        return 0.0
    if value > MAXIMUM_VALUE:
        return MAXIMUM_VALUE
    return value

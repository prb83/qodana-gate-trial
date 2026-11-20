import pytest

from parcel.pricing import cheapest, shipping_price


def test_standard_price():
    assert shipping_price(2) == 6.9


def test_express_price():
    assert shipping_price(2, express=True) == 10.35


@pytest.mark.parametrize("weight", [0, -1])
def test_weight_must_be_above_zero(weight):
    with pytest.raises(ValueError, match="above zero"):
        shipping_price(weight)


def test_weight_has_a_maximum():
    with pytest.raises(ValueError, match="too heavy"):
        shipping_price(30.1)


def test_cheapest_of_several_parcels():
    assert cheapest([5, 1, 3]) == 5.7


def test_cheapest_needs_a_parcel():
    with pytest.raises(ValueError, match="no parcel"):
        cheapest([])

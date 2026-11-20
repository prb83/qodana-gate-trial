from parcel.discount import discounted_price


def test_bulk_discount():
    assert discounted_price(2, parcels=10) == 5.52


def test_no_discount():
    assert discounted_price(2, parcels=1) == 6.9

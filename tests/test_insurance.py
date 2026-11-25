import pytest

from parcel.insurance import insurance_fee, insured_price


def test_fee_has_a_minimum():
    assert insurance_fee(10) == 1.0


def test_fee_follows_the_value():
    assert insurance_fee(200) == 4.0


def test_value_must_be_above_zero():
    with pytest.raises(ValueError, match="above zero"):
        insurance_fee(0)


def test_insured_price():
    assert insured_price(2, 200) == 10.9

import pytest
from capitalise_name import cap_name


def test_cap_name_positive_case_single_name():
    assert cap_name('chRis') == 'Chris'


def test_cap_name_positive_case_four_names():
    assert cap_name('maya alice Jane johnson') == 'Maya Alice Jane Johnson'


def test_cap_name_negative_case_no_name():
    assert not cap_name('')

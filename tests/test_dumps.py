from watsonpy import dumps
import pytest

@pytest.mark.skip()
def test_dumps_int_01():
    data = 123
    assert dumps(data) == "BBuaBubaBubbbaBubbbbaBubbbbbaBubbbbbba"

@pytest.mark.skip()
def test_dumps_str_01():
    data = "tako"
    assert dumps(data) == "?SShaakShaaaakShaaaaakShaaaaaak-SShkShaaaaakShaaaaaak-SShkShakShaaakShaaaaakShaaaaaak-SShkShakShaakShaaakShaaaaakShaaaaaak-"

@pytest.mark.skip()
def test_dumps_object_01():
    data = {"first":True,"hello":"world"}
    assert dumps(data) == "~?ShaaaaaarrShaaaaarrkShaaarrk-SameeShaaaaaarrShaaaaarrkShaarrkShrrk-ShaaaaaarrShaaaaakSameeShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrkSharrkShrrk-$BubbbbbbBubbbbbaBubbbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbbaBuba!BubbbbbbBubbbbbaBubbbaBubba!BubbbbbbBubbbbbaBubba!M?ShaaaaaaShaaaaakShaakShak-ShaaaaaaShaaaaakShaaakShk-ShaaaaaaShaaaaakShaaaakShak-ShaaaaaaShaaaaakShaaaakShakShk-ShaaaaaaShaaaaakShaaaakShaak-^!!!!!!!!!!!!!g"
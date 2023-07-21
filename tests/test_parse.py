from watsonpy import parse


def test_parse_integer_01():
    watson_code = "BBuaBubaBubbbaBubbbbaBubbbbbaBubbbbbba"
    assert parse(watson_code) == [123]

def test_parse_string_01():
    watson_code = "?SShaakShaaaakShaaaaakShaaaaaak-SShkShaaaaakShaaaaaak-SShkShakShaaakShaaaaakShaaaaaak-SShkShakShaakShaaakShaaaaakShaaaaaak-"
    assert parse(watson_code) == ["tako"]

def test_parse_object_01():
    watson_code = """~?ShaaaaaarrShaaaaarrkShaaarrk-SameeShaaaaaarrShaaaaarrkShaarrkShrrk-ShaaaaaarrShaaaaakSameeShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrkSharrkShrrk-$BubbbbbbBubbbbbaBubbbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbbaBuba!BubbbbbbBubbbbbaBubbbaBubba!BubbbbbbBubbbbbaBubba!M?ShaaaaaaShaaaaakShaakShak-ShaaaaaaShaaaaakShaaakShk-ShaaaaaaShaaaaakShaaaakShak-ShaaaaaaShaaaaakShaaaakShakShk-ShaaaaaaShaaaaakShaaaakShaak-^!!!!!!!!!!!!!g"""
    assert parse(watson_code) == [{"first":True,"hello":"world"}]

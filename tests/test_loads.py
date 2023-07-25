from watsonpy import loads


def test_loads_int_01():
    watson_code = "BBuaBubaBubbbaBubbbbaBubbbbbaBubbbbbba"
    assert loads(watson_code) == 123

def test_loads_str_01():
    watson_code = "?SShaakShaaaakShaaaaakShaaaaaak-SShkShaaaaakShaaaaaak-SShkShakShaaakShaaaaakShaaaaaak-SShkShakShaakShaaakShaaaaakShaaaaaak-"
    assert loads(watson_code) == "tako"

def test_loads_object_01():
    watson_code = """~?ShaaaaaarrShaaaaarrkShaaarrk-SameeShaaaaaarrShaaaaarrkShaarrkShrrk-ShaaaaaarrShaaaaakSameeShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrkSharrkShrrk-$BubbbbbbBubbbbbaBubbbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbbaBuba!BubbbbbbBubbbbbaBubbbaBubba!BubbbbbbBubbbbbaBubba!M?ShaaaaaaShaaaaakShaakShak-ShaaaaaaShaaaaakShaaakShk-ShaaaaaaShaaaaakShaaaakShak-ShaaaaaaShaaaaakShaaaakShakShk-ShaaaaaaShaaaaakShaaaakShaak-^!!!!!!!!!!!!!g"""
    assert loads(watson_code) == {"first":True,"hello":"world"}

from watsonpy import watsonify

def test_watsonify_int_01():
    data = [123]
    assert watsonify(data) == "BBuaBubaBubbbaBubbbbaBubbbbbaBubbbbbba"

def test_watsonify_str_01():
    data = ["tako"]
    assert watsonify(data) == "?SShaakShaaaakShaaaaakShaaaaaak-SShkShaaaaakShaaaaaak-SShkShakShaaakShaaaaakShaaaaaak-SShkShakShaakShaaakShaaaaakShaaaaaak-"

def test_watsonify_object_01():
    data = [{"first":True,"hello":"world"}]
    assert watsonify(data) == "~?ShaaaaaarrShaaaaarrkShaaarrk-SameeShaaaaaarrShaaaaarrkShaarrkShrrk-ShaaaaaarrShaaaaakSameeShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrk-ShaaaaaarrShaaaaarrkShaaarrkShaarrkSharrkShrrk-$BubbbbbbBubbbbbaBubbbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbaBubbaBubaBua!BubbbbbbBubbbbbaBubbbbaBuba!BubbbbbbBubbbbbaBubbbaBubba!BubbbbbbBubbbbbaBubba!M?ShaaaaaaShaaaaakShaakShak-ShaaaaaaShaaaaakShaaakShk-ShaaaaaaShaaaaakShaaaakShak-ShaaaaaaShaaaaakShaaaakShakShk-ShaaaaaaShaaaaakShaaaakShaak-^!!!!!!!!!!!!!g"
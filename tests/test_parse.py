from watsonpy import parse

def test_parse_Inew_01():
    watson_code = "B"
    assert parse(watson_code) == [0]

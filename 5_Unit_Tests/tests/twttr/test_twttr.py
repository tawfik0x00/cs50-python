from twttr import shorten

def test_upper_lower():
    # Our Cases
    assert shorten("Twitter") == "Twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwITTer") == "TwTTr"

def test_number():
    assert shorten("1234") == "1234"

def test_punctuation():
    assert shorten('!?.,') == '!?.,'

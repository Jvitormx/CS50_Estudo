from twttr import shorten

def test_twttr():
    assert shorten("twitter")=="twttr"

def test_upper_twttr():
    assert shorten("TWITTER")=="TWTTR"

def test_numbers_twttr():
    assert shorten("1234")=="1234"

def test_ponctuation_twttr():
    assert shorten("TWITTER!")=="TWTTR!"

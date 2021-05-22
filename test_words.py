from words import prefix, suffix
import pytest

def test_prefix():
    string = prefix("", "") 
    assert string == ''

    string = prefix("", "correct") 
    assert string == ''

    string = prefix("clear", "") 
    assert string == ''

    string = prefix("happy", "funny") 
    assert string == ''

    string = prefix("cat", "catalog") 
    assert string == 'cat'

    string = prefix("dogmatic", "dog") 
    assert string == 'dog'

    string = prefix("jump", "joyous") 
    assert string == 'j'

    string = prefix("unwise", "ungrateful") 
    assert string == 'un'

    string = prefix("Disable", "dIstasteful") 
    assert string == 'dis'


def test_suffix():
    string = suffix("", "") 
    assert string == ''

    string = suffix("", "correct") 
    assert string == ''

    string = suffix("clear", "") 
    assert string == ''

    string = suffix("angelic", "awesome") 
    assert string == ''

    string = suffix("found", "profound") 
    assert string == 'found'

    string = suffix("ditch", "itch") 
    assert string == 'itch'

    string = suffix("happy", "funny") 
    assert string == 'y'

    string = suffix("tired", "fatigued") 
    assert string == 'ed'

    string = suffix("swimming", "FLYING") 
    assert string == 'ing'

pytest.main(["-v", "--tb=line", "-rN", "test_words.py"])
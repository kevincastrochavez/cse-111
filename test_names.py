from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    string = make_full_name("Sally", "Brown") 
    assert string == 'Brown;Sally'

def test_extract_family_name():
    string = extract_family_name("Brown; Sally") 
    assert string == 'Brown'

def test_extract_given_name():
    string = extract_given_name("Brown; Sally") 
    assert string == 'Sally'


pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])
from trip import TripCalculator
import pytest

def test_cleanup():
    '''
    Assert that clean up operations are smooth
    '''
    
    tc = TripCalculator()
    assert len(tc.clean_up("a\n\n\b\n\nc\n")) == 3
    

def test_invalid():
    '''
    Test with some invalid input
    '''
    tc = TripCalculator()
    assert tc.calculate("a\n", "") == 'The number of entries in the two datasets do not match'
    assert tc.calculate("", "a") == 'The number of entries in the two datasets do not match'
    assert tc.calculate("a","a") == 'Error in reading expenses, please make sure you have entered valid numbers.'
    
    
def test_valid():
    '''
    Test with some valid inputs
    '''
    
    tc = TripCalculator()
    resp = tc.calculate("a\nb\nc", "1,2,3\n2,3,4\n4,5,6\n")
    assert 'a owes' in resp
    assert 'b owes' in resp
    assert 'Others owe c' in resp
    
    
    
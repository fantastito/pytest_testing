import pytest
from lib.present import *

def test_present_wrap():
    callum_present = Present()
    callum_present.wrap('Barbie')
    with pytest.raises(Exception) as e:
        callum_present.wrap('Action man')
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."

def test_present_unwrap():
    callum_present = Present()
    with pytest.raises(Exception) as e:
        callum_present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

# 1. run wrap, get error, pass
# 2. run unwrap, get error, pass
# 3. run wrap, run unwrap, no error, pass
'''
test code with pytest
'''

from hello import add


def test_add():
    '''
    add Function test code
    '''
    assert add(1, 2) == 3

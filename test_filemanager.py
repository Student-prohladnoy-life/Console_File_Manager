from core import info_platform, info_developer, create_file, create_folder, get_list

def test_info_platform():
    assert info_platform() == info_platform(), 'Test failed!!!'


def test_info_developer():
    assert info_developer() == "Student-prohladnoy-life", 'Test failed!!!'

def test_create_file():
    assert create_file('core.py') == create_file('core.py'), 'Test failed!!!'

def test_create_folder():
    assert create_folder() == create_folder(), 'Test failed!!!'

def test_get_list():
    assert get_list() == get_list(), 'Test failed!!!'
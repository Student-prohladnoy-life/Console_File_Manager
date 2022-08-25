from core import get_list

def test_listdir():
    assert get_list('D:/Python_project/Console_File_Manager') == 'D:/Python_project/Console_File_Manager'
    assert get_list('folder') == 'new2', '.git'
    assert get_list('folder') == '.idea', 'folder'
    assert get_list('folder') == 'new_folder', 'test_folder'
    assert get_list('folder') == 'venv', '__pycache__'

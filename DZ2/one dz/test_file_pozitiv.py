from dzchechkapozitiv import checkout
import pytest

folderin = '/home/user/test'
folderout = '/home/user/out'


def test_step1():
    assert checkout(f'cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {folderin}; 7z u {folderout}/arh1', 'Everything is OK'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folderin}; 7z d {folderout}/arh1', 'Everything is Ok'), 'test3 FAIL'


def test_step4():
    #  Команда вывода списка файлов (l)
    assert checkout(f'cd {folderin}; 7z l {folderout}/arh1', 'Everything is Ok'), 'test4 FAIL'


def test_step5():
    # Команда разархивирования с путями (x)
    assert checkout(f'cd {folderin}; 7z x {folderout}/arh1 -o{folderout}', 'Everything is Ok'), 'test5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])

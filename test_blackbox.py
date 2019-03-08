from blackbox import blackbox

print('Importando blackbox')

def test_method1():

    assert 1 == blackbox.method1(), 'debe ser  1'

def test_method2():

    assert 3 == blackbox.method2(), 'debe ser  2'
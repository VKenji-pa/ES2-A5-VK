import pytest
from lanchonete import Carrinho , Menu

@pytest.fixture
def data():
    return [{'nome': 'arroz', 'preco': 8},
            {'nome': 'coxinha', 'preco': 3.50}]

def test_carrinho_empty():
    c = Carrinho()
    
    assert not c.get_lista()
    assert c.get_total() == 0

def test_carrinho_adding_item(data):
    c = Carrinho()
    for i in data:
        c.add(i)
        
    ls = c.get_lista()
    
    assert len(ls) == 2
    assert ls[-1]['nome'] == 'coxinha'
    
def test_carrinho_removing_item(data):
    c = Carrinho()
    for i in data:
        c.add(i)
        
    c.remove()
    
    ls = c.get_lista()
    assert len(ls) == 1
    assert ls[-1]['nome'] == 'arroz'
    
def test_carrinho_conteudo(data):
    c = Carrinho()
    c.add(data[0])    
    
    res = c.conteudo()
    assert res == ("=== Carrinho ===\n"
                   "arroz - R$ 8.00\n")

##### MENU #####

def test_menu_read_file():
    f = open('tests/testMenu.txt', 'w')
    f.write('banana; 1.50')
    f.close()
    
    m = Menu()
    m.ler_menu('tests/testMenu.txt')
    
    assert len(m.get()) == 1
    assert m.get()[0]['nome'] == 'banana'
    
def test_menu_add(data):
    m = Menu()
    
    for i in data:
        m.adicionar_item(i)
        
    assert len(m.get()) == 2

def test_menu_remove(data):
    m = Menu()
    
    for i in data:
        m.adicionar_item(i)
    
    m.remover_item(1)   # idx + 1
    
    assert len(m.get()) == 1
    assert m.get()[0]['nome'] == 'coxinha'
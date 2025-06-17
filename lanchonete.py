import os

SENHA_ADMIN = 'admin123'

class Carrinho:
    _valor_total = 0
    _lista = []
    
    def __init__(self):
        self._valor_total = 0
        self._lista = []
    
    def get_total(self):
        return self._valor_total
    
    def get_lista(self):
        return self._lista
    
    def add(self, item):
        self._valor_total += item['preco']
        self._lista.append(item)
        
    def remove(self):
        if self._lista:
            self._lista.pop()
        else:
            print("Carrinho vazio")
            
    def conteudo(self):
        i = ("=== Carrinho ===\n")
        
        for item in self._lista:
            i += (f"{item['nome']} - R$ {item['preco']:.2f}\n")
        
        return i
    
class Menu:
    _lista = []
    
    def __init__(self):
        self._lista = []
    
    def get(self):
        return self._lista
    
    def remover_item(self, codigo):
        self._lista.pop(codigo-1)
                
    def adicionar_item(self, item):            
        self._lista.append(item)
        
    def mostrar_menu(self):
        print("=== MENU DO DIA ===")
        for item in self._lista:
            print(f"{self._lista.index(item) + 1} - {item['nome']} - R$ {item['preco']:.2f}")
            
    def ler_menu(self, arquivo_menu):
        if not os.path.exists(arquivo_menu):
            print(f"Arquivo {arquivo_menu} não encontrado.")
            
        with open(arquivo_menu, 'r', encoding='utf-8') as f:
            for linha in f:
                partes = linha.strip().split(';')
                if len(partes) == 2:
                    nome, preco = partes
                    self._lista.append({
                        'nome': nome,
                        'preco': float(preco.replace(',', '.'))
                    })
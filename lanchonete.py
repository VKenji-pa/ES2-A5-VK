import os

SENHA_ADMIN = 'admin123'

'''def ler_menu(arquivo_menu):
    menu = []
    if not os.path.exists(arquivo_menu):
        print(f"Arquivo {arquivo_menu} não encontrado.")
        return menu
    with open(arquivo_menu, 'r', encoding='utf-8') as f:
        for linha in f:
            partes = linha.strip().split(';')
            if len(partes) == 3:
                codigo, nome, preco = partes
                menu.append({
                    'codigo': codigo,
                    'nome': nome,
                    'preco': float(preco.replace(',', '.'))
                })
    return menu'''

def mostrar_menu(menu):
    print("=== MENU DO DIA ===")
    for item in menu:
        print(f"{menu.index(item) + 1} - {item['nome']} - R$ {item['preco']:.2f}")

def escolher_itens(menu):
    carrinho = []
    while True:
        mostrar_menu(menu)
        print("\nTotal do carrinho: R$ {:.2f}".format(sum(item['preco'] for item in carrinho)))
        escolha = input("Digite o código do item para adicionar ao carrinho (ou 'fim' para finalizar): ").strip()
        
        if escolha.lower() == 'fim':
            break
        
        item = menu[escolha-1]
        
        if escolha <= len(menu):
            carrinho.append(item)
            print(f"{item['nome']} adicionado ao carrinho.")
            os.system('cls' if os.name == 'nt' else 'clear')
        else:
            print("Código inválido. Tente novamente.")
            
    return carrinho

def gerar_recibo(carrinho, arquivo_recibo):
    total = sum(item['preco'] for item in carrinho)
    with open(arquivo_recibo, 'w', encoding='utf-8') as f:
        f.write("=== RECIBO ===\n")
        for item in carrinho:
            f.write(f"{item['nome']} - R$ {item['preco']:.2f}\n")
        f.write(f"\nTOTAL: R$ {total:.2f}\n")
    print(f"Recibo gerado em {arquivo_recibo}")
        
def remover_item(codigo, menu):
    menu.pop(codigo-1)
            
def adicionar_item(item, menu):
    print("Adicionando novo item")
    menu.append(item)
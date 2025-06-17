import os


def ler_menu(arquivo_menu):
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
    return menu

def mostrar_menu(menu):
    print("=== MENU DO DIA ===")
    for item in menu:
        print(f"{item['codigo']} - {item['nome']} - R$ {item['preco']:.2f}")

def escolher_itens(menu):
    carrinho = []
    while True:
        mostrar_menu(menu)
        print("\nTotal do carrinho: R$ {:.2f}".format(sum(item['preco'] for item in carrinho)))
        escolha = input("Digite o código do item para adicionar ao carrinho (ou 'fim' para finalizar): ").strip()
        if escolha.lower() == 'fim':
            break
        item = next((i for i in menu if i['codigo'] == escolha), None)
        if item:
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
    
    
def pedido():
    menu = ler_menu('menu.txt')
    print("Bem-vindo à Lanchonete!")
    if not menu:
        return
    
    carrinho = escolher_itens(menu)
    if not carrinho:
        print("Nenhum item selecionado.")
        return
    print("\nSeu carrinho:")
    for item in carrinho:
        print(f"- {item['nome']} - R$ {item['preco']:.2f}")
    confirmar = input("Deseja confirmar o pedido? (s/n): ").strip().lower()
    if confirmar == 's':
        gerar_recibo(carrinho, 'recibo.txt')
    else:
        print("Pedido cancelado.")

def main():
    while True:
        print("Lanchonete - Sistema de Pedidos")
        print("1 - Fazer Pedido\n"
            "2 - Sair\n"
            "0 - Admin")
        opt = input("Digite uma opção: ")
        
        match opt:
            case '1':
                pedido()
            case '2':
                print("Saindo do sistema. Até logo!")
                break
            case '0':
                print("Acesso ao modo admin não implementado.")
            case _:
                print("Opção inválida. Tente novamente.")
    

if __name__ == "__main__":
    main()
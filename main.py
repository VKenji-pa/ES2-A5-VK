from lanchonete import *

def pedido(menu=Menu()):
    if not menu:
        print("Sem produtos cadastrados")
        return
    
    carrinho = Carrinho()
    while True:
        print("\nBem-vindo à Lanchonete!")
        menu.mostrar_menu()
        print("\nTotal do carrinho: R$ {:.2f}".format(sum(item['preco'] for item in carrinho.get_lista())))
        escolha = input("Digite:\n"
                        "- O código do item para adicionar ao carrinho, ou\n"
                        "- 'fim' para finalizar, ou\n"
                        "- 'corrigir' para remover o ultimo item inserido\n").strip()
        
        if escolha.lower() == 'fim':
            break
        elif escolha.lower() == 'corrigir':
            carrinho.remove()
        else:
            try:
                codigo_item = int(escolha)
                if 0 < codigo_item <= len(menu.get()):
                    item = menu.get()[codigo_item - 1]
                    carrinho.add(item)
                    print(f"{item['nome']} adicionado ao carrinho.")
                else:
                    print("Código inválido. Esse item não existe no menu.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número, 'fim' ou 'corrigir'.")


    if not carrinho.get_lista():
        print("Nenhum item selecionado.")
        return
    
    print(carrinho.conteudo())
    print(f"=== TOTAL: R$ {carrinho.get_total()}\n")

    confirmar = input("Deseja confirmar o pedido? (s/n): ").strip().lower()
    
    if confirmar == 's':
        f = open('recibo.txt', 'w')
        f.write(carrinho.conteudo()
                + f"\n=== TOTAL: R$ {carrinho.get_total()}")
        print("\nRECIBO GERADO\n")
    else:
        print("Pedido cancelado.")

def admin(menu=Menu()):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if not menu.get():
            print("== Nenhum item no menu ==\n")
        else:
            menu.mostrar_menu()
        
        print("\n1 - Adicionar Item ao Menu\n"
            "2 - Remover Item do Menu\n"
            "3 - Sair")
        
        opt = input("Digite uma opção: ")
        
        match opt:
            case '1':
                item = {}
                item['nome'] = input("Informe o item a ser adicionado: ").strip()
                while True:
                    item['preco'] = float(input("Informe o valor do produto: "))
                    if item['preco'] >= 0:
                        break     
                               
            case '2':
                if not menu.get():
                    print("Nenhum item no menu para remover.")
                else:
                    codigo = int(input("Digite o código do item a ser removido: ").strip())
                    menu.remover_item(codigo)
            case '3':
                break
            
def main():
    menu = Menu()
    menu.ler_menu('menu.txt')
    while True:
        print("\nLanchonete - Sistema de Pedidos")
        print("1 - Fazer Pedido\n"
            "2 - Sair\n"
            "0 - Admin")
        opt = input("Digite uma opção: ")
        
        match opt:
            case '1':
                pedido(menu)
            case '2':
                print("Saindo do sistema. Até logo!")
                break
            case '0':
                senha = input("Digite a senha de admin: ")
                if senha == SENHA_ADMIN:
                    admin(menu)
                else:
                    print("Senha incorreta. Acesso negado.")
            case _:
                print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    main()
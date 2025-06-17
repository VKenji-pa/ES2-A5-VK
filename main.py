from lanchonete import *

def pedido(menu):
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

def admin(menu):
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        if not menu:
            print("Nenhum item no menu.")
        else:
            mostrar_menu(menu)
        
        print("1 - Adicionar Item ao Menu\n"
            "2 - Remover Item do Menu\n"
            "3 - Sair")
        
        opt = input("Digite uma opção: ")
        
        match opt:
            case '1':
                adicionar_item(menu)                
            case '2':
                if not menu:
                    print("Nenhum item no menu para remover.")
                else:
                    codigo = input("Digite o código do item a ser removido: ").strip()
                    remover_item(codigo, menu)
            case '3':
                break
            
def main():
    menu = []
    while True:
        print("Lanchonete - Sistema de Pedidos")
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
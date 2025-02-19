from datetime import datetime

class Estoque: 
    """   
    Representa o coração do sismte
    """
    def __init__(self):
        self.listaDeProdutos = []
        self.listaDePedidos = []
        self.fornecedores = {}
        self.categorias = {}

    def adicionarProduto(self, produto):
        """Adiciona um produto ao estoque"""
        self.listaDeProdutos.append(produto)

    def adicionarPedido(self, pedido):
        """Adiciona um pedido ao sistema"""
        self.listaDePedidos.append(pedido)

    def finalizarPedidos(self):
        """Finaliza todos os pedidos, fazendo a retirada do estoque dos produtos"""
        for pedido in self.listaDePedidos:
            for produto, quantidade in pedido.itens.items():
                for prod in self.listaDeProdutos:
                    if prod.codigo == produto.codigo:
                        prod.retirada(quantidade)
                        break


class Produto:
    """
    Representa um produto no estoque, contendo informações como nome, código, 
    quantidade, peso, categoria, preço e fornecedor.

    Atributos:
        nome (str): Descrição do nome do produto.
        codigo (int): Código único do produto.
        quantidade (int): Quantidade disponível em unidades.
        peso (float): Peso em Kg.
        categoria (int): ID da categoria do produto.
        preco (float): Preço unitário do produto.
        fornecedor (int): ID do fornecedor do produto.
        historicoDeMovi (list): Registra o histórico de movimentações do produto.
    """

    def __init__(self, nome: str, codigo: int, quantidade: int, peso: float, categoria: int, preco: float, fornecedor: int):
        """
        Inicializa um novo produto com os dados fornecidos.

        Args:
            nome (str): Nome do produto.
            codigo (int): Código do produto.
            quantidade (int): Quantidade inicial em estoque.
            peso (float): Peso unitário em Kg.
            categoria (int): ID da categoria do produto.
            preco (float): Preço unitário do produto.
            fornecedor (int): ID do fornecedor do produto.
        """
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.peso = peso
        self.categoria = categoria
        self.preco = preco
        self.fornecedor = fornecedor
        self.historicoDeMovi = []

    def registrarMovimentacao(self, tipo: str, quantidade: int):
        """
        Registra uma movimentação no histórico com a data.

        Args:
            tipo (str): Tipo da movimentação ("Adição" ou "Retirada").
            quantidade (int): Quantidade movimentada.
        """
        data = datetime.today().strftime("%d/%m/%Y")
        self.historicoDeMovi.append(f"{data} - {tipo}: {quantidade} unidades.")

    def adicionar(self, quantAdicionada: int):
        """
        Adiciona uma quantidade ao estoque do produto.

        Args:
            quantAdicionada (int): Quantidade a ser adicionada ao estoque.
        """
        self.quantidade += quantAdicionada
        self.registrarMovimentacao("Adição", quantAdicionada)

    def retirada(self, quantidadeRetirada: int):
        """
        Retira uma quantidade do estoque, verificando se há saldo suficiente.

        Args:
            quantidadeRetirada (int): Quantidade a ser removida do estoque.

        Raises:
            ValueError: Se a quantidade retirada for maior que o estoque disponível.
        """
        if quantidadeRetirada > self.quantidade:
            raise ValueError("Quantidade insuficiente em estoque.")
        self.quantidade -= quantidadeRetirada
        self.registrarMovimentacao("Retirada", quantidadeRetirada)

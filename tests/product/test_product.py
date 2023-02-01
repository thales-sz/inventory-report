from inventory_report.inventory.product import Product

"""from tests.factories.product_factory import ProductFactory"""


def test_cria_produto():
    product = Product(5, "Batata", "Donalds", "11/10", "31/10", 5, "G")

    assert product.id == 5
    assert product.nome_do_produto == "Batata"
    assert product.nome_da_empresa == "Donalds"
    assert product.data_de_fabricacao == "11/10"
    assert product.data_de_validade == "31/10"
    assert product.numero_de_serie == 5
    assert product.instrucoes_de_armazenamento == "G"


def test_relatorio_produto():
    product = Product(5, "Batata", "Donalds", "11/10", "31/10", 5, "G")

    assert (
        product.__repr__()
        == (
            f"O produto {product.nome_do_produto}"
            f" fabricado em {product.data_de_fabricacao}"
            f" por {product.nome_da_empresa} com validade"
            f" até {product.data_de_validade}"
            f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
        )
    )

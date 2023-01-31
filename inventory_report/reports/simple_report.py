from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data: list[dict]) -> str:
        fabrica = None
        validade = None
        empresa = None
        hoje = datetime.now()
        datas_fabricacao = [
            datetime.strptime(produto["data_de_fabricacao"], "%Y-%m-%d")
            for produto in data
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            >= hoje
        ]
        datas_validade = [
            datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            for produto in data
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            >= hoje
        ]
        empresas = [
            produto["nome_da_empresa"]
            for produto in data
            if datetime.strptime(produto["data_de_validade"], "%Y-%m-%d")
            >= hoje
        ]
        fabrica = min(datas_fabricacao)
        validade = min(datas_validade)
        empresa = max(empresas, key=empresas.count)
        return (
            f"Data de fabricação mais antiga: {fabrica.strftime('%Y-%m-%d')}\n"
            f"Data de validade mais próxima: {validade.strftime('%Y-%m-%d')}\n"
            f"Empresa com mais produtos: {empresa}"
        )

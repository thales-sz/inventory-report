from datetime import datetime


class SimpleReport:
    @staticmethod
    def generate(data):
        fabricaçao = None
        validade = None
        empresa = None
        hoje = datetime.now().date()
        datas_fabricacao = [
            datetime.strptime(produto["data_de_fabricacao"], "%Y-%m-%d").date()
            for produto in data
            if datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d"
            ).date()
            >= hoje
        ]
        if datas_fabricacao:
            fabricaçao = min(datas_fabricacao)
        datas_validade = [
            datetime.strptime(produto["data_de_validade"], "%Y-%m-%d").date()
            for produto in data
            if datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d"
            ).date()
            >= hoje
        ]
        if datas_validade:
            validade = min(datas_validade)
        empresas = [
            produto["nome_da_empresa"]
            for produto in data
            if datetime.strptime(
                produto["data_de_validade"], "%Y-%m-%d"
            ).date()
            >= hoje
        ]
        if empresas:
            empresa = max(set(empresas), key=empresas.count)
        return f"""
        Data de fabricação mais antiga: {fabricaçao.strftime('%Y-%m-%d')}\n
        Data de validade mais próxima: {validade.strftime('%Y-%m-%d')}\n
        Empresa com mais produtos: {empresa}
        """

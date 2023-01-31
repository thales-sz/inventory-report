class SimpleReport:
    @staticmethod
    def generate(data: list[dict]) -> str:
        oldest = None
        nearest = None
        company = None
        max = 0
        for product in data:
            data_de_fabricacao = product["data_de_fabricacao"]
            data_de_validade = product["data_de_validade"]
            if not oldest or data_de_fabricacao < oldest:
                oldest = data_de_fabricacao
            if not nearest or data_de_validade < nearest:
                nearest = data_de_validade
            nome_da_empresa = product["nome_da_empresa"]
            company_count = data.count(product)
            if company_count > max:
                max = company_count
                company = nome_da_empresa
        return f"""
        Data de fabricação mais antiga: {oldest}\n
        Data de validade mais próxima: {nearest}\n
        Empresa com mais produtos: {company}
        """

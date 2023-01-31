from .simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(data):
        simple_response = SimpleReport.generate(data)
        empresa = [product["nome_da_empresa"] for product in data]
        qtd_empresas = Counter(empresa)
        response = ""
        for item, count in qtd_empresas.items():
            response += f"- {item}: {count}\n"

        return (
            simple_response + "\nProdutos estocados por empresa:\n" + response
        )

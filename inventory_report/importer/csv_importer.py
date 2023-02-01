from .importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(file):
        if file.endswith(".csv"):
            return super().import_data(file)
        raise ValueError("Arquivo inválido")

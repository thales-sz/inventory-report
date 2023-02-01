from .importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(file):
        if file.endswith(".json"):
            return super().import_data(file)
        raise ValueError("Arquivo inválido")

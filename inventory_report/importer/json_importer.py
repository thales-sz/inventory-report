from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        if file.endswith(".json"):
            return Inventory.verify_archive_format(file)
        raise ValueError("Arquivo inválido")

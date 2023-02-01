from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @classmethod
    def import_data(file):
        if file.endswith(".csv"):
            return Inventory.verify_archive_format(file)
        raise ValueError("Arquivo inválido")

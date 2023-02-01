from .importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @classmethod
    def import_data(file):
        if file.endswith(".xml"):
            return Inventory.verify_archive_format(file)
        raise ValueError("Arquivo inválido")

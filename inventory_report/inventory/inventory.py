from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xmltodict
import csv
import json


class Inventory:
    @staticmethod
    def verify_archive_format(file):
        with open(file) as archive:
            if file.endswith(".csv"):
                return list(csv.DictReader(archive))
            elif file.endswith(".json"):
                return json.load(archive)
            data = xmltodict.parse(archive.read())
            formatted = data["dataset"]["record"]
            return list(dict(item) for item in formatted)

    @staticmethod
    def import_data(__path__, type):
        product_list = Inventory.verify_archive_format(__path__)
        if type == "simples":
            return SimpleReport().generate(product_list)
        return CompleteReport().generate(product_list)

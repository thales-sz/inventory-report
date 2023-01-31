from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import xml.etree.ElementTree as et
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
            else:
                arquivo = et.parse(archive)
                raiz = arquivo.getroot()
                for item in raiz:
                    print(item)

    @classmethod
    def import_data(test, __path__, type):
        print(test, __path__, type)
        product_list = Inventory.verify_archive_format(__path__)
        if type == "simples":
            return SimpleReport().generate(product_list)
        else:
            return CompleteReport().generate(product_list)

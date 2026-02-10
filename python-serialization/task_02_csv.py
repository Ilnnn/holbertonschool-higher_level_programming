#!/usr/bin/python3
import csv
import json

def convert_csv_to_json(filename):
    """
    Convertit un fichier CSV en fichier JSON (data.json).

    Args:
        filename (str): Nom du fichier CSV à lire.

    Returns:
        bool: True si succès, False en cas d'erreur.
    """
    try:
        data_list = []

        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json.file:
            json.dump(data_list, json_file)

        return True

    except (FileNotFoundError, OSError):
        return False

#!/usr/bin/python3

def serialize_and_save_to_file(data, filename):

    """
    Sérialise un dictionnaire Python et l'enregistre dans un fichier JSON.

    Args:
        data (dict): Le dictionnaire à sauvegarder.
        filename (str): Le nom du fichier JSON de sortie.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Charging files JSON from file and convert in Python.

    Args:
        filename (str): Le nom du fichier JSON à lire.

    Returns:
        dict: Le dictionnaire Python obtenu après désérialisation.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)

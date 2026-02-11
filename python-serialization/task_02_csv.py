#!/usr/bin/python3
import csv
import json


def convert_csv_to_json(filename):
    """
    Convert a CSV file to a JSON file (data.json).

    Args:
        filename (str): CSV file to read.

    Returns:
        bool: True if success, False otherwise.
    """
    try:
        data_list = []

        with open(filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data_list.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data_list, json_file)

        return True

    except (FileNotFoundError, OSError):
        return False

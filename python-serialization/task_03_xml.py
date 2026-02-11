#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a dictionary to an XML file."""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """Deserialize an XML file back into a dictionary."""
    result = {}

    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        for child in root:
            text = child.text

            if text is None:
                value = None
            elif text.lower() == "true":
                value = True
            elif text.lower() == "false":
                value = False
            else:
                try:
                    value = int(text)
                except ValueError:
                    value = text

            result[child.tag] = value

        return result

    except (ET.ParseError, FileNotFoundError, OSError):
        return None

#!/usr/bin/python3
"""
Ce module contient un script qui liste tous les états de la base de données
hbtn_0e_0_usa. Il prend trois arguments : nom d'utilisateur, mot de passe
et nom de la base de données.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    # Connexion au serveur MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Création du curseur pour exécuter les commandes SQL
    cursor = db.cursor()

    # Requête SQL pour récupérer les états triés par id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Récupération et affichage de toutes les lignes
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture propre du curseur et de la connexion
    cursor.close()
    db.close()
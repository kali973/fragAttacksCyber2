import subprocess

def run_command(command, description):
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        print(f"\033[1;33m{command}\033[0m")  # Affichage de la commande en orange
        print(f"\033[1;31m{description}\033[0m")  # Affichage du commentaire de la commande en rouge
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")


# Désactivation de la carte WiFi
run_command('sudo ifconfig wlan0 down', '# Désactiver la carte WiFi')

# Passage en mode géré
run_command('sudo iwconfig wlan0 mode managed', '# Passage en mode géré')

# Réactivation de la carte WiFi
run_command('sudo ifconfig wlan0 up', '# Réactiver la carte WiFi')

# Affichage des informations de la carte WiFi
run_command('iwconfig wlan0', '# Affichage des informations de la carte WiFi')

# Arrêt des processus interférents
run_command('airmon-ng check kill', '# Arrêt des processus interférents')

print()
input("Appuyez sur Entrée pour continuer...")

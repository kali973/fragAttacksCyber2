import subprocess


def is_wifi_connected():
    try:
        output = subprocess.check_output(['iw', 'dev']).decode('utf-8')
        if 'wlan0' in output:  # Remplacez 'wlan0' par l'interface WiFi correspondante
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False


def run_command(command, description):
    try:
        output = subprocess.check_output(command, shell=True).decode('utf-8')
        print(f"\033[1;36m{command}\033[0m")  # Affichage de la commande en bleu clair
        print(f"\033[1;31m{description}\033[0m")  # Affichage du commentaire de la commande en rouge
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de la commande : {e}")


if is_wifi_connected():
    print("Le dongle WiFi est connecté.")
    run_command('ifconfig', '# Affichage de la configuration de l\'interface')
    run_command('iwconfig', '# Affichage de la puissance de la carte WiFi')
    run_command('lsusb', '# Affichage de la liste des périphériques USB')

    # Informations détaillées du dongle WiFi
    run_command('lsusb -vs 001:002', '# Affichage des informations détaillées du dongle WiFi')

    # Informations du dongle WiFi
    run_command('ethtool -i wlan0', '# Affichage des informations de la carte WiFi')

    # Désactiver la carte WiFi
    run_command('sudo ifconfig wlan0', '# Désactiver la carte WiFi')

    # Activer le mode monitor
    run_command('sudo iwconfig wlan0 mode monitor', '# Activer le mode monitor')

    # Réactiver la carte WiFi
    run_command('sudo ifconfig wlan0 up', '# Réactiver la carte WiFi')

    # Informations de la carte WiFi
    run_command('iwconfig wlan0', '# Affichage des informations de la carte WiFi')

    # Désactivation de la carte WiFi
    run_command('sudo ip link set wlan0 down', '# Désactiver la carte WiFi')

    # Configuration du mode monitor
    run_command('sudo iw dev wlan0 set type monitor', '# Configuration du mode monitor')

    # Affichage des informations de configuration
    run_command('iwconfig', '# Affichage des informations de configuration')

    # Arrêt des processus interférents
    run_command('airmon-ng check kill', '# Arrêt des processus interférents')

    # Affichage des interfaces WiFi en mode monitor
    run_command('airmon-ng', '# Affichage des interfaces WiFi en mode monitor')

    # Exécution du test avec aireplay-ng
    run_command('aireplay-ng --test wlan0', '# Exécution du test avec aireplay-ng')

else:
    print("Le dongle WiFi n'est pas connecté.")

print()
input("Appuyez sur Entrée pour continuer...")

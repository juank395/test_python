import time
import random
import subprocess


def get_random_mac():  #Este codigo genera un codigo MAC Aleatorio
  return "02:%02x:%02x:%02x:%02x:%02x" % (random.randint(
      0, 255), random.randint(0, 255), random.randint(
          0, 255), random.randint(0, 255), random.randint(0, 255))


def change_mac(interface, new_mac):  #Con esta funcion se cambia el codigo MAC
  subprocess.call(["ip", "link", "set", interface, "down"])
  subprocess.call(["ip", "link", "set", interface, "address", new_mac])
  subprocess.call(["ip", "link", "set", interface, "up"])



if __name__ == "__main__":
  interface = "eth0"  # Cambia esto a la interfaz de red que deseas usar

  while True:
    new_mac = get_random_mac()  #Se genera un nuevo codigo MAC aleatorio
    change_mac(interface, new_mac)  #Se cambia el codigo MAC
    print(f"MAC address for {interface} changed to {new_mac}")  #Se imprime el nuevo codigo MAC
    time.sleep(30)  #Se espera 30 segundos antes de cambiar el codigo MAC nuevamente

    exit = input("Desea terminar el proceso? (s/n): >")  #Se pregunta al usuario si desea terminar el proceso
    if exit.lower() == "s":  #Si el usuario responde "s" (si), se termina el proceso, en caso contrario, se continua
      break

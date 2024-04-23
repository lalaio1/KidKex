import os
import subprocess
from colorama import Fore, Style, init
from start import iniciar_kex
from start import encerrar_processos

init()

def exibir_banner():
    print(f"""{Fore.LIGHTMAGENTA_EX}
▄ •▄ ▪  ·▄▄▄▄  ▄ •▄ ▄▄▄ .▐▄• ▄ 
█▌▄▌▪██ ██▪ ██ █▌▄▌▪▀▄.▀· █▌█▌▪
▐▀▀▄·▐█·▐█· ▐█▌▐▀▀▄·▐▀▀▪▄ ·██· 
▐█.█▌▐█▌██. ██ ▐█.█▌▐█▄▄▌▪▐█·█▌
·▀  ▀▀▀▀▀▀▀▀▀• ·▀  ▀ ▀▀▀ •▀▀ ▀▀                       ▀

[By // lalaio1]
    """)

def notificar(mensagem, tipo):
    if tipo == "info":
        print(f"{Fore.BLUE}[i]{Style.RESET_ALL} {mensagem}")
    elif tipo == "sucesso":
        print(f"{Fore.GREEN}[+]{Style.RESET_ALL} {mensagem}")
    elif tipo == "erro":
        print(f"{Fore.RED}[-]{Style.RESET_ALL} {mensagem}")
    else:
        print(f"{Fore.YELLOW}[!]{Style.RESET_ALL} {mensagem}")

os.system("cls")

exibir_banner()

print(f"{Fore.YELLOW}[!] Aviso!!: por favor instale o WSL com Kali Linux para funcionar\n\n")


print(f"{Fore.CYAN}1. Instalar o Win-KeX com todas as ferramentas do Kali Linux")
print(f"{Fore.CYAN}2. Instalar somente o Win-KeX")
print(f"{Fore.CYAN}3. Instalar todas as ferramentas do Kali Linux (para quem escolheu somente a opção 2)")
print(f"{Fore.RED}4. Menu Instalar {Fore.GREEN}WSL")

escolha = input(f"{Fore.RESET}-> ")

if escolha == "1":
    notificar(f"{Fore.BLUE}[!] Instalando o Win-KeX com todas as ferramentas do Kali Linux... (isso pode demorar um pouco)", "info")
    subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "update"])
    resultado_instalacao = subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "install", "-y", "kali-win-kex", "kali-linux-large"])
    if resultado_instalacao.returncode == 0:
        notificar(f"{Fore.GREEN}[+] Win-KeX instalado com sucesso!", "sucesso")
    else:
        notificar(f"{Fore.RED}[-] Erro ao instalar o Win-KeX.", "erro")

elif escolha == "2":
    notificar(f"{Fore.CYAN}[!] Instalando somente o Win-KeX... (isso pode demorar um pouco)", "info")
    subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "update"])
    resultado_instalacao = subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "install", "-y", "kali-win-kex"])
    if resultado_instalacao.returncode == 0:
        notificar(f"{Fore.GREEN}[+] Win-KeX instalado com sucesso!", "sucesso")
    else:
        notificar(f"{Fore.RED}[-] Erro ao instalar o Win-KeX.", "erro")

elif escolha == "3":
    notificar(f"{Fore.GREEN}[!] Instalando todas as ferramentas do Kali Linux... (isso pode demorar um pouco)", "info")
    subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "update"])
    resultado_instalacao = subprocess.run(["wsl", "-d", "kali-linux", "sudo", "apt", "install", "-y", "kali-linux-large"])
    if resultado_instalacao.returncode == 0:
        notificar(f"{Fore.GREEN}[+] Todas as ferramentas do Kali Linux instaladas com sucesso!", "sucesso")
    else:
        notificar(f"{Fore.RED}[-] Erro ao instalar as ferramentas do Kali Linux.", "erro")

elif escolha == "4":
    print(f"{Fore.CYAN}\n\n[1] Ubuntu\n[2] Debian\n[3] Kali Linux\n[4] Oracle Linux 8.5\n[5] Voltar")
    escolha = input(f"{Fore.RESET}-> ")

    if escolha == "1":
        notificar(f"{Fore.BLUE}[!] Instalando Ubuntu...", "info")
        subprocess.run(["wsl", "--install", "-d", "Ubuntu"])
        notificar(f"{Fore.GREEN}[+] Ubuntu instalado com sucesso!", "sucesso")
    elif escolha == "2":
        notificar(f"{Fore.BLUE}[!] Instalando Debian...", "info")
        subprocess.run(["wsl", "--install", "-d", "Debian"])
        notificar(f"{Fore.GREEN}[+] Debian instalado com sucesso!", "sucesso")
    elif escolha == "3":
        notificar(f"{Fore.BLUE}[!] Instalando Kali Linux...", "info")
        subprocess.run(["wsl", "--install", "-d", "Kali-linux"])
        notificar(f"{Fore.GREEN}[+] Kali Linux instalado com sucesso!", "sucesso")
    elif escolha == "4":
        notificar(f"{Fore.BLUE}[!] Instalando Oracle Linux 8.5...", "info")
        subprocess.run(["wsl", "--install", "-d", "OracleLinux_8_5"])
        notificar(f"{Fore.GREEN}[+] Oracle Linux 8.5 instalado com sucesso!", "sucesso")


print(f"{Fore.GREEN}[!] Para utilizar o kex, é só dar o comando 'kex' no seu terminal WSL")
input(f"{Fore.RED}\n\n\n\n\n[-] Pressione Enter para continuar...")
encerrar_processos()
iniciar_kex()

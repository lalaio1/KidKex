# WSL Installer and Kali Linux Kex Installer

This script is designed to streamline the installation process of various Linux systems using Windows Subsystem for Linux (WSL), as well as the installation of Kali Linux Kex with all available tools.

## Installation

### Prerequisites
- Python 3.x installed on your system
- Run `install.bat` as an administrator

### Steps
1. Download or clone this repository to your local machine.
2. Navigate to the directory containing the script.
3. Right-click on `install.bat` and select "Run as administrator" to ensure proper installation of Python and pip if not already installed.
4. After installing Python and pip, run `start.py` to start the installation process.

## Usage

1. Run `start.py`.
2. Follow the prompts to select the desired installation option:
   - Option 1: Install Win-KeX with all tools of Kali Linux.
   - Option 2: Install only Win-KeX.
   - Option 3: Install all tools of Kali Linux.
   - Option 4: Access the WSL installation menu to install other Linux distributions.
3. Follow any additional prompts to complete the installation process.

## Note

- Ensure that you run `install.bat` as an administrator to avoid any permission issues during installation.
- After installation, you can use the `kex` command in your WSL terminal to start Kali Linux Kex.


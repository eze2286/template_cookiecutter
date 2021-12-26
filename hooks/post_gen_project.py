import os
import subprocess

MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

print(f"{MESSAGE_COLOR}Almost done!")
print(f"Initializing a git repository...{RESET_ALL}")

subprocess.call(['git', 'init'])
subprocess.call(['git', 'add', '*'])
subprocess.call(['git', 'commit', '-m', 'Initial commit'])
# Iniciar ambiente virtual
subprocess.call(['python', '-m', 'venv', 'venv'])
# Ruta del entorno virtual
python_venv =   os.getcwd()+"\\venv\\Scripts\\python.exe"
# Instala pip y las librerías dentro de la carpeta donde se encuentra python
subprocess.call([python_venv,'-m', 'pip', '--upgrade', 'pip'])
subprocess.call([python_venv,'-m', 'pip', 'install', '-r', 'requirements.txt'])
# Instala las librerías indicadas
#subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

print(f"{MESSAGE_COLOR}The beginning of your destiny is defined now! Create and have fun!{RESET_ALL}")
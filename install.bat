@echo off

python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Python nao encontrado, instalando...
    powershell -Command "& { Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.11.7/python-3.11.7-amd64.exe' -OutFile 'python_installer.exe' }"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1
    del python_installer.exe
) else (
    echo Python ja está instalado.
)

pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Pip nao encontrado, instalando...
    python -m ensurepip
) else (
    echo Pip ja está instalado.
)

pip install -r requirements.txt
python Kex.py 

pause > nul 

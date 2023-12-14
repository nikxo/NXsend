@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Nettoyage
del ..\comp\NXsend.dist
del ..\comp\NXsend.build

:: Étape 1: Compiler avec Nuitka
echo Compilation du fichier Python avec Nuitka...
call nuitka --standalone --include-data-dir="..\..\Python_file\Base"=Base --include-data-dir="..\..\Python_file\frame0"=frame0 "..\..\Python_file\NXsend.py" --enable-plugin=tk-inter --windows-disable-console  --windows-icon-from-ico="file_comp\logo.ico" --output-dir="..\Build" --windows-uac-admin



echo Processus terminé.
ENDLOCAL

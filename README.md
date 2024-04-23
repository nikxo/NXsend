![Image de démonstration](https://raw.githubusercontent.com/nikxo/NXsend/main/File/NXsend_ban.jpg)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
![Static Badge](https://img.shields.io/badge/Nginx-1.7.11.3-green:badgeContent)
![Static Badge](https://img.shields.io/badge/Docker-17.06.0+-blue:badgeContent)
![GitHub stars](https://img.shields.io/github/stars/nikxo/Xeha)

# Description

# Installation
```bash
# Clone the repository
git clone https://github.com/nikxo/NXsend.git

# install requirements
pip install -r requirements.txt
```
# Usage
To use the basic functionality of this project, you will need to run some essential commands. Here's a quick guide
## Run server
Go to ``` Server ``` , open the terminal and type ```python Serv.py```

## Run client gui
Go to ``` App_Gui/Python_file ``` , open the terminal and type ```python NXsend.py```

## Purging sql tables
If you want to purge the SQL tables to start from a clean database you must :
- **For server**
   - Go to ``` Server ```, open the terminal and type ```python Database_client.py```
- **For client**
   - Go to ``` App_Gui/Python_file ```, open the terminal and type ```python Database.py```

# Usage
Pour utiliser les fonctionnalités de base de ce projet, vous devrez exécuter certaines commandes essentielles. Voici un guide rapide pour vous aider à démarrer :

## Lancement du Serveur
Pour démarrer le serveur, suivez ces étapes :
- Accédez au répertoire `Server`.
- Ouvrez le terminal.
- Tapez la commande suivante pour exécuter le serveur :
  ```bash
  python Serv.py
  ```

## Lancement de l'Interface Client GUI
Pour lancer l'interface graphique du client :
- Accédez au répertoire `App_Gui/Python_file`.
- Ouvrez le terminal.
- Tapez la commande suivante pour exécuter le client GUI :
  ```bash
  python NXsend.py
  ```

## Purge des Tables SQL
Si vous souhaitez purger les tables SQL pour recommencer avec une base de données propre, voici ce que vous devez faire :

- **Pour le Serveur** :
  - Allez dans le répertoire `Server`.
  - Ouvrez le terminal.
  - Tapez la commande suivante pour exécuter le script qui purge la base de données du serveur :
    ```bash
    python Database_client.py
    ```

- **Pour le Client** :
  - Allez dans `App_Gui/Python_file`.
  - Ouvrez le terminal.
  - Tapez la commande suivante pour purger la base de données du client :
    ```bash
    python Database.py
    ```

# Overview

## Token exchanger

![Image de démonstration]()

## Streaming area

![Image de démonstration]()

# License

Specify the license under which your project is distributed. If using a popular license (like MIT, Apache, or GPL), provide a brief summary and a link to the full text.

```text
This project is licensed under the MIT License - see the LICENSE file for details.
```

# Authors

List the project's authors and contributors. You can link to their GitHub profiles or personal websites.

- [Nikxo](https://github.com/nikxo)
- [Vegasword](https://github.com/vegasword)

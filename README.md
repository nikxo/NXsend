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
To use the basic features of this project, you need to run some essential commands. Here's a quick guide to get you started:

## Starting the Server
To start the server, follow these steps:
- Go to the `Server` directory.
- Open a terminal.
- Type the following command to run the server:
  ```bash
  python Serv.py
  ```

## Starting the Client GUI
To launch the graphical user interface for the client:
- Go to the `App_Gui/Python_file` directory.
- Open a terminal.
- Type the following command to run the client GUI:
  ```bash
  python NXsend.py
  ```

## Purging SQL Tables
If you want to purge the SQL tables to start from a clean database, here's what you need to do:

- **For the Server**:
  - Go to the `Server` directory.
  - Open a terminal.
  - Type the following command to run the script that purges the server's database:
    ```bash
    python Database_client.py
    ```

- **For the Client**:
  - Go to `App_Gui/Python_file`.
  - Open a terminal.
  - Type the following command to purge the client's database:
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

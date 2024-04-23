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
- You must first modify the IP and the port in `Serv.py` and `Database.py` so that it corresponds to the IP of the machine used as well as a free port (otherwise an error will occur).

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

# Client configuration
To configure the client for this project, you will need to follow a few essential steps. This section will guide you through the process of setting up the client through to creating a conversation.

## Adding a server
After launching the client, you will see an interface like this :
![Image de démonstration]()

Press the ```settings``` button and you will see this window appear :
![Image de démonstration]()

Enter your username, the IP address and the port you configured in Serv.py and Database.py then Apply.

![Image de démonstration]()

## create a conversation

Now you will press the other add user button and you should get this window:

Enter the name you wish to assign as well as the IP of the person with whom you wish to communicate.

The new user is now added on the right side of the screen, tap on it to start a chat session.
*You are now ready to use the application*

# License

Specify the license under which your project is distributed. If using a popular license (like MIT, Apache, or GPL), provide a brief summary and a link to the full text.

```text
This project is licensed under the MIT License - see the LICENSE file for details.
```

# Authors

List the project's authors and contributors. You can link to their GitHub profiles or personal websites.

- [Nikxo](https://github.com/nikxo)
- [Vegasword](https://github.com/vegasword)

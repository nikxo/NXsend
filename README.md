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

# Client Configuration
To configure the client for this project, follow these steps to set up the client and start a conversation.

## Adding a Server
After launching the client, you will see an interface like this:

![Demo Image]()

1. Press the `Settings` button to open the settings window. It should look like this:

   ![Settings Window Image]()

2. Enter your username, the server's IP address, and the port you configured in `Serv.py` and `Database.py`.

3. Click `Apply` to save the settings.

## Creating a Conversation
To create a conversation, follow these steps:

1. Click the `Add User` button to open the user addition window:

   ![Add User Window Image]()

2. Enter the desired username and the IP address of the person you want to communicate with.

3. Once the user is added, you will see them on the right side of the screen. Click on the username to start a chat session.

   ![Chat Session Image]()

With these steps, you should be ready to use the application. Happy chatting!

# Important: Configuration Order

> ⚠️⚠️ **Critical Warning**: You must follow the configuration steps in the exact order. Begin by configuring the server, then proceed to add contacts.

**Do not skip or change the sequence** to avoid potential issues with communication and connectivity.

1. **Configure the Server**: Make sure to set up the server first, including entering the IP address and port.
2. **Add a Contact**: Once the server configuration is complete, you can add contacts in the client GUI.

Skipping the server configuration or adding contacts out of sequence can lead to errors and disrupt functionality. In the case of a bad configuration order, restart the server as well as the client



# License

Specify the license under which your project is distributed. If using a popular license (like MIT, Apache, or GPL), provide a brief summary and a link to the full text.

```text
This project is licensed under the MIT License - see the LICENSE file for details.
```

# Authors

List the project's authors and contributors. You can link to their GitHub profiles or personal websites.

- [Nikxo](https://github.com/nikxo)
- [Vegasword](https://github.com/vegasword)

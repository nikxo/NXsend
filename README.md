![Image de démonstration](https://raw.githubusercontent.com/nikxo/NXsend/main/File/NXsend_ban.jpg)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)
[![Python-3.10.0](https://img.shields.io/badge/Python-3.10.0-green:badgeContent)](https://www.python.org/downloads/release/python-3100/)
[![customtkinter-5.2.2](https://img.shields.io/badge/customtkinter-5.2.2-green:badgeContent)](https://github.com/TomSchimansky/CustomTkinter)
![GitHub stars](https://img.shields.io/github/stars/nikxo/Xeha)

# Description
Nxsend is a Python messaging application based on the TCP protocol. It aims to be a fast and secure messaging service, accessible to everyone, while remaining open source. Designed to meet varied needs, Nxsend seeks to provide a smooth and reliable user experience.

### Main Features
- **Real-Time Communication**: Nxsend uses the TCP protocol to ensure fast and efficient communication between users.
- **Security**: Data security is a priority. Nxsend implements robust security measures to protect user conversations.
- **Open Source**: As an open source project, Nxsend encourages community participation. Source code is available for developers to contribute, modify and improve the application.

### Objective
Nxsend's goal is to become a versatile and secure messaging tool that can be used by everyone. Thanks to its open source approach, it encourages innovation and collaboration between developers around the world.
### Current status
> ⚠️⚠️ currently, the function allowing the management of private and public keys allowing the encryption of communications is not implemented. This version is a prototype for a more advanced version in C language. Please do not use it as a secure messaging service in the current state of affairs.
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

![Demo Image](https://raw.githubusercontent.com/nikxo/NXsend/main/File/Demo.png)

1. Press the `Settings` button to open the settings window. It should look like this:

   ![Settings Window Image](https://raw.githubusercontent.com/nikxo/NXsend/main/File/settings.png)

2. Enter your username, the server's IP address, and the port you configured in `Serv.py` and `Database.py`.

3. Click `Apply` to save the settings.

## Creating a Conversation
To create a conversation, follow these steps:

1. Click the `Add User` button to open the user addition window:

   ![Add User Window Image](https://raw.githubusercontent.com/nikxo/NXsend/main/File/contact.png)

2. Enter the desired username and the IP address of the person you want to communicate with.

3. Once the user is added, you will see them on the right side of the screen. Click on the username to start a chat session.

   ![Chat Session Image](https://raw.githubusercontent.com/nikxo/NXsend/main/File/user.png)

With these steps, you should be ready to use the application. Happy chatting!

# Important: Configuration Order

> ⚠️⚠️ **Critical Warning**: You must follow the configuration steps in the exact order. Begin by configuring the server, then proceed to add contacts.

**Do not skip or change the sequence** to avoid potential issues with communication and connectivity.

1. **Configure the Server**: Make sure to set up the server first, including entering the IP address and port.
2. **Add a Contact**: Once the server configuration is complete, you can add contacts in the client GUI.

Skipping the server configuration or adding contacts out of sequence can lead to errors and disrupt functionality. In the case of a bad configuration order, restart the server as well as the client.



## Licence
This project is distributed under the Creative Commons Attribution-NonCommercial 4.0 International license (CC BY-NC 4.0). This license allows users to copy, distribute, and remix your work as long as they give you credit as the creator. However, it prohibits commercial use.

### Main Features of the CC BY-NC 4.0 License
- **Attribution (BY)**: Users should give credit to the original creator when using your work.
- **Non-Commercial Use (NC)**: Users may not use the content for commercial purposes or to obtain financial advantage.

You can see [the full text of the CC BY-NC 4.0 license](https://creativecommons.org/licenses/by-nc/4.0/) for more details.

Please ensure that any use, distribution, or modification of this project complies with the terms of this license. For any questions regarding rights and restrictions, please see the link above or contact an intellectual property expert.

# Automatic_Data_Collection_System

A Python-based asynchronous tool for collecting public Telegram channel data (messages and metadata) and exporting it to structured JSON files for analysis, research, or archiving.<br>
This project is designed to be modular, configurable, and easy to extend, making it suitable for learning async Python, working with the Telegram API, and building data pipelines. 

![Process_of_program](./Flowchart.png)

📌 Features

Collect messages from public Telegram channels

Asynchronous execution using asyncio

Uses Telegram client library (e.g. Telethon)

Export data to JSON files

Configurable message limits per channel

Clean project structure with clear entry point

Designed for scalability (single channel → multi-channel)

⚙️ Requirements
Before Using This Program (For Normal Users)

To run this program successfully, please make sure you meet all the following requirements.

1️⃣ Telegram Account

A valid Telegram account

The account must be active and able to receive login codes

The program will log in using your Telegram account via the official Telegram API.

2️⃣ Telegram API Credentials

You must obtain your own API credentials:

API_ID

API_HASH

How to get them:

Visit https://my.telegram.org

Log in with your Telegram account

Go to API development tools

Create an application

Copy your API_ID and API_HASH

⚠️ Do not share these credentials publicly.

3️⃣ Public Telegram Channel

Only public Telegram channels are supported

You must have:

Channel username (e.g. @example_channel)

OR public channel link

❌ Private channels and groups are not supported unless you are a member and explicitly modify the code.

4️⃣ System Requirements

Operating System:

Windows 10+

Linux (recommended)

macOS

Python:

Python 3.9 or higher

5️⃣ Python Dependencies

Required libraries:

telethon
asyncio

-pip install telethon 

Reference:https://my.telegram.org/apps

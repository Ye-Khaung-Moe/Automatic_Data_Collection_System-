from collector import channel_collector,client

Description = """
 If you are using this program for first time we are strongly 
 recommand to copy the channel link in here.

 This program is designed for export message from any telegram channel which
 is running as public 

 How to use program
 ------------------
 1. Copy and paste the channel link 
 2. Type 'yes' for process
"""

print(Description)

channel = input("Enter Telegram channel link or username:").strip()

confirm = input("Type Yes to start collection:").strip().lower()
if confirm != 'yes':
    print("Program Cancel")
    exit()

with client: 
    client.loop.run_until_complete(channel_collector(channel))
# WhatsApp Message Sender

This Python script utilizes the `pywhatkit` library to automate sending messages on WhatsApp. It provides options to send messages to individual contacts and groups at specified times.

## Features:

### 1. Send Message to a Person:
   - Enter the recipient's phone number.
   - Input the message you want to send.
   - Set the desired hour and minute for sending the message.
   - Optionally, specify a wait time before sending, print the wait time, and choose whether to open tabs.

### 2. Send Message to a Group:
   - Enter the name of the WhatsApp group.
   - Input the message you want to send.
   - Set the desired hour and minute for sending the group message.

## Usage Instructions:

1. Run the script using a Python interpreter.

2. Choose an option:
   - **Option 1:** Send a message to a person.
   - **Option 2:** Send a message to a group.

3. Follow the prompts to provide the necessary information:
   - Phone number (for individuals) or group name (for groups).
   - Message content.
   - Hour and minute for sending the message.
   - Optionally, specify wait time, print wait time, and tab open (for individuals).

4. The script will attempt to send the message at the specified time, and any errors encountered will be displayed.

**Note:**
- Ensure you have the `pywhatkit` library installed (`pip install pywhatkit`).
- Make sure to have a valid WhatsApp session open in your browser before running the script.
- Be cautious about automating messaging and comply with WhatsApp's terms of service.

Feel free to customize the script according to your needs. Use responsibly and consider privacy and ethical considerations while automating messaging tasks.
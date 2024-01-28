import pywhatkit


def send_message_to_person():
    phone_number = input("Enter phone number: ")
    message = input("Enter message: ")
    hour = int(input("Enter hour: "))
    minute = int(input("Enter minute: "))
    wait_time = int(input("Enter wait time (optional): ") or 0)
    print_wait_time = bool(input("Print wait time? (optional): ") or False)
    tab_open = int(input("Enter tab open (optional): ") or 0)

    try:
        pywhatkit.sendwhatmsg(phone_number, message, hour, minute, wait_time, print_wait_time, tab_open)
    except Exception as e:
        print("An error occurred:", str(e))

def send_message_to_group():
    group_name = input("Enter group name: ")

    try:
        pywhatkit.sendwhatmsg_to_group(group_name, message, hour, minute)
    except Exception as e:
        print("An error occurred:", str(e))

option = input("Choose an option:\n1. Send message to a person\n2. Send message to a group\n")

if option == "1":
    send_message_to_person()
elif option == "2":
    send_message_to_group()
else:
    print("Invalid option")


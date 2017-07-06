
from frnds import NewSpy, friends
from chat import Msg
#Steganography is used for sending and receiving secret messages.
from steganography.steganography import Steganography
#Termcolor is used for printing statements using different colors.
from termcolor import colored
#Time taken to send and receive secret message
from datetime import datetime


spy_status ="What's up !!!"

STATUS_MESSAGES = ["What's up !!1", "Busy","Available","Whatsap only"]
spy=NewSpy("Abhilasha","Ms.",21,4.5)



print colored ('Hey! Let\'s Get Started','red')

question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

# function to add Status message
def add_status():

    if spy.current_status_message != None:
        print colored('Your current status message is %s \n', 'blue') % (spy.current_status_message)
    else:
        print colored('Currently you don\'t have any status message ', 'blue')
    default = raw_input("Do you wanna select from your old status (y/n)? ")
    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")
        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message) #Add new status message to the list of status message.
            updated_status_message = new_status_message
    if default.upper() == 'Y':
        item_pos = 1
        for e in STATUS_MESSAGES:
           print str(item_pos) + ". " + e
           item_pos = item_pos + 1
        status_choice = raw_input("Which status do you want to set")
        if int(status_choice) > len(STATUS_MESSAGES):
            print colored('There is an error', 'blue')
        if len(STATUS_MESSAGES) >= int(status_choice):
           updated_status_message = STATUS_MESSAGES[int(status_choice) - 1]
           print colored('Your status Message is:%s', 'blue') % (updated_status_message)
    return updated_status_message

# function to add friend
def add_friend():
    name = raw_input(" Add your friend's name please: ")
    salutation = raw_input("Are they Mr. or Ms.?: ")
    age = int(raw_input("Age?"))
    rating = float(raw_input("Spy rating?"))


    if len(name) > 0 and age > 12 and  rating  >= spy.rating:
        new_friend=NewSpy(name,salutation,age,rating)
        friends.append(new_friend)# Add new friend to the list of friends.
        print colored('New friends are added!', 'blue')

    else:
        print colored('Sorry!! There is an Invalid entry. ', 'blue')
    return len(friends)

#function for selecting our friend
def select_friend():
    item_number = 0
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number + 1, friend.name,
                                                             friend.age,
                                                             friend.rating)
        item_number = item_number + 1
    friend_choice = raw_input("Choose from your friends")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position

#function to send a secret message
def send_message():

    friend_choice = select_friend()
    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)
    new_chat = Msg(text,True)
    friends[friend_choice].chats.append(new_chat)


    print colored('Your secret message image is ready!.', 'blue')

#function to read a secret message
def read_message():

    sender = select_friend()
    output_path = raw_input("What is the name of the file?")
    secret_text = Steganography.decode(output_path)
    new_chat = Msg(secret_text,False)
    friends[sender].chats.append(new_chat)


    print colored('Your secret message has been saved!', 'blue')

#function to display chat history
def chat_history():
    read_for = select_friend()

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (
            chat.time.strftime(colored('%d %B %Y', 'blue')), colored('You said:', 'red'), chat.message)
        else:
            print '[%s] %s said: %s' % (chat.time.strftime(colored('%d %B %Y', 'blue')), colored(friends[read_for].name, 'red'), chat.message)

#function to receive average no of words.
def average_words():
    sentence = raw_input('Enter the sentence:')
    Sum =0
    for ch in sentence.split():
        character = len(ch)
        Sum = Sum + character
    average = (Sum)/(len(sentence.split()))
    print (average)

# function for spy menu
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name

    if spy.age > 12 and spy.age < 50:

        print colored('Authentication complete. Welcome ', 'green') + spy.name + colored(' age:', 'green') + str(
            spy.age) + colored(' and rating of:', 'green') + str(
            spy.rating) + colored(' Proud to have you onboard', 'green')

        show_menu = True
        # menu containing different choices
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3.Send secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Average of words \n 7. Close Application \n"
            menu_choice = raw_input(menu_choices)
            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print colored('You have %d friends', 'blue') % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    chat_history()
                elif menu_choice == 6:
                    average_words()
                elif menu_choice == 7:
                    print 'THANK YOU!'
                    break
                else:
                    show_menu = False
    else:
        print colored('Sorry your age is not appropriate to be a spy', 'blue')


if existing == "Y":
    start_chat(spy)
else:
    name = raw_input("Welcome to spy chat. To continue further you must tell me your spy name first: ")

    if len(name) > 0:
        salutation = raw_input("Should I call you (Mr. or Ms.)?: ")
        age = int(raw_input("What is your age?"))
        rating = float(raw_input("What is your spy rating?"))
        spy=NewSpy(name,salutation,age,rating)
        start_chat(spy)
    else:
        print colored('Please Enter a valid spy name', 'blue')
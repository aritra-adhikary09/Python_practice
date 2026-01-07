'''Concept: Object-Oriented Programming (OOP)

Q10. Mini Project – OOP Chat System

Create a Chat System using Object-Oriented Programming concepts.
You must create the following classes:

User

Message

ChatRoom

The system should support the following functionalities:

Sending messages

Viewing chat history

Users joining the chat room

Users leaving the chat room'''

# User class
class User:
    def __init__(self, username):
        self.username = username


# Message class
class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def display(self):
        print(f"{self.sender.username}: {self.content}")


# ChatRoom class
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join(self, user):
        self.users.append(user)
        print(f"{user.username} joined the chat.")

    def leave(self, user):
        self.users.remove(user)
        print(f"{user.username} left the chat.")

    def send_message(self, sender, content):
        if sender in self.users:
            message = Message(sender, content)
            self.messages.append(message)
        else:
            print("User is not in the chat room.")

    def show_chat_history(self):
        print("\nChat History:")
        for message in self.messages:
            message.display()


# Testing the chat system
user1 = User("Aritra")
user2 = User("Rahul")

chat = ChatRoom("Python Chat Room")

chat.join(user1)
chat.join(user2)

chat.send_message(user1, "Hello everyone!")
chat.send_message(user2, "Hi Aritra!")

chat.show_chat_history()

chat.leave(user2)

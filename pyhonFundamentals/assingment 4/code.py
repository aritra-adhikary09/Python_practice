# -------------------------------
# Message Class
# -------------------------------
class Message:
    message_counter = 1  # simple counter

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# -------------------------------
# User Class
# -------------------------------
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# -------------------------------
# ChatRoom Class
# -------------------------------
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)


# ---------------------------------------
# Example Usage
# ---------------------------------------
if __name__ == "__main__":
    room = ChatRoom("Python Lounge")

    u1 = User("Alice")
    u2 = User("Bob")
    u3 = User("Charlie")

    u1.join_chatroom(room)
    u2.join_chatroom(room)

    u1.send_message("Hello everyone!")
    u2.send_message("Hi Alice!")

    u3.join_chatroom(room)
    u3.send_message("Hey guys, what's up?")

    room.show_chat_history()

    u1.leave_chatroom()
    u2.leave_chatroom()
    u3.leave_chatroom()




'''class User:
    def __init__(self,UserName):
        self.username = UserName

class Message:
    def __init__(self,sender,content):
        self.sender = sender
        self.content = content
    def display(self):
        print(f"{self.sender.username}:{self.content}")
    

class Chatroom:
    def __init__(self,room_name):
        self.room_name = room_name 
        self.users = []   
        self.messages = []
    
    def join(self,user):
        self.user.append(user)
        print(f"{user.username} joined the chat.")
    
    def leave(self, user):
        self.user.remove(user)
        print(f"{user.username} Joined the chat.")
    
    def send_message(self,sender,content):
        if sender in self.users:
            message = Message(sender,content)
            self.messages.append(message)
        else:
            print("User is not in the chat room.")

    def show_chat_history(self):
        print("\nChat History:")
        for message in self.messages:
            message.display()

user1 = User("Aritra")
user2 = User("Rohan")

chat = Chatroom("Python Chat Room")

chat.join(user1)
chat.join(user2)

chat.send_message(user1,"Hello everyone!")
chat.send_message(user2,"Hi Aritra!")

chat.show_chat_history()

chat.leave(user2)'''
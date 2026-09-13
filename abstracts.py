from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod #
#     def start(self):
#         pass #null-will not do anything

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting")

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotification(Notification):
    def send(self, message):
        print(f"Sending email: {message}")
        
class SMSNotification(Notification):
    def send(self, message):
        print(f"Sending SMS: {message}")

email = EmailNotification()
sms = SMSNotification()
email.send("Your order has been shipped!")
sms.send("Your OTP is 123456!")
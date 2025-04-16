from abc import ABC, abstractmethod


class Notification(ABC):
    @abstractmethod
    def notify(self, message): pass

class EmailNotification(Notification):
    def notify(self, message): print(f"Email: {message}")

class SMSNotification(Notification):
    def notify(self, message): print(f"SMS: {message}")


class NotificationManager(ABC):
    @abstractmethod
    def create_notification(self) -> Notification: pass

    def send_notification(self, message):
        notification = self.create_notification()
        notification.notify(message)

class EmailNotificationManager(NotificationManager):
    def create_notification(self) -> Notification:
        return EmailNotification()

class SMSNotificationManager(NotificationManager):
    def create_notification(self) -> Notification:
        return SMSNotification()


# Test code
def send_unknown_notification(manager: NotificationManager, message: str) -> None:
    # The function can be called with any NotificationManager
    # and will send the notification using the appropriate method.
    manager.send_notification(message)

if __name__ == "__main__":
    # Calling the test function with EmailNotificationManager
    email_manager = EmailNotificationManager()
    send_unknown_notification(email_manager, "Hello via Email!")

    # Calling the test function with SMSNotificationManager
    sms_manager = SMSNotificationManager()
    send_unknown_notification(sms_manager, "Hello via SMS!")

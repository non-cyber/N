class Notification:
    def __init__(self,message,recipient):
        self._message=message
        self._recipient=recipient

    def message(self):
        return self._message
    def recipient(self):
        return self._recipient
class NotificationManager:
    _notifications_sent=0
    def __init__(self, notification_type, notification_time):
        self._notification_type = notification_type
        self._notification_time = notification_time

    def notification_type(self):
        return self._notification_type

    def notification_time(self):
        return self._notification_time

    def notification_time(self,new_time):
        self._notification_time=new_time
    def send_notification(self,notification):
        notification.recipient.receve_notification(notification)
        NotificationManager._increment_notifications_sent()
        print(f"Notification type: {self._notification_type}, Notification time: {self._notification_time}")

    @classmethod
    def _increment_notifications_sent(cls):
        cls._notifications_sent += 1

    @classmethod
    def get_notifications_count(cls):
        return cls._notifications_sent

class Student:
    def __init__(self,student_id,name):
        self.student_id=student_id
        self.name=name

    def receive_notification(self,notification):
        print(f"name for {self.name}received a notification {notification.message}")


notification_manager1=NotificationManager("Lecture","10:30 AM")
notification_manager2=NotificationManager("Exam","9:00 AM")
student1=Student(21,"Noor")
student2=Student(10,"Fatima")
notification1=Notification("The Lecture has been postponed to 11:00 AM", student1)
notification2=Notification("The Lecture has been postponed to 11:00 AM",student2)
notification_manager1.send_notification(notification1)
notification_manager2.send_notification(notification2)
print(f"total :{NotificationManager.get_notifications_count()}")
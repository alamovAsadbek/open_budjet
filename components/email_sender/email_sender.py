import contextlib
import smtplib

from main_files.decorator.decorator_func import log_decorator


class EmailSender:
    def __init__(self):
        self.smtp_server = 'smtp.gmail.com'
        self.port = 587
        self.sender_email = 'alamovasad@gmail.com'
        self.password = 'fghr vfgj fcjx zqpj'

    @log_decorator
    @contextlib.contextmanager
    def connect_email(self):
        server = smtplib.SMTP(self.smtp_server, self.port)
        server.starttls()
        server.login(self.sender_email, self.password)
        yield server
        server.quit()

    @log_decorator
    def send_email(self):
        pass

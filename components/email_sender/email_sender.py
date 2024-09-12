import contextlib

from main_files.decorator.decorator_func import log_decorator


class EmailSender:
    def __init__(self):
        pass

    @log_decorator
    @contextlib.contextmanager
    def connect_email(self):
        pass

    @log_decorator
    def send_email(self):
        pass

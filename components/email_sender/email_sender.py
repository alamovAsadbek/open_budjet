from main_files.decorator.decorator_func import log_decorator


class EmailSender:
    @log_decorator
    def send_email(self):
        pass

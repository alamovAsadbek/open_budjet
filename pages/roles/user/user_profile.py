import hashlib

from components.color_text.color_text import color_text
from main_files.database.db_setting import get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserProfile:
    def __init__(self):
        self.__active_user = get_active_user()

    @log_decorator
    def show_profile(self) -> bool:
        print(self.__active_user)
        while True:
            update_check = input('Do you want to update your profile (y/n): ').strip().lower()
            if update_check == 'y':
                self.update_profile()
            elif update_check == 'n':
                break
            else:
                print(color_text('Wrong input', 'yellow'))
        return True

    @log_decorator
    def update_profile(self) -> bool:
        password: str = hashlib.sha256(input("Enter new password: ").strip().encode('utf-8')).hexdigest()
        confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        while password != confirm_password:
            print(color_text('Passwords do not match!', 'red'))
            password: str = hashlib.sha256(input("Enter new password: ").strip().encode('utf-8')).hexdigest()
            confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        return True

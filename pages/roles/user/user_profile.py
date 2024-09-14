import hashlib

from components.color_text.color_text import color_text
from main_files.database.db_setting import get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserProfile:
    @log_decorator
    def show_profile(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        active_user = get_active_user()
        print(f"\n{color_text('First name: ', 'blue')}{active_user['first_name']}\n"
              f"{color_text('Last name: ', 'blue')}{active_user['last_name']}\n"
              f"{color_text('Email: ', 'blue')}{active_user['email']}\n"
              f"{color_text('Registered: ', 'blue')}{active_user['created_at']}\n")
        while True:
            update_check = input('Do you want to update your profile (y/n): ').strip().lower()
            if update_check == 'y':
                print(color_text('Profile update', 'magenta'))
                self.update_profile()

            elif update_check == 'n':
                print(color_text('Exit', 'magenta'))
            else:
                print(color_text('Wrong input', 'yellow'))
                continue
            break
        return True

    @log_decorator
    def update_profile(self) -> bool:
        password: str = hashlib.sha256(input("Enter new password: ").strip().encode('utf-8')).hexdigest()
        confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        while password != confirm_password:
            print(color_text('Passwords do not match!', 'red'))
            password: str = hashlib.sha256(input("Enter new password: ").strip().encode('utf-8')).hexdigest()
            confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        print(color_text('Profile updated', 'green'))
        return True

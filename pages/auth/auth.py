import hashlib
import threading
import time

from components.color_text.color_text import color_text
from components.email_sender.email_sender import EmailSender
from components.random_password.generate_password import generate_password
from components.tables.tables import Tables
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__tables = Tables()
        self.__confirm_time = 0
        self.__admin_email = 'alamovasad@gmail.com'
        self.__email_sender = EmailSender()

    @log_decorator
    def create_tables(self) -> bool:
        self.__tables.create_users_table()
        threading.Thread(target=self.__tables.create_categories_table).start()
        return True

    @log_decorator
    def count_time(self) -> bool:
        for i in range(30):
            time.sleep(1)
            self.__confirm_time += 1
        return True

    @log_decorator
    def login(self) -> bool:
        pass

    @log_decorator
    def logout(self) -> bool:
        self.create_tables()
        query = '''
               UPDATE users SET is_login=FALSE;
        '''
        execute_query(query)
        return True

    @log_decorator
    def check_email(self, email: str) -> bool:
        query = '''
        SELECT * FROM USERS WHERE email=%s;
        '''
        result = execute_query(query, (email,))
        if result is None:
            return False
        return True

    @log_decorator
    def register(self) -> bool:
        first_name: str = input('First name: ').strip()
        last_name: str = input('Last name: ').strip()
        email: str = input('Email: ').strip()
        if email == self.__admin_email:
            print("This email is already registered.")
            return False
        password: str = hashlib.sha256(input('Password: ').encode('utf-8')).hexdigest()
        confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        while password != confirm_password:
            print(color_text('Passwords do not match!', color='red', is_bold=True))
            password: str = hashlib.sha256(input('Password: ').encode('utf-8')).hexdigest()
            confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        print(f"\n{color_text(text='Confirm email: ', color='blue')}{email}\n")
        print("You will have 30 seconds to confirm your email")
        threading.Thread(target=self.count_time).start()
        code = generate_password()
        email_subject = 'Confirm your email'
        email_body = f"Your password: {code}"
        threading.Thread(target=self.__email_sender.send_email, args=(email_subject, email_body, email)).start()
        number_of_attempts: int = 0
        while True:
            confirm_code: int = int(input("Confirm code: "))
            if number_of_attempts > 2:
                print(color_text("You have reached the maximum number of attempts. Please try again.", color='red',
                                 is_bold=True))
                return False
            elif self.__confirm_time >= 30:
                print(color_text("Time is over. Please try again.", color='red', is_bold=True))
                return False
            print(f"Number of attempts: {number_of_attempts + 1}")
            if confirm_code == code:
                print(color_text('Confirm email', color='green', is_bold=True))
                break
            else:
                print("Wrong code")
                number_of_attempts += 1
        query = '''
        INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s);
        '''
        params = (first_name, last_name, email, password)
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(color_text("Registered successfully", color='green', is_bold=True))
        return True

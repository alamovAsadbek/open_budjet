from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth


@log_decorator
def auth_menu():
    text = '''
1. Register
2. Login
3. Logout
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            auth.register()
        elif user_input == 2:
            auth.login()
        elif user_input == 3:
            auth.logout()
        else:
            print("Wrong input")
        auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


if __name__ == '__main__':
    print("Waiting...")
    auth = Auth()
    auth.logout()
    auth_menu()

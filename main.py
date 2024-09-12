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
            result_login = auth.login()
            if not result_login['is_login']:
                auth_menu()
            elif result_login['role'] == 'admin':
                admin_menu()
            elif result_login['role'] == 'user':
                user_menu()
            else:
                print("Login failed")
                auth_menu()
        elif user_input == 3:
            print("Waiting...")
            auth.logout()
            return
        else:
            print("Wrong input")
        auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        auth_menu()


@log_decorator
def user_menu():
    text = '''
1. Send a request
2. Season
3. Profile
4. Exit
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            pass
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            print("Exit")
            print("Waiting...")
            auth.logout()
            auth_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_menu()


@log_decorator
def admin_menu():
    text = '''
1. Statistics
2. Appeals
3. Season
4. Categories
5. Users
6. Logout
    '''
    print(text)
    try:
        pass
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


if __name__ == '__main__':
    print("Waiting...")
    auth = Auth()
    auth.logout()
    auth_menu()

from main_files.decorator.decorator_func import log_decorator
from pages.auth.auth import Auth
from pages.roles.admin.admin import Admin


@log_decorator
def auth_menu():
    text = '''
1. Register
2. Login
3. Exit
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
1. Appeal
2. Season
3. Profile
4. Exit
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            user_appeal_menu()
        elif user_input == 2:
            user_season_menu()
        elif user_input == 3:
            user.my_profile()
        elif user_input == 4:
            print("Exit")
            print("Waiting...")
            auth.logout()
            auth_menu()
        else:
            print("Wrong input")
        user_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_menu()


@log_decorator
def user_season_menu():
    text = '''
1. Voting
2. Statistics
3. My votes
4. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            user.voting_appeal()
        elif user_input == 2:
            pass
        elif user_input == 3:
            pass
        elif user_input == 4:
            user_menu()
        else:
            print('Wrong input')
        user_season_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_season_menu()


@log_decorator
def user_appeal_menu():
    text = '''
1. Send appeal
2. My request
3. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            user.send_request()
        elif user_input == 2:
            user.my_request()
        elif user_input == 3:
            user_menu()
        else:
            print('Wrong input')
        user_appeal_menu()
    except Exception as e:
        print(f'Error: {e}')
        user_appeal_menu()


@log_decorator
def admin_menu():
    text = '''
1. Appeals
2. Season
3. Categories
4. Users
5. Logout
    '''
    print(text)
    try:
        admin_input: int = int(input("Choose menu: ").strip())
        if admin_input == 1:
            admin_appeals_menu()
        elif admin_input == 2:
            admin_seasons_menu()
        elif admin_input == 3:
            admin_categories_menu()
        elif admin_input == 4:
            admin_users_menu()
        elif admin_input == 5:
            print("Exit")
            auth_menu()
        else:
            print("Wrong input")
        admin_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_menu()


@log_decorator
def admin_appeals_menu():
    text = '''
1. Rejecting appeals
2. Approved appeals
3. Accepting applications
4. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            admin.rejecting_appeals()
        elif user_input == 2:
            admin.approved_appeals()
        elif user_input == 3:
            admin.accepting_application()
        elif user_input == 4:
            admin_menu()
        else:
            print("Wrong input")
        admin_appeals_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_appeals_menu()


@log_decorator
def admin_seasons_menu():
    text = '''
1. Create new season
2. Update existing season's status
3. Statistics
4. Show all seasons
5. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            admin.create_new_season()
        elif user_input == 2:
            admin.update_season_status()
        elif user_input == 3:
            pass
        elif user_input == 4:
            admin.show_all_seasons()
        elif user_input == 5:
            admin_menu()
        else:
            print("Wrong input")
        admin_seasons_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_seasons_menu()


@log_decorator
def admin_categories_menu():
    print("Waiting...")
    admin = Admin()
    text = '''
1. Create new categories
2. Update existing categories
3. Delete existing categories
4. Show existing categories
5. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            admin.create_new_category()
        elif user_input == 2:
            admin.update_category()
        elif user_input == 3:
            admin.delete_category()
        elif user_input == 4:
            admin.show_all_categories()
        elif user_input == 5:
            admin_menu()
        else:
            print("Wrong input")
        admin_categories_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_categories_menu()


@log_decorator
def admin_users_menu():
    print("Waiting...")
    admin = Admin()
    text = '''
1. Update existing users
2. Delete existing users
3. Show existing users
4. Back
    '''
    print(text)
    try:
        user_input: int = int(input("Choose menu: ").strip())
        if user_input == 1:
            admin.update_users()
        elif user_input == 2:
            pass
        elif user_input == 3:
            admin.show_all_users()
        elif user_input == 4:
            admin_menu()
        else:
            print("Wrong input")
        admin_users_menu()
    except Exception as e:
        print(f'Error: {e}')
        admin_users_menu()


if __name__ == '__main__':
    print("Waiting...")
    auth = Auth()
    auth.logout()
    # admin = Admin()
    # user = User()
    auth_menu()

from main_files.decorator.decorator_func import log_decorator


class UserSeason:
    @log_decorator
    def get_active_appeal(self):
        pass

    @log_decorator
    def voting_user(self):
        pass

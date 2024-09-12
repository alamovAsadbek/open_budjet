from main_files.decorator.decorator_func import log_decorator


class AdminSeasonsPageAdmin:
    @log_decorator
    def check_seasons(self):
        pass

    @log_decorator
    def get_categories(self):
        pass

    @log_decorator
    def create_seasons(self):
        pass

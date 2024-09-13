from main_files.decorator.decorator_func import log_decorator


class AdminAppealsPageAdmin:
    @log_decorator
    def get_appeals(self):
        query='''
        select a.id          as a_id,
           a.name        as a_name,
           a.description as a_description,
           a.price       as a_price,
           c.name        as category_name,
           r.name        as region_name,
           d.name        as destricts_name,
           s.name        as season_name,
           s.status      as season_status,
           s.created_at  as season_created,
           u.first_name     as u_first_name,
           u.last_name     as u_last_name,
           u.email         as u_email
        FROM appeals a
                 inner join categories c on c.ID = a.CATEGORY_ID
                 inner join districts d on a.DISTRICTS_ID = d.ID
                 inner join regions r on d.REGION_ID = r.ID
                 inner join SEASONS S on S.ID = a.SEASONS_ID
                 inner join users u on u.ID = a.USER_ID
        '''

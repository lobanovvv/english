from ..models import Countries

class DB_Reader:
    '''Класс чтения данных из бд'''
    
    def get_all_filtered_rows(filter):
        return list(Countries.objects.filter(**filter))

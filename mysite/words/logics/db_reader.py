from ..models import Countries

class DB_Reader:
    '''Класс чтения данных из бд'''
    
    def get_all_filtered_rows(filter):
        """Возвращает все объекты из бд по заданному фильтру"""
        return list(Countries.objects.filter(**filter))

    def get_all_answers(answers_column):
        """Возвращает список с ответами"""
        raw = list(Countries.objects.values(answers_column))
        only_aswers_name = []
        for i in raw:
            only_aswers_name.append(i.get(answers_column))
        return only_aswers_name
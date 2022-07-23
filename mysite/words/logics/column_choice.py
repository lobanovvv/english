import random

from .db_reader import DB_Reader

class ColumnChoice:

    def __init__(self, base_column_name, answer_column_name, filter) -> None:
        '''
        Класс для формирования данных по выбору

        param: int base_col: Имя колонки в которой находится база по которой будет
        формироваться запрос
        param: int answer_col: Имя колонка по которой будет формироваться ответы
        param: int filters: Словарь с фильтрами для выбора определенного типа колонок
        '''
        self.base_column_name = base_column_name
        self.answer_column_name = answer_column_name

        remained_rows = DB_Reader.get_all_filtered_rows(filter=filter)
        # count_of_all_rows = rows_left = len(remained_rows)
        # current_row = remained_rows.pop(random.randrange(rows_left))
        # print('hello')
        # print(current_row)
        # correct_answer = current_row.nationalities


    def get_current_base_item(self):
        '''Возвращает название страны, основываясь на base_col'''
        pass
    
    
    def get_shuffled_answers(self):
        '''Возвращает четыре перемешанных ответа'''
        pass
    
    
    def get_number_of_remained_rows(self):
        '''Возвращает количество оставшихся вопросов'''
        pass

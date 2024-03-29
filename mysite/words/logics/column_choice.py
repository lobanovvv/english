import random
from .audio import Audio

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

        self.remained_rows = DB_Reader.get_all_filtered_rows(filter=filter)
        self.count_of_all_rows = self.rows_left = len(self.remained_rows)
        self.extract_current_row()
        self.get_correct_answer()
        self.all_answers = DB_Reader.get_all_answers(answers_column = answer_column_name)
        self.four_answers = []
        self.is_correct = None
        

    def get_correct_answer(self):
        self.correct_answer = getattr(self.current_row, self.answer_column_name)

    def extract_current_row(self):
        number_of_remained_rows = self.get_number_of_remained_rows()
        self.current_row = self.remained_rows.pop(random.randrange(number_of_remained_rows))

        Audio.create_sound(text = getattr(self.current_row, self.base_column_name), file_name='start_sound.mp3')

    def get_current_base_item(self):
        '''Возвращает название страны, основываясь на base_col'''
        return getattr(self.current_row, self.base_column_name)
    
    def get_shuffled_answers(self):
        '''Возвращает четыре перемешанных ответа'''
        self.get_correct_answer()
        self.four_answers = []
        self.four_answers.append(self.correct_answer)

        rnd4Nums_from_allRows = random.sample(range(self.count_of_all_rows), 3)
        for num in rnd4Nums_from_allRows:
            self.four_answers.append(self.all_answers[num])
        random.shuffle(self.four_answers)
        
        return self.four_answers

    def get_number_of_remained_rows(self):
        '''Возвращает количество оставшихся вопросов'''
        return len(self.remained_rows)

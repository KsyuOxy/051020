from xml.dom import minidom


class XMLDriver(object):  # -> управляет данными файла '.xml'
    def __init__(self, path):
        self._doc = minidom.parse(path)

    def get_name(self):  # -> возвращает название тестов
        root = self._doc.getElementsByTagName('tests')[0]
        name = root.attributes['name'].value
        return name

    def get_difficulty(self):  # -> возвращает список, содержащий варианты сложности
        difficulty = self._doc.getElementsByTagName('test_difficulty')
        diff_list = []
        for i, diff in enumerate(difficulty):
            diff_list.append(diff.attributes["name"].value)
        return diff_list

    def get_tasks(self, test_difficulty: str):  # -> возвращает список заданий. Атрибут: test_difficulty-сложность
        tasks = []
        difficulty = self._doc.getElementsByTagName('test_difficulty')
        for diff in difficulty:
            if diff.attributes['name'].value == test_difficulty:
                task = diff.getElementsByTagName('task')  # + diff.attributes['text'].value
                for q in task:
                    result = f'{q.attributes["name"].value}. {q.attributes["question"].value}'
                    tasks.append(result)
        return tasks

    # -> возвращает список вариантов ответов одного задания. Атрибуты: test_difficulty-сложность, num_task-номер задания
    def get_answers_options_of_task(self, test_difficulty: str, num_task: str) -> list:
        block_answers = []  # -> будет хранить варианты ответов
        difficulty = self._doc.getElementsByTagName('test_difficulty')  # -> получает варианты сложности из файла
        for diff in difficulty:  # -> итерируется по сложности
            if diff.attributes['name'].value == test_difficulty:  # -> если находит совпадение
                task = diff.getElementsByTagName('task')  # -> получает из файла задания
                for t in task:  # -> итерируется по заданиям
                    if t.attributes['name'].value == num_task:  # -> в случае совпадения с параметром
                        answers = t.getElementsByTagName('answer')  # -> получ. из файла варианты ответов этого задания
                        for answ in answers:  # -> итерируется по ответам
                            block_answers.append(f'{answ.attributes["text"].value}')  # -> добавляет их в список
        return block_answers

    # -> возвращает список, содержащий списки вариантов ответов по каждому заданию отдельно
    def get_all_answers_options(self, test_difficulty: str) -> list:  # -> test_difficulty - сложность теста
        answers = []  # -> будет хранить варианты ответов
        difficulty = self._doc.getElementsByTagName('test_difficulty')  # -> получает варианты сложности из файла
        for diff in difficulty:  # -> итерируется по сложности
            if diff.attributes['name'].value == test_difficulty:  # -> если находит совпадение
                task = diff.getElementsByTagName('task')  # -> получает из файла задания
                for q in task:  # -> итерируется по заданиям
                    answers_get = q.getElementsByTagName('answer')  # -> в случае совпадения
                    block_answers_of_task = []  # -> созд.список для хранения вариантов ответов
                    for a in answers_get:  # -> итерируется по ответам
                        block_answers_of_task.append(f'{a.attributes["text"].value}')  # -> добавляет их в список
                    answers.append(block_answers_of_task)  # -> добавл.список вар.ответов для одного задания в список
        return answers

    def correct_answers(self, test_difficulty: str):  # -> получает список правильных ответов заданной сложности
        correct_answers_list = []  # -> будет хранить список правильных ответов
        difficulty = self._doc.getElementsByTagName('test_difficulty')  # -> получ варианты сложности
        for diff in difficulty:  # -> итерируется по сложности
            if diff.attributes['name'].value == test_difficulty:
                correct_answers = diff.getElementsByTagName('correct_answer')  # -> получает ответы
                for c in correct_answers:  # -> итерируется по ответам
                    result = f'{c.attributes["text"].value}'
                    correct_answers_list.append(result)
        return correct_answers_list


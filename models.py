from tkinter import *
from tkinter import messagebox


user_list = []  # -> список ответов пользователя


class CreateButton(Button):  # -> создаёт кнопку
    def __init__(self, command=False):
        super().__init__()
        self._command = command

    def create_button(self, font_size, butt_text, x, y):
        button = Button()
        button.config(font=('Comic Sans Ms', font_size), width=7, fg='Beige', bg='DarkSeaGreen', text=butt_text,
                      relief=RAISED, bd=3, command=self._command)
        button.place(x=x, y=y)


class CreateAnswerButton(Button):  # -> создаёт кнопку варианта ответа

    def __init__(self, butt_text):
        super().__init__()
        self._butt_text = butt_text

    def create_button(self, butt_text, x, y):

        def click():  # -> в случае нажатия на кнопку добавляет её текст в вписок пользователя
            if butt_text not in user_list:
                user_list.append(butt_text)
            else:  # -> если ответ дублируется предупреждение
                messagebox.showwarning('Внимание!', 'Такой ответ уже принят.')

        button = Button()
        button.config(font='Arial 9', width=40, bg='Beige', text=butt_text, command=click)
        button.place(x=x, y=y)

    def get_text_btt(self):
        return self._butt_text


class CreateTaskLabel(Label):  # -> создаёт Label для заданий
    def __init__(self):
        super().__init__()

    def create_label(self, lbl_text: str, x: int, y: int):
        lbl = Label()
        lbl.config(font=('Comic Sans Ms', 10), width=47, height=2, bg='DarkOliveGreen', text=lbl_text, fg='white')
        lbl.place(x=x, y=y)


class CreateLabel(Label):  # -> создаёт текстовый Label
    def __init__(self):
        super().__init__()

    def create_label(self, font_size: int, lbl_text: str, bg: str, fg: str, x: int, y: int):
        lbl = Label()
        lbl.config(font=('Comic Sans Ms', font_size), bg=bg, text=lbl_text, fg=fg)
        lbl.place(x=x, y=y)


class BlockAnswersOptions(CreateAnswerButton):  # -> создаёт блок из кнопок-варианты ответов (4шт) для одного задания
    def __init__(self, butt_text):
        super().__init__(butt_text)
        self._text = butt_text

    def create_block_ao(self, button: list, x: int, y: int) -> None:
        self.create_button(button[0], x, y)
        self.create_button(button[1], x, y + 30)
        self.create_button(button[2], x, y + 60)
        self.create_button(button[3], x, y + 90)


class BlockAnswersFive(BlockAnswersOptions):  # -> создаёт 5 блоков из кнопок-ответов(4шт) для всех(5) заданий
    def __init__(self, butt_text):
        super().__init__(butt_text)
        self._text = butt_text
        self._block = BlockAnswersOptions(self._text)

    def create_five_blocks_ao(self, list1: list, list2: list, list3: list, list4: list, list5: list, x: int, y: int):
        self._block.create_block_ao(list1, x=x, y=y)
        self._block.create_block_ao(list2, x=x, y=y + 175)
        self._block.create_block_ao(list3, x=x, y=y + 350)
        self._block.create_block_ao(list4, x=x + 430, y=y)
        self._block.create_block_ao(list5, x=x + 430, y=y + 175)


class BlockTasksLabels:  # -> создаёт блок всех заданий выбранной сложности
    def create_block_tasks_lbl(self, text1, text2, text3, text4, text5, x, y):
        lbl1 = CreateTaskLabel()
        lbl1.create_label(text1, x, y)
        lbl2 = CreateTaskLabel()
        lbl2.create_label(text2, x, y + 175)
        lbl3 = CreateTaskLabel()
        lbl3.create_label(text3, x, y + 350)
        lbl4 = CreateTaskLabel()
        lbl4.create_label(text4, x + 430, y)
        lbl5 = CreateTaskLabel()
        lbl5.create_label(text5, x + 430, y + 175)

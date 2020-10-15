from drivers import *
from models import *
from tkinter import *
from tkinter.ttk import Separator

# -> создание окна и его параметры
root = Tk()
root.geometry('900x680+200+100')
root.config(bg='Beige')

# -> декоративные элементы -----------------------------------------
color_lbl1 = Label()
color_lbl1.config(bg='DarkSeaGreen', width=130, height=7)
color_lbl1.place(x=0, y=0)

Separator(root, orient='horizontal').place(x=0, y=105, relwidth=20)
Separator(root, orient='horizontal').place(x=0, y=108, relwidth=20)

color_lbl1 = Label()
color_lbl1.config(bg='DarkSeaGreen', width=2, height=38)
color_lbl1.place(x=0, y=120)  # ------------------------------------

# -> создание заголовка тестов
title_txt = XMLDriver('data.xml').get_name()
title_lbl = CreateLabel().create_label(38, title_txt, 'DarkSeaGreen', 'DarkOliveGreen', 80, 18)

# -> создание Label 'choose difficulty:'
difficulty_lbl = CreateLabel().create_label(14, 'choose difficulty:', 'DarkSeaGreen', 'DarkOliveGreen', 478, 55)


# ----------------------------------------------------------------------------------------------------------------------
def check_result_easy():  # -> проверка результатов и вывод сообщения
    correct_answers = XMLDriver('data.xml').correct_answers('easy')  # -> получ.правильн.ответы сложности easy из файла
    color_lbl2 = Label()  # -> для вывода результата
    color_lbl2.config(bg='DarkSeaGreen', width=14, height=2, font=('Comic Sans Ms', 32),
                      fg='DarkOliveGreen')
    color_lbl2.place(x=480, y=522)

    # -> user_list - список ответов пользователя, correct_answers - список правильн.ответов из файла
    if user_list == correct_answers:         # -> сравнение списков на совпадение правильных ответов
        color_lbl2.config(text='Excelent!')

    elif len(user_list) < len(correct_answers):                          # -> сравнение длин списков
        messagebox.showwarning('Внимание!', 'Вы ответили не на все вопросы.')

    elif len(user_list) > len(correct_answers):                          # -> сравнение длин списков
        messagebox.showwarning('Внимание!', 'На какой-то вопрос Вы дали более одного ответа.')

    else:
        k = 0                   # -> будет хранит кол-во правильных ответов
        for i in user_list:     # -> ищет совпадение ответов в списках и выдаст сообщение, в зависимости от результата
            if i in correct_answers:
                k += 1
        if k == 4:
            color_lbl2.config(text='Good!')
        elif k == 3:
            color_lbl2.config(text='Not so bad!')
        elif k < 3:
            color_lbl2.config(text='Ohh..')


def easy_level():  # ---------------------------------------------------------------------------------------------------
    # -> сложность 'easy'
    # -> создание Labels вопросов теста
    text_tasks = XMLDriver('data.xml').get_tasks('easy')  # -> список текстов заданий из файла
    tasks_text_lbl = BlockTasksLabels()  # -> создание блока вопросов с заполнением текста из файла
    tasks_text_lbl.create_block_tasks_lbl(text_tasks[0], text_tasks[1], text_tasks[2], text_tasks[3], text_tasks[4], 50,
                                          120)

    # -> создание блоков вариантов ответа для каждого вопроса
    txt_all_answ = XMLDriver('data.xml').get_all_answers_options('easy')  # -> список вариантов ответов для кажд.задания
    answers_5 = BlockAnswersFive(txt_all_answ)  # -> создаёт блоки с вариантами ответов для каждого задания и вставляет
    answers_5.create_five_blocks_ao(txt_all_answ[0], txt_all_answ[1], txt_all_answ[2],  # -> в них текст вариантов из
                                    txt_all_answ[3], txt_all_answ[4], 95, 170)          # -> списка

    # -> создание кнопки 'result' для вывода результата
    result_btn = CreateButton(check_result_easy)
    result_btn.create_button(10, 'result', 787, 480)


# ----------------------------------------------------------------------------------------------------------------------

def check_result_medium():  # -> проверка результатов и вывод сообщения
    correct_answers = XMLDriver('data.xml').correct_answers('medium')  # -> получ.прав.ответы сложности medium из файла
    color_lbl2 = Label()                                               # -> для вывода результата
    color_lbl2.config(bg='DarkSeaGreen', width=14, height=2, font=('Comic Sans Ms', 32),
                      fg='DarkOliveGreen')
    color_lbl2.place(x=480, y=522)

    # -> user_list - список ответов пользователя, correct_answers - список правильн.ответов из файла
    if user_list == correct_answers:
        color_lbl2.config(text='Excelent!')
    elif len(user_list) < len(correct_answers):                               # -> сравнение длин списков
        messagebox.showwarning('Внимание!', 'Вы ответили не на все вопросы.')
    elif len(user_list) > len(correct_answers):                               # -> сравнение длин списков
        messagebox.showwarning('Внимание!', 'На какой-то вопрос Вы дали более одного ответа.')
    else:
        k = 0                     # -> будет хранит кол-во правильных ответов
        for i in user_list:       # -> ищет совпадение ответов в списках и выдаст сообщение, в зависимости от результата
            if i in correct_answers:
                k += 1
        if k == 4:
            color_lbl2.config(text='Good!')
        elif k == 3:
            color_lbl2.config(text='Not so bad!')
        elif k < 3:
            color_lbl2.config(text='Ohh..')


# ----------------------------------------------------------------------------------------------------------------------
# -> сложность 'medium'
# -> создание Labels вопросов теста
def medium_level():
    # -> создание Labels вопросов теста
    text_tasks = XMLDriver('data.xml').get_tasks('medium')  # -> список текстов заданий из файла
    tasks_text_lbl = BlockTasksLabels()  # -> создание блока вопросов с заполнением текста из файла
    tasks_text_lbl.create_block_tasks_lbl(text_tasks[0], text_tasks[1], text_tasks[2], text_tasks[3], text_tasks[4], 50,
                                          120)

    # -> создание блоков вариантов ответа для каждого вопроса
    txt_all_answ = XMLDriver('data.xml').get_all_answers_options('medium')  # -> список вар. ответов для каждого задания
    answers_5 = BlockAnswersFive(txt_all_answ)  # -> создаёт блоки с вариантами ответов для каждого задания и вставляет
    answers_5.create_five_blocks_ao(txt_all_answ[0], txt_all_answ[1], txt_all_answ[2],   # -> в них текст вариантов из
                                    txt_all_answ[3], txt_all_answ[4], 95, 170)           # -> списка

    # -> создание кнопки 'result' для вывода результата
    result_btn = CreateButton(check_result_medium)
    result_btn.create_button(10, 'result', 787, 480)
# ----------------------------------------------------------------------------------------------------------------------


diff_txt = XMLDriver('data.xml').get_difficulty()  # -> получает список сложности из файла

diff_btn1 = CreateButton(easy_level)  # -> кнопка вызова заданий сложности easy
diff_btn1.create_button(12, diff_txt[0], 665, 50)  # -> easy

diff_btn2 = CreateButton(medium_level)  # -> кнопка вызова заданий сложности medium
diff_btn2.create_button(12, diff_txt[1], 765, 50)  # -> medium


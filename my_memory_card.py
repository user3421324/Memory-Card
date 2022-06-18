#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from random import *
from PyQt5.QtWidgets import QApplication, QGroupBox,QButtonGroup, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Memory Card")
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox()
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')
rbtn_4 = QRadioButton('Алеуты')
but = QPushButton("Ответить")
layout_ans1 = QVBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox('Результаты')
ib_Question1= QLabel('правильно/неправильно')
ib_Question2 =QLabel('правильный ответ')
v_line = QVBoxLayout()
v_line.addWidget(ib_Question1)
v_line.addWidget(ib_Question2)
ansGroupBox.setLayout(v_line)

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

ansGroupBox.hide()
layout_line=QVBoxLayout()
layout_line.addWidget(question)
layout_line.addWidget(RadioGroupBox)
layout_line.addWidget(ansGroupBox)
layout_line.addWidget(but)

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
answers=[rbtn_1,rbtn_2,rbtn_3,rbtn_4]

def show_question():
    RadioGroupBox.show()
    ansGroupBox.hide()
    but.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)


def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    ib_Question2.setText(q.right_answer)
    show_question()
main_win.score=0
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
           show_correct('Неверно!')
           print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
def show_correct(res):
    ib_Question1.setText(res)
    show_result()

def show_result():
    RadioGroupBox.hide( )
    ansGroupBox.show()
    but.setText('Следующий вопрос')
question_list = []
q1 = Question(
    'Государственный язык Швейцарии',
'Немецкий', 
      'Чешский', 'Португальский', 'Английский')
question_list.append(q1)
q2 = Question(
    'Столица Швейцарии',
 'Берн','Стокгольм', 'Хельсинки', 'Рейкьявик')
question_list.append(q2)
q3 = Question(
    'Дата распада Берлинской стены',
'9 ноября 1989',
      '19 декабря 1990', '29 августа 1989', '26 декабря 1991')
question_list.append(q3)
q4 = Question(
    'Дата распада Чехословакии',
'31 декабря 1992',
       '12 декабря 1991', '21 сентября 1990', '23 января 1993')
question_list.append(q4)
q5 = Question(
    'Дата начала Второй Мировой Войны',
'1 сентября 1939',
'22 июня 1941', '9 мая 1945', '23 декабря 1943')
question_list.append(q5)
q6 = Question(
    'Государственный язык Молдавии' ,
'Румынский язык',
'Молдавский язык', 'Русский язык', 'Украинский язык')
question_list.append(q6)
q7 = Question(
     'Дата распада австро-венгерской империи',
'17 октября 1918 года',
'23 декабря 1919 года', '12 января 1918 года', '15 марта 1918 года')
question_list.append(q7)
q8 = Question(
     'Дата распада османской империи',
'1 ноября 1922 года',
'16 ноября 1922 года', '23 января 1922 года', '14 открября 1922')
question_list.append(q8)

def click_OK():
    if but.text() == 'Ответить':
        check_answer()
    else:
        next_question()
main_win.total=0
def next_question():
    main_win.total+=1
    cur_question = randint(0,len(question_list)-1)
    q = question_list[cur_question]
    ask(q)
but.clicked.connect(click_OK)
next_question()
main_win.setLayout(layout_line)
main_win.show()
app.exec()


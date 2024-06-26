from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout,
                             QGroupBox, QRadioButton,
                             QPushButton, QLabel,
                             QButtonGroup)      # Si dalis yra atsakinga uz PyQt5 Biblioteka bei PyQt5 funkcijas ir Skirtingus dizainus
from random import shuffle


class Question():
    ''' Vieta skirta klausimo sudarymui, atpazinimui teisingo bei neteisingo atsakymo.'''

    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


app = QApplication([])


window = QWidget()
window.setWindowTitle('Memo Card')


btn_OK = QPushButton('Answer') # answer button
lb_Question = QLabel('Kiek kodo eiluciu reikia parasyti jog Emilis butu patenkintas') # your question


RadioGroupBox = QGroupBox("Answer options") # group on the screen for radio buttons with answers
rbtn_1 = QRadioButton('---------')
# 3 buttons
rbtn_2 = QRadioButton('---------')
rbtn_3 = QRadioButton('---------')
rbtn_4 = QRadioButton('---------')


RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)



layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() # the vertical ones will be inside the horizontal ones
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # two answers in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # two answers in the second column
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # columns are in the same line
RadioGroupBox.setLayout(layout_ans1) # “panel” with answer options is ready


AnsGroupBox = QGroupBox("Test result")
lb_Result = QLabel('Are you correct or not?') # “Correct” or “Incorrect” text will be here
lb_Correct = QLabel('the answer will be here!') # correct answer text will be written here



layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)


layout_line1 = QHBoxLayout() # question
layout_line2 = QHBoxLayout() # answer options or test results
layout_line3 = QHBoxLayout() # “Answer” button


layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # the button sho


#uld be large
layout_line3.addStretch(1)


# Now let’s put the lines we’ve created one under one another:
layout_card = QVBoxLayout()


layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # spaces between the content




def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Next question')

def show_question():
    RadioGroupBox.show() # Ijungiam atgal klausimus
    AnsGroupBox.hide() # isjungiam atskymu lenta
    btn_OK.setText('Answer') # Pakeiciam mygtuka jog rodytu Answer o ne ok
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)  # Nustatome Atsakymu pasirinkima jog butu tuscia

answers = [rbtn_1, rbtn_2, rbtn_3,rbtn_4]

def ask(q: Question):
    '''This function writes the value of the question and answers in the corresponding widgets. The answer options are distributed randomly. '''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()


def show_correct(res):
    lb_Result.setText(res)
    show_result()


def check_answer():
    if answers[0].isChecked():
        show_correct('Correct! Malacius!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect! Eik mokinkis!')


def test():
    if 'Answer' == btn_OK.text():
        show_result()
    else:
        show_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

q = Question('Select the most appropriate English name for the programming concept to store some data', 'variable', 'variation','cesnakas','Pinigenai')

btn_OK.clicked.connect(test) # check that the answer panel appears when the button is pressed
window.show()
app.exec()






















from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout,
                             QGroupBox, QButtonGroup, QRadioButton,
                             QPushButton, QLabel)
from random import randint, shuffle


class Question():
  '''contains a question, a correct answer and three incorrect ones'''

  def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
    self.question = question
    self.right_answer = right_answer
    self.wrong1 = wrong1
    self.wrong2 = wrong2
    self.wrong3 = wrong3


questions_list = []
questions_list.append(
    Question('Official language of Brazil', 'Portuguese', 'English', 'Spanish',
             'Brazilian'))
questions_list.append(
    Question('Which color does not appear on the American flag?', 'Green',
             'Red', 'White', 'Blue'))
questions_list.append(
    Question('Yakut national house', 'Urasa', 'Yurta', 'Igloo', 'Khata'))

app = QApplication([])

btn_OK = QPushButton('Reply')  # the reply button
lb_Question = QLabel(
    'The most difficult question in the world!')  # question text

RadioGroupBox = QGroupBox("Answer options")  # on-screen group of radio buttons

rbtn_1 = QRadioButton('Option 1')
rbtn_2 = QRadioButton('Option 2')
rbtn_3 = QRadioButton('Option 3')
rbtn_4 = QRadioButton('Option 4')

RadioGroup = QButtonGroup(
)  # this is to group radio buttons to control their behavior
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()  # vertical guides inside the horizontal one
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)  # two answer options in the first column
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)  # two answer options in the second column
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)  # columns placed in one line

RadioGroupBox.setLayout(
    layout_ans1)  # the "panel" with answer options is ready

AnsGroupBox = QGroupBox("Test results")
lb_Result = QLabel('are you right or not?'
                   )  # here it will be written if you are "right" or "wrong"
lb_Correct = QLabel(
    'answer will be here!')  # here will be the text of the correct answer

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()  # question
layout_line2 = QHBoxLayout()  # answer options or test result
layout_line3 = QHBoxLayout()  # "Answer" button

layout_line1.addWidget(lb_Question,
                       alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide(
)  # hide the answer panel, the question panel should be visible first
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2)  # the button should be large

layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)  # spaces between the content elements

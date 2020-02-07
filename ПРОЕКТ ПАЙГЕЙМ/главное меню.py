import pygame
import os
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtWidgets
import sqlite3
import sys

pygame.init()


class addName(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.text = ''

    def initUI(self):
        self.setGeometry(300, 300, 250, 170)
        self.setStyleSheet("background-color: #AFE2FF")
        self.lbl = QLabel(self)
        self.lbl.setText("Введите своё имя")
        self.lbl.move(80, 40)
        self.res = QPushButton(self)
        self.res.move(52, 130)
        self.res.resize(150, 25)
        self.res.setText('Далее')
        self.res.clicked.connect(self.next)
        a = QLineEdit(self)
        a.move(60, 100)
        a.textChanged[str].connect(self.onChanged)
        self.setWindowTitle('QLineEdit')
        self.show()

    def onChanged(self, t):
        print(t)
        self.text = t
        return t

    def next(self):
        global Time, run, window, drawing, RUN, running
        if self.text != '':
            b = base()
            b.add(self.text, Time)
            run = True
            #drawing = True
            RUN = False
            running = False
            window.close()


class base(QWidget):
    def __init__(self):
        super().__init__()
        tabl = sqlite3.connect('Table_Records.db')

        cursor = tabl.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS core_fes(ИМЯ TEXT, '
                       'ВРЕМЯ INT)')
        cursor.close()
        tabl.commit()
        self.element()

    def add(self, a, b):
        tabl = sqlite3.connect('Table_Records.db')
        cursor = tabl.cursor()
        cursor.execute('INSERT INTO core_fes VALUES(?, ?)', (a, b))
        cursor.close()
        tabl.commit()

    def element(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('RECORDS')
        self.a = QTableWidget(self)
        self.a.setFixedSize(500, 500)
        data = []
        column_name = None
        data_base = 'Table_Records.db'
        table = 'core_fes'
        tabl = sqlite3.connect(data_base)
        cursor = tabl.cursor()
        query_columns = 'pragma table_info(' + table + ')'
        cursor.execute(query_columns)
        columns_description = cursor.fetchall()
        columns_names = []
        for column in columns_description:
            columns_names.append(column[1])
        if column_name is None:
            query = 'SELECT * FROM ' + table
            cursor.execute(query)
            data = cursor.fetchall()
        cursor.close()
        tabl.close()
        args = []
        for a in data:
            if a not in args:
                args.append(a)

        self.a.setRowCount(len(args))
        self.a.setColumnCount(2)
        header = self.a.horizontalHeader()
        self.a.setHorizontalHeaderLabels([columns_names[0], columns_names[1]])
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        self.exit = QPushButton('ВЫХОД', self)
        self.exit.setCheckable(True)
        self.exit.move(568, 670)

        self.exit.clicked.connect(self.exit_table)

        i = 0
        for tup in args:
            j = 0
            for item in tup:
                cellinfo = QTableWidgetItem(str(item))
                cellinfo.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled
                )

                self.a.setItem(i, j, cellinfo)
                j += 1

            i += 1

        self.show()

    def exit_table(self):
        self.hide()


class pravila:
    def __init__(self):
        self.screen1 = pygame.display.set_mode((800, 620))

    def text(self):
        fullname = os.path.join('фон3.jpg')
        image = pygame.image.load(fullname).convert()
        image1 = pygame.transform.scale(image, (800, 620))
        self.screen1.blit(image1, (0, 0))
        intro_text = ["Здравствуй, друг",
                      "Правила игры",
                      "Для передвижения нажимай на стрелочки на клавиатуре,",
                      "при нажатии на пробел происходит перезапуск игры!",
                      'Чтобы победить, тебе необходимо активировать и достигнуть',
                      'финиш! Для этого тебе нужно отгадывать загадки (где-то собрать',
                      'нужные предметы, где-то найти ключ). В листьях могут быть спрятаны',
                      'бонусные монетки. Если собрать их всех, ты получишь -5 секунд',
                      'от времени твоего прохождения. Для проверки листьев тебе нужно',
                      'подойти к ней, упереться в неё, если она раскрылась, ты увидишь',
                      'монетку. Собирай её и тогда приблизишься к бонусу!',
                      'На шипы кролик не может наступать, поэтому будь внимателен!',
                      'За каждое выполненное задание ты получишь значок, который',
                      'загорится сверху, если ты всё сделал верно!',
                      'Если ты не можешь понять, что нужно делать, ты можешь купить подсказку',
                      'за 1 бонусную монетку!',
                      'Удачи, помоги кролику добраться до финиша!']
        text_coord = 10
        font = pygame.font.SysFont('freesans', 20)
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('#0025B9'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 10
            text_coord += intro_rect.height
            self.screen1.blit(string_rendered, intro_rect)
        self.screen1.fill(pygame.Color('#FF9487'), (550, 540, 160, 60))
        font = pygame.font.SysFont('freesans', 50)
        text = font.render('Далее', 1, (85, 21, 151))
        self.screen1.blit(text, (570, 545))

    def next(self, a='off', b='off'):
        if a == 'off' and b == 'off':
            self.screen1.fill(pygame.Color('#FF9487'), (550, 540, 160, 60))
            font = pygame.font.SysFont('freesans', 50)
            text = font.render('Далее', 1, (85, 21, 151))
            self.screen1.blit(text, (570, 540))
        elif a == 'on' and b == 'off':
            self.screen1.fill(pygame.Color('#FF87A9'), (540, 530, 180, 80))
            font = pygame.font.SysFont('freesans', 55)
            text = font.render('Далее', 1, (85, 21, 151))
            self.screen1.blit(text, (560, 530))
        pygame.display.flip()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.karta = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 3, 4, 2, 6, 8, 17, 2, 6, 2, 1],
                      [1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                      [1, 2, 5, 5, 6, 6, 6, 5, 5, 15, 1],
                      [1, 2, 5, 6, 6, 2, 6, 6, 5, 2, 1],
                      [1, 6, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                      [1, 18, 2, 5, 5, 10, 5, 5, 2, 15, 1],
                      [1, 13, 2, 2, 2, 2, 2, 2, 2, 6, 1],
                      [1, 3, 13, 2, 16, 0, 2, 6, 2, 2, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.person_i = 9
        self.person_j = 5
        self.person = 2
        self.carrot = 15
        self.key = 0
        self.cabbage = 1
        self.winner = 0
        self.time = 0
        self.coin = 0
        pygame.mixer.music.load('play.mp3')
        pygame.mixer.music.play()

    def win(self):
        return self.winner

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        x = (self.width * self.cell_size)
        y = (self.height * self.cell_size)
        self.screen = pygame.display.set_mode((x + 40, y + 100))
        self.screen.fill(pygame.Color('#FFCBB0'))

    def proverka(self):
        global n, Time
        if self.carrot == 0:
            self.karta[1][9] = 7
            self.carrot = 100
            n = 0
        if self.key == 1:
            self.karta[2][1] = 2
            self.karta[1][2] = 2
            n = 0
        if self.key == 2:
            self.karta[8][1] = 2
            self.karta[9][2] = 2
            n = 0
        if self.cabbage == 0:
            self.karta[9][9] = 14
            n = 0
        if self.winner == 6:
            size = self.width1, self.height1 = 600, 400
            self.screen1 = pygame.display.set_mode(size)
            fullname = os.path.join('фон4.jpg')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (600, 400))
            self.screen1.blit(image1, (0, 0))
            font = pygame.font.SysFont('freesans', 30)
            text = font.render(
                'ПОБЕДА - ваше время - ' + str((pygame.time.get_ticks() - self.time) // 1000) + ' секунд',
                1,
                (255, 130, 14))
            self.screen1.blit(text, (160, 100))
            self.screen1.fill(pygame.Color('#FF87A9'), (400, 10, 130, 70))
            font = pygame.font.SysFont('freesans', 50)
            text = font.render('Далее', 1, (85, 21, 151))
            self.screen1.blit(text, (400, 10))
            Time = int((pygame.time.get_ticks() - self.time) // 1000)

    def time_clock(self):
        if pygame.time.get_ticks() - self.time > 5000:
            return True
        else:
            return False

    def moving(self, movee):
        global n
        self.go = [2, 3, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 10]
        if (movee == 2 and (self.person_i + 1) < 11) or (movee == 1 and self.person_i > 0) or (
                        movee == 3 and (self.person_j + 1) < 11) or (movee == 4 and self.person_j > 0) or movee == 5:

            if movee == 1 and self.karta[self.person_i - 1][self.person_j] in self.go:
                if self.person_i >= 0:
                    self.karta[self.person_i][self.person_j] = self.person
                    self.person_i -= 1
                    self.person = self.karta[self.person_i][self.person_j]
                    self.karta[self.person_i][self.person_j] = 0
            elif movee == 2 and self.karta[self.person_i + 1][self.person_j] in self.go:
                if (self.person_i + 1) >= 11:
                    pass
                else:
                    self.karta[self.person_i][self.person_j] = self.person
                    self.person_i += 1
                    self.person = self.karta[self.person_i][self.person_j]
                    self.karta[self.person_i][self.person_j] = 0

            elif movee == 3 and self.karta[self.person_i][self.person_j + 1] in self.go:
                self.karta[self.person_i][self.person_j] = self.person
                self.person_j += 1
                self.person = self.karta[self.person_i][self.person_j]
                self.karta[self.person_i][self.person_j] = 0
            elif movee == 4 and self.karta[self.person_i][self.person_j - 1] in self.go:
                self.karta[self.person_i][self.person_j] = self.person
                self.person_j -= 1
                self.person = self.karta[self.person_i][self.person_j]
                self.karta[self.person_i][self.person_j] = 0
            elif movee == 5:
                self.width = 11
                self.height = 11
                self.board = [[0] * 11 for _ in range(11)]
                self.karta = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                              [1, 3, 4, 2, 6, 8, 17, 2, 6, 2, 1],
                              [1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                              [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                              [1, 2, 5, 5, 6, 6, 6, 5, 5, 15, 1],
                              [1, 2, 5, 6, 6, 2, 6, 6, 5, 2, 1],
                              [1, 6, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                              [1, 18, 2, 5, 5, 10, 5, 5, 2, 15, 1],
                              [1, 13, 2, 2, 2, 2, 2, 2, 2, 6, 1],
                              [1, 3, 13, 2, 16, 0, 2, 6, 2, 2, 1],
                              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
                self.person_i = 9
                self.person_j = 5
                self.person = 2
                self.carrot = 15
                self.key = 0
                self.cabbage = 1
                self.winner = 0
                self.coin = 0
                self.time += (pygame.time.get_ticks())
        if movee == 1 and self.person == 17:
            self.karta[self.person_i - 1][self.person_j] = 19
            self.person = 2
        elif movee == 2 and self.person == 16:
            self.karta[self.person_i + 1][self.person_j] = 19
            self.person = 2
        elif movee == 3 and self.person == 15:
            self.karta[self.person_i][self.person_j + 1] = 19
            self.person = 2
        elif movee == 4 and self.person == 18:
            self.karta[self.person_i][self.person_j - 1] = 19
            self.person = 2

        if self.person == 6:
            self.person = 2
            self.carrot -= 1
            n = 1
        elif self.person == 7 or self.person == 14:
            self.person = 2
            if self.key == 0:
                self.key = 1
            elif self.key == 1:
                self.key = 2
                self.cabbage = 100
            n = 1
        elif self.person == 19:
            self.person = 2
            self.coin += 1
        elif self.person == 3 and self.key == 1:
            self.cabbage = 10
            self.karta[1][7] = 9
            self.karta[2][9] = 9
            self.karta[9][7] = 9
            self.karta[5][1] = 9
            self.karta[8][2] = 9
            self.person = 11
        elif self.person == 9:
            self.cabbage -= 1
            self.person = 2
            if self.cabbage == 5:
                self.karta[1][3] = 9
                self.karta[3][2] = 9
                self.karta[3][8] = 9
                self.karta[7][8] = 9
                self.karta[7][2] = 9
            n = 1
        elif self.person == 3 and self.key == 2:
            self.winner = 1
            self.person = 11
            self.karta[1][5] = 12
        elif self.person == 9:
            self.cabbage -= 1
        elif self.person == 10:
            self.person = 20

        if self.winner == 1 and self.person == 12:
            self.person = 2
            self.karta[9][5] = 8
            self.winner = 2
        elif self.winner == 2 and self.person == 8:
            self.person = 2
            self.karta[5][9] = 8
            self.winner = 3
        elif self.winner == 3 and self.person == 8:
            self.person = 2
            self.karta[1][9] = 8
            self.winner = 4
        elif self.winner == 4 and self.person == 8:
            self.person = 2
            self.karta[5][1] = 8
            self.winner = 5
            n = 1
        elif self.winner == 5 and self.person == 8:
            self.person = 2
            self.karta[5][1] = 8
            self.winner = 6
            n = 1

        pygame.display.flip()

    def render(self, m=2):
        if m == 5:
            m = 2
        if self.coin != 5:
            fullname = os.path.join('МФ1.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (55, 5))
        else:
            fullname = os.path.join('МФ2.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (55, 5))
        if self.carrot != 100:
            fullname = os.path.join('мор2.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (140, 5))
        else:
            fullname = os.path.join('мор1.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (140, 5))
        if self.cabbage != 0 and self.cabbage != 100:
            fullname = os.path.join('кап1.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (225, 5))
        else:
            fullname = os.path.join('кап2.png')
            image = pygame.image.load(fullname).convert()
            image1 = pygame.transform.scale(image, (70, 70))
            self.screen.blit(image1, (225, 5))
        for i in range(self.width):
            for j in range(self.height):
                if self.karta[i][j] == 1:
                    fullname = os.path.join('трава.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] in [2, 15, 16, 17, 18]:
                    fullname = os.path.join('п.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 5:
                    fullname = os.path.join('забор.png')
                    image = pygame.image.load(fullname).convert()
                    image.set_colorkey((255, 255, 255))
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 6:
                    fullname = os.path.join('морковь.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 8:
                    fullname = os.path.join('финиш.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 4:
                    fullname = os.path.join('замок.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 3:
                    fullname = os.path.join('кнопка.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 10:
                    fullname = os.path.join('ловушка.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 20:
                    fullname = os.path.join('ловушка2.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 0:
                    if m == 2:
                        fullname = os.path.join('кроликперед.png')
                        image = pygame.image.load(fullname).convert()
                        image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                        self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                    elif m == 1:
                        fullname = os.path.join('кроликзад.png')
                        image = pygame.image.load(fullname).convert()
                        image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                        self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                    elif m == 3:
                        fullname = os.path.join('кроликправо.png')
                        image = pygame.image.load(fullname).convert()
                        image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                        self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                    elif m == 4:
                        fullname = os.path.join('кроликлево.png')
                        image = pygame.image.load(fullname).convert()
                        image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                        self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 7:
                    fullname = os.path.join('ключ.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 9:
                    fullname = os.path.join('капуста.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 11:
                    fullname = os.path.join('кнопка1.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 12:
                    fullname = os.path.join('финиш1.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 13:
                    fullname = os.path.join('замок1.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 14:
                    fullname = os.path.join('ключ1.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))
                elif self.karta[i][j] == 19:
                    fullname = os.path.join('монетка.png')
                    image = pygame.image.load(fullname).convert()
                    image1 = pygame.transform.scale(image, (self.cell_size, self.cell_size))
                    self.screen.blit(image1, (self.top + j * self.cell_size, self.left + i * self.cell_size,))


class Menu:
    def __init__(self):
        self.screen2 = pygame.display.set_mode((400, 600))
        self.screen2.fill(pygame.Color('#FFCBB0'))
        pygame.mixer.music.load('menu.mp3')
        pygame.mixer.music.play()

    def fon(self):
        fullname = os.path.join('фон.png')
        image = pygame.image.load(fullname).convert()
        image1 = pygame.transform.scale(image, (400, 600))
        self.screen2.blit(image1, (0, 0))

    def play(self, a='off', b='off'):
        if a == 'off' and b == 'off':
            self.screen2.fill(pygame.Color('#FF9487'), (255, 291, 133, 60))
            font = pygame.font.SysFont('freesans', 50)
            text = font.render('Играть', 1, (85, 21, 151))
            self.screen2.blit(text, (255, 291))
        elif a == 'on' and b == 'off':
            self.screen2.fill(pygame.Color('#FF87A9'), (246, 280, 148, 70))
            font = pygame.font.SysFont('freesans', 55)
            text = font.render('Играть', 1, (85, 21, 151))
            self.screen2.blit(text, (246, 288))
        elif b == 'on':
            pygame.mixer.music.pause()

    def record(self, a='off', b='off'):
        if a == 'off' and b == 'off':
            self.screen2.fill(pygame.Color('#FF9487'), (255, 358, 133, 60))
            font = pygame.font.SysFont('freesans', 40)
            text = font.render('Рекорды', 1, (85, 21, 151))
            self.screen2.blit(text, (255, 361))
        elif a == 'on' and b == 'off':
            self.screen2.fill(pygame.Color('#FF87A9'), (246, 350, 148, 75))
            font = pygame.font.SysFont('freesans', 42)
            text = font.render('Рекорды', 1, (85, 21, 151))
            self.screen2.blit(text, (250, 361))

    def ex(self, a='off', b='off'):
        if a == 'off' and b == 'off':
            self.screen2.fill(pygame.Color('#FF9487'), (255, 425, 133, 60))
            font = pygame.font.SysFont('freesans', 40)
            text = font.render('Выход', 1, (85, 21, 151))
            self.screen2.blit(text, (255, 425))
        elif a == 'on' and b == 'off':
            self.screen2.fill(pygame.Color('#FF87A9'), (246, 425, 148, 70))
            font = pygame.font.SysFont('freesans', 42)
            text = font.render('Выход', 1, (85, 21, 151))
            self.screen2.blit(text, (250, 425))


PLAY = True
a1 = 1
clock = pygame.time.Clock()
Fon = Menu()
run = True
a1 = 'off'
b1 = 'off'
a2 = 'off'
b2 = 'off'
a3 = 'off'
b3 = 'off'
drawing = True
running = False
RUN = False
while PLAY:
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                PLAY = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if (x >= 255) and (x <= 388) and (y >= 291) and (y <= 351):
                    b1 = 'on'
                    Fon.play(a1, b1)
                elif (x >= 255) and (x <= 388) and (y >= 356) and (y <= 416):
                    b2 = 'on'
                    Fon.record(a2, b2)
                elif (x >= 255) and (x <= 388) and (y >= 425) and (y <= 485):
                    b3 = 'on'
                    Fon.ex(a3, b3)
                print(event.pos)
            elif event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
                x, y = event.pos
                if (x >= 255) and (x <= 388) and (y >= 291) and (y <= 351):
                    a1 = 'on'
                    Fon.play(a1)
                elif (x >= 255) and (x <= 388) and (y >= 356) and (y <= 416):
                    a2 = 'on'
                    Fon.record(a2)
                elif (x >= 255) and (x <= 388) and (y >= 425) and (y <= 485):
                    a3 = 'on'
                    Fon.ex(a3)
                if x < 255 or x > 388 or y < 291 or y > 351:
                    a1 = 'off'
                if x < 255 or x > 388 or y < 356 or y > 416:
                    a2 = 'off'
                if x < 255 or x > 388 or y < 425 or y > 485:
                    a3 = 'off'
                if b1 == 'on':
                    run = False
                    RUN = True
                    b1 = 'off'
                if b3 == 'on':
                    run = False
                    PLAY = False
                    drawing = False
                    RUN = False
                    running = False
                    pygame.quit()
                    sys.exit()
                if b2 == 'on':
                    app = QApplication(sys.argv)
                    record = base()
                    record.show()
                    b2 = 'off'
                    sys.exit(app.exec_())

            Fon.fon()
        if drawing:
            Fon.play(a1)
            Fon.record(a2)
            Fon.ex(a3)
            clock.tick(60)
            pygame.display.flip()

    if RUN:
        p = pravila()
        p1 = 'off'
        p2 = 'off'
        drawing = True
        while RUN:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                    PLAY = False
                if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos
                    if (x >= 550) and (x <= 710) and (y >= 540) and (y <= 600):
                        p1 = 'on'
                        p.next(p1)
                    else:
                        p1 = 'off'
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if (x >= 550) and (x <= 710) and (y >= 540) and (y <= 600):
                        p2 = 'on'
                        p.next(p2)
                    if p2 == 'on':
                        RUN = False
                        running = True

                p.text()
            if drawing:
                p.next(p1, p2)
                clock.tick(60)
                pygame.display.flip()
    if running:
        n = 0
        clock = pygame.time.Clock()
        board = Board(11, 11)
        board.set_view(80, 20, 35)
        board.render()
        pygame.display.flip()
        move = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                PLAY = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    move = 1
                    board.moving(move)
                elif event.key == pygame.K_DOWN:
                    move = 2
                    board.moving(move)
                elif event.key == pygame.K_RIGHT:
                    move = 3
                    board.moving(move)
                elif event.key == pygame.K_LEFT:
                    move = 4
                    board.moving(move)
                elif event.key == pygame.K_SPACE:
                    move = 5
                    board.moving(move)
                if n == 1:
                    board.proverka()
                if board.win() != 6:
                    board.render(move)
                pygame.display.flip()
            if event.type == pygame.MOUSEBUTTONDOWN and board.win() == 6:
                x, y = event.pos
                if (x >= 400) and (x <= 530) and (y >= 10) and (y <= 70):
                    app = QApplication(sys.argv)
                    window = addName()
                    window.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    sys.exit(app.exec_())
pygame.quit()

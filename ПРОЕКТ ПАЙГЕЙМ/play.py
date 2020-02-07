import pygame
import os

pygame.init()


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
        global n
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
            self.screen1.fill((255, 179, 155))
            font = pygame.font.SysFont('freesans', 30)
            text = font.render(
                'ПОБЕДА - ваше время - ' + str((pygame.time.get_ticks() - self.time) // 1000) + ' секунд',
                1,
                (217, 108, 255))
            text_x = self.width1 // 2 - text.get_width() // 2
            text_y = self.height1 // 2 - text.get_height() // 2
            self.screen1.blit(text, (text_x, text_y))

    def time_clock(self):
        if pygame.time.get_ticks() - self.time > 5000:
            return True
        else:
            return False

    def moving(self, movee):
        global n
        self.go = [2, 3, 6, 7, 8, 9, 11, 12, 14, 15, 16, 17, 18, 19, 10]

        if movee == 1 and self.karta[self.person_i - 1][self.person_j] in self.go:
            self.karta[self.person_i][self.person_j] = self.person
            self.person_i -= 1
            self.person = self.karta[self.person_i][self.person_j]
            self.karta[self.person_i][self.person_j] = 0
        elif movee == 2 and self.karta[self.person_i + 1][self.person_j] in self.go:
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


n = 0
clock = pygame.time.Clock()
board = Board(11, 11)
board.set_view(80, 20, 35)
board.render()
pygame.display.flip()
running = True
drawing = False
move = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
    if drawing:
        board.render()
        clock.tick(60)
        pygame.display.flip()

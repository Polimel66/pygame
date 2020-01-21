import pygame

pygame.init()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        self.karta = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 3, 4, 2, 6, 8, 2, 2, 6, 2, 1],
                      [1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                      [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                      [1, 2, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                      [1, 2, 5, 6, 6, 2, 6, 6, 5, 2, 1],
                      [1, 6, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                      [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                      [1, 4, 2, 2, 2, 2, 2, 2, 2, 6, 1],
                      [1, 3, 4, 2, 2, 0, 2, 6, 2, 2, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.person_i = 9
        self.person_j = 5
        self.person = 2
        self.carrot = 15
        self.key = 0
        self.cabbage = 1
        self.winner = 0
        self.time = 0

    def win(self):
        return self.winner

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        x = (self.width * self.cell_size)
        y = (self.height * self.cell_size)
        self.screen = pygame.display.set_mode((x + 40, y + 40))
        self.screen.fill(pygame.Color('#FFCBB0'))

    def proverka(self):
        global n
        if self.carrot == 0:
            self.karta[1][9] = 7
            self.carrot = 1
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
            self.karta[9][9] = 7
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

    def moving(self, movee):
        global n
        if (pygame.time.get_ticks() - self.time) < 5000:
            self.go = [2, 3, 6, 7, 8, 9, 10, 11, 12]
        else:
            self.go = [2, 3, 6, 7, 8, 9, 11, 12]
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
                          [1, 3, 4, 2, 6, 8, 2, 2, 6, 2, 1],
                          [1, 4, 2, 2, 2, 2, 2, 2, 2, 2, 1],
                          [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                          [1, 2, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                          [1, 2, 5, 6, 6, 2, 6, 6, 5, 2, 1],
                          [1, 6, 5, 5, 6, 6, 6, 5, 5, 2, 1],
                          [1, 2, 2, 5, 5, 10, 5, 5, 2, 2, 1],
                          [1, 4, 2, 2, 2, 2, 2, 2, 2, 6, 1],
                          [1, 3, 4, 2, 2, 0, 2, 6, 2, 2, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            self.person_i = 9
            self.person_j = 5
            self.person = 2
            self.carrot = 15
            self.key = 0
            self.cabbage = 1
            self.winner = 0
            self.time += (pygame.time.get_ticks())

        if self.person == 6:
            self.person = 2
            self.carrot -= 1
            n = 1
        elif self.person == 7:
            self.person = 2
            if self.key == 0:
                self.key = 1
            elif self.key == 1:
                self.key = 2
                self.cabbage = 1
            n = 1
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

    def render(self):
        for i in range(self.width):
            for j in range(self.height):
                if self.karta[i][j] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('green'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.rect(self.screen, pygame.Color('#1BA224'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 1)
                elif self.karta[i][j] == 2:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                elif self.karta[i][j] == 5:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('#7E3A00'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 15)
                elif self.karta[i][j] == 6:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('#FF7603'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 10)
                    pygame.draw.circle(self.screen, pygame.Color('#89FF13'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 6)
                elif self.karta[i][j] == 8:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 18)
                    pygame.draw.circle(self.screen, pygame.Color('white'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 15)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 10)
                    pygame.draw.circle(self.screen, pygame.Color('white'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 5)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 2)
                elif self.karta[i][j] == 4:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.rect(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size), 1)
                    pygame.draw.line(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size + self.cell_size // 3, self.left + i * self.cell_size), (
                                         self.top + j * self.cell_size + self.cell_size // 3,
                                         self.left + i * self.cell_size + self.cell_size), 2)
                    pygame.draw.line(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size + self.cell_size // 3 * 2, self.left + i * self.cell_size), (
                                         self.top + j * self.cell_size + self.cell_size // 3 * 2,
                                         self.left + i * self.cell_size + self.cell_size), 2)
                    pygame.draw.line(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size + self.cell_size // 3), (
                                         self.top + j * self.cell_size + self.cell_size,
                                         self.left + i * self.cell_size + self.cell_size // 3), 2)
                    pygame.draw.line(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size + self.cell_size // 3 * 2), (
                                         self.top + j * self.cell_size + self.cell_size,
                                         self.left + i * self.cell_size + self.cell_size // 3 * 2), 2)
                elif self.karta[i][j] == 3:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.rect(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + self.cell_size // 4,
                        self.left + i * self.cell_size + self.cell_size // 4, self.cell_size // 2,
                        self.cell_size // 2 + 1), 0)
                elif self.karta[i][j] == 10:
                    if pygame.time.get_ticks() - self.time > 5000:
                        pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                            self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                            self.cell_size + 1), 0)
                        pygame.draw.rect(self.screen, pygame.Color('red'), (
                            self.top + j * self.cell_size + self.cell_size // 8,
                            self.left + i * self.cell_size + self.cell_size // 8, self.cell_size // 8 * 6,
                            self.cell_size // 8 * 6 + 1), 0)
                    else:
                        pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                            self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                            self.cell_size + 1), 0)
                        pygame.draw.rect(self.screen, pygame.Color('#B5B4B4'), (
                            self.top + j * self.cell_size + self.cell_size // 8,
                            self.left + i * self.cell_size + self.cell_size // 8, self.cell_size // 8 * 6,
                            self.cell_size // 8 * 6 + 1), 0)
                elif self.karta[i][j] == 0:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('#FF9D68'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 16)
                    pygame.draw.circle(self.screen, pygame.Color('black'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 16, 1)
                elif self.karta[i][j] == 7:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.line(self.screen, pygame.Color('#FF2860'), (
                        self.top + j * self.cell_size + self.cell_size // 2, self.left + i * self.cell_size), (
                                         self.top + j * self.cell_size + self.cell_size // 2,
                                         self.left + i * self.cell_size + self.cell_size - 2), 2)
                    pygame.draw.line(self.screen, pygame.Color('#FF2860'), (
                        self.top + j * self.cell_size + self.cell_size // 4, self.left + i * self.cell_size), (
                                         self.top + j * self.cell_size + self.cell_size // 2,
                                         self.left + i * self.cell_size), 2)
                    pygame.draw.line(self.screen, pygame.Color('#FF2860'), (
                        self.top + j * self.cell_size + self.cell_size // 4,
                        self.left + i * self.cell_size + self.cell_size // 4), (
                                         self.top + j * self.cell_size + self.cell_size // 2,
                                         self.left + i * self.cell_size + self.cell_size // 4), 2)
                    pygame.draw.circle(self.screen, pygame.Color('#FF2860'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 3 * 2)), 10, 1)
                elif self.karta[i][j] == 9:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('#2EA628'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 10)
                    pygame.draw.circle(self.screen, pygame.Color('#32FF35'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 8)
                    pygame.draw.circle(self.screen, pygame.Color('#2EA628'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 6)
                    pygame.draw.circle(self.screen, pygame.Color('#32FF35'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 4)
                elif self.karta[i][j] == 11:
                    pygame.draw.rect(self.screen, pygame.Color('#F6A808'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.rect(self.screen, pygame.Color('#BBFF00'), (
                        self.top + j * self.cell_size + self.cell_size // 4,
                        self.left + i * self.cell_size + self.cell_size // 4, self.cell_size // 2,
                        self.cell_size // 2 + 1), 0)
                elif self.karta[i][j] == 12:
                    pygame.draw.rect(self.screen, pygame.Color('yellow'), (
                        self.top + j * self.cell_size, self.left + i * self.cell_size, self.cell_size,
                        self.cell_size + 1), 0)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 18)
                    pygame.draw.circle(self.screen, pygame.Color('white'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 15)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 10)
                    pygame.draw.circle(self.screen, pygame.Color('white'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 5)
                    pygame.draw.circle(self.screen, pygame.Color('red'), (
                        self.top + j * self.cell_size + (self.cell_size // 2),
                        self.left + i * self.cell_size + 1 + (self.cell_size // 2)), 2)


n = 0
clock = pygame.time.Clock()
board = Board(11, 11)
board.set_view(20, 20, 35)
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
                board.render()
            pygame.display.flip()
    if drawing:
        board.render()
        clock.tick(60)
        pygame.display.flip()

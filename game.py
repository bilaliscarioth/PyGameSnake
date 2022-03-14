"""
Copyright (C) 2022 BILAL EMOHMADIAN

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION
OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN
CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE

"""

import pygame
import pygame.locals
from entity import ( Entity )

class Game:
    def __init__(self , screen_x, screen_y, score = 0):
        pygame.init() #Need pygame instance to use OpenGL or any API  Video Drivers...
        """ Options Games/ Config"""
        self.screen = pygame.display.set_mode((screen_x, screen_y))
        self.font = pygame.font.SysFont(None, 30)
        self.shutdown = False
        self.score = score
        self.surface = pygame.Surface((screen_x, screen_y))
        self.list_fruits = []
        self.snake: Entity = None

    def Display(self):
        """
        Adding a title to the window;
        ____
        Return: None
        """
        pygame.display.set_caption("Snake")

    def RendererGame():
        """
        Renderer / Update playboard from pygame.
        ____
        Return Nothing
        """
        pygame.display.update()

    def ReadAndPlaySound(filepath:str):
        """
        Read a song and play it with pygame
        _____
        Return None
        """
        pygame.mixer.music.load(filepath)
        pygame.mixer.music.play()

    def LoadImage(filepath:str):
        """
        Load an image and return
        ____
        Return Pygame.Image
        """
        return pygame.image.load(filepath)

    def KeyEvent(self):
        """
        Key Event Thread (only input keyboard)
        ____
        Return None
        """
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.setShutdown(True)
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    self.setShutdown(True)
                if e.key == pygame.K_RIGHT:
                    self.snake.setImage(pygame.transform.rotate(self.snake.getImage() , 90))
                    self.snake.setCords("D")
                if e.key == pygame.K_LEFT:
                    self.snake.setImage(pygame.transform.rotate(self.snake.getImage() , -90))
                    self.snake.setCords("Q")
                if e.key == pygame.K_UP:
                    self.snake.setImage(pygame.transform.rotate(self.snake.getImage() , -0))
                    self.snake.setCords("W")
                if e.key == pygame.K_DOWN:
                    self.snake.setImage(pygame.transform.rotate(self.snake.getImage() , 180))
                    self.snake.setCords("S")

    def setScore(self, score):
        self.score = score

    def setSnake(self, snake:Entity):
        print("Create character..")
        self.snake = snake
        print(self.snake)

    def getSnake(self):
        """
        Get address memory from snake.
        ____
        Return Entity
        """
        return self.snake

    def getFont(self):
        """
        Get Font from pygame
        ____
        Pygame
        """
        return self.font

    def getScreen(self):
        return self.screen

    def getShutdown(self):
        return self.shutdown

    def setShutdown(self, shut):
        self.shutdown = shut

    def getScore(self):
        return self.score

    def getSurface(self):
        return self.surface

    def setList(self, L:Entity):
        """
        Add an item entity on the playboard;
        Can be return with list_fruits.
        ___
        Return None
        """
        self.list_fruits = L

    def getList(self):
        return self.list_fruits

    def quit():
        """
        Quit PyGame; Close Instance...
        ____
        Return None
        """
        pygame.quit()
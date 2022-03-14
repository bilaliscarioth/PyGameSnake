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
import time
from random import randint

from game import (
    Game
)

from entity import(
    Entity
)

game = Game(800, 600)
game.setList([Entity([32,32], [randint(30, 760),randint(30, 560)],  Game.LoadImage("NOURRITURE.png"))])
fill = game.getSurface()
fill.fill((50, 50, 255))
SCORE = game.getFont().render("{0} points".format(game.getScore()) , 1, (255,0,0))
game.getScreen().blit(fill, (0, 0))
game.setSnake(Entity([32, 32], [300, 332], Game.LoadImage("TETE.png"), Corps=[]))
game.Display()
snake = game.getSnake()

while not game.getShutdown():
    list_fruit = game.getList()
    fill = game.getSurface()

    for i in snake.getCorps():
        game.getScreen().blit(i.getImage(), i.getCords())
    game.getScreen().blit(snake.getImage(), snake.getCords())

    if(len(game.getList()) == 0):
        game.setList([Entity([32,32], [randint(30, 760),randint(30, 560)],  Game.LoadImage("NOURRITURE.png"))])
        list_fruit = game.getList()

    if(len(list_fruit) == 1):
        game.getScreen().blit(list_fruit[0].getImage(), list_fruit[0].getCords())
    old_pos = snake.getCords()

    if( old_pos[0] < 20 or old_pos[0]  > 780):
        game.setShutdown(True)
    if( old_pos[1] < 20 or old_pos[1]  > 580):
        game.setShutdown(True)

    if(len(game.getList()) == 1):
        if(list_fruit[0].getCords()[0] < old_pos[0] +  snake.getSize()[0]) and \
            (list_fruit[0].getCords()[0]  +  list_fruit[0].getSize()[0] > snake.getCords()[0]) and \
            (list_fruit[0].getCords()[1] < old_pos[1] +  snake.getSize()[1]) and \
            (list_fruit[0].getCords()[1]  +  list_fruit[0].getSize()[1] > snake.getCords()[1]) :
            Game.ReadAndPlaySound("NOURRITURE.mp3")
            game.setScore(game.getScore() + 1)
            SCORE = game.getFont().render("{0} points".format(game.getScore()) , 1, (255,0,0))
            game.getScreen().blit(SCORE, (10, 20))
            game.getList().pop()
            snake.getCorps().append(Entity([32, 32], [snake.getCords()[0]+ 30, snake.getCords()[1]+ 30], Game.LoadImage("CORPS.png")))

    snake.updateImg()
    Game.RendererGame()
    game.KeyEvent()
    game.getScreen().fill((50, 50, 255))
    game.getScreen().blit(SCORE, (10, 20))


Game.ReadAndPlaySound('PERDU.mp3')
time.sleep(12)
Game.quit()
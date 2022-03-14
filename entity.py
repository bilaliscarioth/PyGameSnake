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

from typing import( List )

class Entity:
    def __init__(self, size, pos, img = None, destination = "D", Corps=None):
        if len(pos) == 2:
            self.pos= pos
        if len(size) == 2:
            self.size = size
        self.corps = Corps
        self.img = img
        self.destination = destination

    def setCords(self, pos:List[int]):
        """
        Change Coords with given pos
        ____
        Return : None
        """
        self.destination = pos

    def updateImg(self):
        """
        Update image from Entity:
        ____
        Return :  None
        """
        if self.destination == "D":
            self.pos[0] += 0.25
        elif self.destination == "Q":
            self.pos[0] -= 0.25
        elif self.destination == "W":
            self.pos[1] -= 0.25
        elif self.destination == "S":
            self.pos[1] += 0.25

    def getCorps(self):
        """
        Snake body
        ____
        Return Entity
        """
        return self.corps

    def setSize(self, size:List[int]):
        """
        Give a 2D Arrays [x, y]
        ___
        Return : None
        """
        self.size = size

    def setImage(self, img):
        """
        Give a PyGame.Image
        ___
        Return: None
        """
        self.img = img

    def getSize(self):
        """
        Give a 2D Arrays [x,y]
        ___
        Return: Pygame.Image
        """
        return self.size
    def getCords(self):
        """
        Return 2D Arrays coords [x,y]
        ____
        Return : List[int]
        """
        return self.pos

    def getImage(self):
        """
        Return Pygame.Image
        """
        return self.img
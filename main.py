from tkinter import *
import functools

class gameControl(Canvas):

    def __init__(self):
        self.width = 2000
        self.height = 1000
        super().__init__(width=self.width, height = self.height)
        self.speed = 5
        self.vspeed = 15
        self.grav = 1e-7

        self.rect = self.create_rectangle(50, 20, 150, 80, fill="#476042")
        self.floor = self.create_rectangle(0, 950, 2500, 1000, fill="#476042")
        coords = self.coords(self.rect)
        print(coords)
        self.pack(expand=YES, fill=BOTH)
        self.focus_set()

        def lefthandler(event, obj=self.rect):
            return move_left(event, obj)

        def handler(event, obj=self.rect):
            return move_right(event, obj)

        def uphandler(event, obj=self.rect):
            return move_up(event, obj)

        self.bind('<Right>', handler)
        self.bind('<Left>', lefthandler)
        self.bind('<Up>', uphandler)

        self.check_boundaries(self.rect)

    def check_boundaries(self, rect):
        p = self.coords(rect)
        coll = self.find_overlapping(p[0], p[1], p[2], p[3])
        coll = list(coll)
        coll.remove(rect)

        if len(coll) != 0:
            print('hit')

    def gravity(self, rect):
        coords = self.coords(rect)
        self.grav = self.grav+1e-7
        self.coords(rect, coords[0], coords[1]+self.grav, coords[2], coords[3]+self.grav)



def move_left(event, obj):
    coords = self.coords(obj)
    if self.coords(obj)[2] > 0:
        self.coords(obj, coords[0] - self.speed, coords[1], coords[2] - self.speed, coords[3])

def move_right(event, obj):
    coords = self.coords(obj)
    if self.coords(obj)[2] < self.width:
        self.coords(obj, coords[0] + self.speed, coords[1], coords[2] + self.speed, coords[3])

def move_up(event, obj):
    coords = self.coords(obj)
    if self.coords(obj)[1] > 0:
        self.coords(obj, coords[0] , coords[1]- 2000*self.grav, coords[2], coords[3]- 2000*self.grav)



if __name__ == '__main__':
    from tkinter import *

    master = Tk()

    self = gameControl()
    while True:
        #self.gravity(self.rect)
        master.update_idletasks()
        master.update()




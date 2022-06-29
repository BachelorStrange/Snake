from tkinter import *
import functools






def move_right(event, obj):
    coords = w.coords(obj)
    #print(coords)
    #w.delete("all")
    #w.create_rectangle(coords[0] + 1, coords[1], coords[2] + 1, coords[3], fill="#476042")
    w.coords(obj, coords[0] + 1, coords[1], coords[2] + 1, coords[3])


if __name__ == '__main__':
    from tkinter import *

    master = Tk()

    w = Canvas(master, width=2000, height=1000)


    rect = w.create_rectangle(50, 20, 150, 80, fill="#476042")
    floor = w.create_rectangle(0, 950, 2500, 1000, fill="#476042")
    coords = w.coords(rect)
    print(coords)
    w.pack(expand=YES, fill=BOTH)
    w.focus_set()
    def handler(event, obj=rect):
        return move_right(event, obj)
    w.bind('<Right>', handler)





    mainloop()

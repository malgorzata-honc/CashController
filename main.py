from tkinter import *

import model
import view
import controller


if __name__ == '__main__':
    root = Tk()
    #view = view.View(root)
    #model = model.Model()
    controller = controller.Controller( model.Model(), view.View(root))
    root.mainloop()

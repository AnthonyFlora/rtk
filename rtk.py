import Tkinter

class Plot(Tkinter.Frame):
  def __init__(self, parent=None):  
    Tkinter.Frame.__init__(self, parent)
    self.parent = parent
    self.parent.title("Hello")
    print "plot init"


root = Tkinter.Tk()

p = Plot(parent=root)

root.mainloop()



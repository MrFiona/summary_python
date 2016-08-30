'''
Created on 2016年8月4日

@author: apple
'''

from tkinter  import *

 #Button类的子类
class HelloButton(Button):
     def __init__(self, master=None, **config):
         Button.__init__(self, master, **config)
         self.pack()
         self.config(command=self.callback)
#          self.callback()
         
        
#          self.config(command=self.callback)
         
     def callback(self):
         print("Goodbye world....")
         self.quit()

# if __name__ == "__main__":
#     root = Tk()
#     HelloButton(text="Hello subclass world").mainloop()
root = Tk()
# HelloButton(root, text="Hello subclass world")
mainloop()

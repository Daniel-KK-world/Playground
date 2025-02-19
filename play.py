from tkinter import* 
from tkinter import messagebox
def click():
    #messagebox.showinfo(title='This is an info messagebox', message="You are a person")
    #messagebox.showwarning(title='This is a warning msg', message='The end is near')
    #messagebox.showerror(title='This is an error message', message='something went wrong :(' )
    
    #if messagebox.askokcancel(title='ask ok cancel', message='Do u want to do the thing? '):
        #print('You did a thing')
    #else:
        #print('You cancelled a thing.')
    #if messagebox.askretrycancel(title='ask retry cancel', message='Do you want to retry the thing?'):
        #print('You retried a thing')
    #else: 
        #print("You cancelled a thing.")
    #if messagebox.askyesno(title='ask yes or no', message='Do you like cake?'):
        #print('I like cake too.')
    #else:
        #print('why do u not like cake?')
    #answer = messagebox.askquestion(title='ask question', message='Do u like pie?')
    #if answer == 'yes':
        #print('I like pie too')
    #else: 
        #print('Y do u not like pie?')


window = Tk()


button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
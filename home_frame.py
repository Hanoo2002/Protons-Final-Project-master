from tkinter import *
from Algorithm import *
import calendar

create_table()


def raise_frame(parent):
    parent.tkraise()

root = Tk()

Home = Frame(root)
AddActivity = Frame(root)
AddCategory = Frame(root)
EditActivity = Frame(root)
EditCategory = Frame(root)
Calendar = Frame(root)
Todo = Frame(root)
Today = Frame(root)
Now = Frame(root)


for frame in (Home, AddActivity, AddCategory, EditActivity, EditCategory, Calendar, Todo, Today, Now):
    frame.grid(row=0, column=0, sticky='news')


def home_frame_build():
    def destroy_pop_up(parent,pop_up):
        raise_frame(parent)
        pop_up.destroy()

    class Edit:
        def __init__(self, parent):
            top = self.top = Toplevel(parent)

            Label(top, text="Edit").pack()

            Label(top, text='What do you want to edit?')

            cate = Button(top, text="Category", command=lambda: destroy_pop_up(EditCategory,top))
            cate.pack(pady=5, padx=5, side=LEFT)

            activity = Button(top, text="Activity", command=lambda: destroy_pop_up(EditActivity,top))
            activity.pack(pady=5, padx=5, side=LEFT)


    def edit():
        ed = Edit(Home)
        Home.wait_window(ed.top)


    class Add:
        def __init__(self, parent):
            top = self.top = Toplevel(parent)

            Label(top, text="Add").pack()

            Label(top, text='What do you want to add?')

            cat = Button(top, text="Category", command=lambda: destroy_pop_up(AddCategory,top))
            cat.pack(pady=5, padx=5, side=LEFT)

            act = Button(top, text="Activity", command=lambda: destroy_pop_up(AddActivity,top))
            act.pack(pady=5, padx=5, side=LEFT)


    def add():
        ad = Add(Home)
        Home.wait_window(ad.top)

    TopFrame = Frame(Home)
    MiddleFrame = Frame(Home, padx=200)
    BottomFrame = Frame(Home)
    LastFrame_Home = Frame(Home)

    TopFrame.pack(side='top', fill=X)
    MiddleFrame.pack(side='top', ipady=5, fill=X)
    BottomFrame.pack(side='top', ipady=5, fill=X)
    LastFrame_Home.pack(side='top', ipady=5, fill=X)

    HomeLabel = Label(TopFrame, text='Home')
    HomeLabel.pack(side=LEFT)

    AddButton = Button(TopFrame, text='Add', command=add)
    AddButton.pack(side=RIGHT)

    CalendarButton = Button(MiddleFrame, text='Calendar', command=lambda: raise_frame(Calendar))
    CalendarButton.pack(padx=5, pady=10, side=LEFT)

    TodoButton = Button(MiddleFrame, text='Todo', command=lambda: raise_frame(Todo))
    TodoButton.pack(padx=5, pady=10, side=LEFT)

    TodayButton = Button(MiddleFrame, text='Today', command=lambda: raise_frame(Today))
    TodayButton.pack(padx=5, pady=10, side=LEFT)

    NowButton = Button(MiddleFrame, text='Now', command=lambda: raise_frame(Now))
    NowButton.pack(padx=5, pady=10, side=LEFT)


    category_name = strainer('name', 'sort', 'category')
    number = 0
    # if category_name[number][0]
    for i in range(0, len(category_name)):
        if number == 10:
            break
        CategoryButton = Button(BottomFrame, text='{}'.format(category_name[number][0]), width=5, anchor="w")
        CategoryButton.pack(padx=5, pady=5, fill=X)
        number += 1

    EditButton = Button(LastFrame_Home, text='Edit', command=edit)
    EditButton.pack()
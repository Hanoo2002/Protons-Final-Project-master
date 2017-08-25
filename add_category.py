from add_activity import *


def back():
    raise_frame(Home)


def build_add_category_frame():

    NameFrame = Frame(AddCategory)
    PriorityFrame = Frame(AddCategory)
    LastFrame_AddCategory = Frame(AddCategory)

    NameFrame.pack(side='top', fill=X, ipady=5)
    PriorityFrame.pack(side='top', ipady=5, fill=X, padx=200)
    LastFrame_AddCategory.pack(side='top', fill=X)

    NameLabel = Label(NameFrame, text='Name: ')
    NameLabel.pack(side=LEFT)

    event_name = Entry(NameFrame, fg='grey')
    event_name.insert(0, "Enter the name of your event ...", )
    event_name.bind('<FocusIn>', on_entry_click)
    event_name.pack(ipadx=25, side=LEFT)

    Importance = IntVar()
    Label(PriorityFrame,text='What is its priority? 1-Best').pack(side=LEFT)
    Radiobutton(PriorityFrame, text='1', variable=Importance, value=1).pack(side=LEFT, padx=5)
    Radiobutton(PriorityFrame, text='2', variable=Importance, value=2).pack(side=LEFT, padx=5)
    Radiobutton(PriorityFrame, text='3', variable=Importance, value=3).pack(side=LEFT, padx=5)
    Radiobutton(PriorityFrame, text='4', variable=Importance, value=4).pack(side=LEFT, padx=5)
    Radiobutton(PriorityFrame, text='5', variable=Importance, value=5).pack(side=LEFT, padx=5)




    def insert():
        insert_category(event_name.get(), Importance.get())
        raise_frame(Home)




    Insert_AddCategory = Button(LastFrame_AddCategory, text='Insert', command=insert).pack(side=LEFT, ipadx=20)
    Back_AddCategory = Button(LastFrame_AddCategory, text='Back', command=back).pack(side=LEFT, ipadx=20)
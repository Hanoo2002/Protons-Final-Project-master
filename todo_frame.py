from edit_activity import *

def build_todo_frame():
    right_todoframe = Frame(Todo,width = 320,height = 350)
    right_todoframe.grid(row = 0)


    left_todoframe = Frame(Todo,width = 320,height = 350)
    left_todoframe.grid(row = 0,column = 1)

    Back_Todo = Button(right_todoframe, text='Back', command=back)
    Back_Todo.place(relx = .04,rely = .9)

    todo_listM = strainer('name', 'sort','event')
    todo_list_timefrmM = strainer('frm', 'sort','event')
    todo_list_timetoM = strainer('till', 'sort','event')
    print(todo_list_timefrmM)
    xv1 = .2
    yv1 = .1

    for i in range(len(todo_listM)):
        todo_listM[i] = Checkbutton(right_todoframe,text = todo_listM[i])

        todo_listM[i].place(relx = xv1,rely = yv1)


        todo_list_timefrmM[i] = Label(left_todoframe,text = todo_list_timefrmM[i])

        todo_list_timefrmM[i].place(relx=xv1, rely=yv1)

        labelmark = Label(left_todoframe,text = ".")
        labelmark.place(relx=xv1+.05, rely=yv1)

        todo_list_timetoM[i] = Label(left_todoframe, text=todo_list_timetoM[i])

        todo_list_timetoM[i].place(relx=xv1+.08, rely=yv1)

        if todo_listM[i].config(state = "active"):
            done(todo_listM[i])

        yv1 += .1

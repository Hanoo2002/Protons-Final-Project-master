from edit_category import*
def build_today_frame():
    right_todayframe = Frame(Today, width=320, height=350)
    right_todayframe.grid(row=0)


    left_todayframe = Frame(Today, width=320, height=350)
    left_todayframe.grid(row=0, column=1)


    Back_Today = Button(right_todayframe, text='Back', command=back)
    Back_Today.place(relx=.04, rely=.9)

    # events_list = strainer("","event","sort")

    search_box1 = Entry(right_todayframe, width=40)
    search_box1.insert(0, "Search")
    search_box1.place(relx=.05, rely=.05)

    search_button1 = Button(right_todayframe, text="Search")
    search_button1.place(relx=.83, rely=.048)

    seached_item = search_box1.get()

    # today_listM = strainer('name','sort','event')
    # today_listM.extend(strainer('name','sort','todo'))

    today_listM = organizeM()

    today_list_timefrmM = strainer('frm', 'sort', 'event')
    today_list_timetoM = strainer('till', 'sort', 'event')

    xv2 = .05
    yv2 = .15

    for i in range(len(today_listM)):
        today_listM[i] = Checkbutton(right_todayframe, text=str(today_listM[i])[2:(len(str(today_listM[i])) - 3)])

        today_listM[i].place(relx=xv2, rely=yv2)
        yv2 += .1
    for i in range(len(today_list_timefrmM)):

        if today_list_timefrmM[i] in today_list_timetoM or today_list_timefrmM[i] > today_list_timetoM[i]:
            popup1 = Frame(Home)

            label1 = Label(popup1, text="you have two events at the same time. please select one of them to have")

            raise_frame(popup1)

    # sbar = Scrollbar(right_todayframe).pack(side = LEFT,fill = Y)
    # sbaror = Listbox(right_todayframe,yscrollcommand = sbar.set)




    def do_search(event):
        if seached_item in today_listM:
            seached_item_widget = Checkbutton(right_todayframe, text=seached_item)
            seached_item_widget.place(relx=xv2, rely=yv2)
        else:
            seached_item_widget = Label(right_todayframe, text="Nothing found")
            seached_item_widget.place(relx=.15, rely=.15)

    search_button1.bind("<Button-1>", do_search)
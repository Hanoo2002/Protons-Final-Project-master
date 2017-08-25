from home_frame import  *

def delete_something(string):
    delete(string)
    back()
    print(string)

def build_activity_frame():
    EditActivityFrame = Frame(EditActivity)
    EditActivityFrame.pack(side='top', fill=X)
    middle_activity_frame=Frame(EditActivity)
    middle_activity_frame.pack(side='top',fill=Y)

    category_names = []

    category_name = strainer('name', 'sort', 'activities')
    number = 0

    for x in range(0, len(category_name)):
        category_names.append(category_name[number][0])
        number += 1


    def check():
        print(category_names)

    Button(middle_activity_frame,text='check',command=check).pack()
    Back_EditActivity = Button(middle_activity_frame, text='Back', command=back).pack(side=LEFT, ipadx=20)
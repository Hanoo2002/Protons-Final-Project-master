from home_frame import  *

def delete_something(string):
    delete(string)
    back()
    print(string)

def build_activity_frame():
    EditActivityFrame = Frame(EditActivity)
    EditActivityFrame.pack(side='top', fill=X)

    Label(EditActivityFrame,text="Enter the name of the activity you want to edit").pack(side=LEFT)
    name_of_edited_actvity=Entry(EditActivityFrame)
    name_of_edited_actvity.pack(side=LEFT)
    Label(EditActivityFrame,text='Change its name into(optional if deleting):').pack(side=LEFT)
    change_to=Entry(EditActivityFrame)
    change_to.pack(side=LEFT)

    def change(frm,to):
        edit_anything(frm,'name',to)
        back()

    Button(EditActivityFrame,text='Change',command=lambda :change(name_of_edited_actvity.get(),change_to.get())).pack(side=RIGHT)
    Back_EditActivity = Button(EditActivityFrame, text='Back', command=back).pack(side=RIGHT)
    Button(EditActivityFrame,text='Delete',command=delete_something(name_of_edited_actvity.get())).pack(side=RIGHT)
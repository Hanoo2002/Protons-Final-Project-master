from edit_category import *

# Home Frame
home_frame_build()

# AddActivity Frame
# The layout is divided in many frames
build_add_activity_frame()

# AddCategory Frame
build_add_category_frame()

########################################################################################################################
# EditActivity Frame todo

EditActivityFrame = Frame(EditActivity)
EditActivityFrame.pack(side='top', fill=X)

Back_EditActivity = Button(EditActivityFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)
# Edit_EditActivity = Button(EditActivityFrame, text='Edit', command=back).pack(side=LEFT, ipadx=20)
# Functions you will use: edit, done, delete, del_done, strainer
########################################################################################################################
# EditCategory Frame
build_edit_category_frame()

########################################################################################################################
# Calendar Frame todo

LastFrame = Frame(Calendar)
LastFrame.pack(side='top', fill=X)

Back_Calendar = Button(LastFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here the user should see all of his events
# Functions you will use: strainer, done
########################################################################################################################
# To-do Frame todo

LastFrame_Todo = Frame(Todo)
LastFrame_Todo.pack(side='top', fill=Y)

Todos=strainer('name','sort','activities')
Todo_list=[]
number=0


Back_Todo = Button(LastFrame_Todo, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Here the user should see all of his To-do
# Functions you will use: strainer, done
########################################################################################################################
# Today Frame

LastFrame_Today = Frame(Today)
LastFrame_Today.pack(side='top', fill=X)

Back_Today = Button(LastFrame_Today, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Functions you will use: strainer, organize(propabily you will need to make an extra db for this)
########################################################################################################################
# Now Frame

LastFrame_Now = Frame(Now)
LastFrame_Now.pack(side='top', fill=X)

Back_Now = Button(LastFrame_Now, text='Back', command=back).pack(side=LEFT, ipadx=20)

# Functions you will use: strainer(propabily you will need to make an extra db for this)

raise_frame(Home)
root.mainloop()

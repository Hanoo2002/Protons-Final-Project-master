from todo_frame import *

def build_edit_category_frame():
    LastFrame = Frame(EditCategory)
    LastFrame.pack(side='top', fill=X)

    category_names = []

    category_name = strainer('name', 'sort', 'category')
    number = 0

    for x in range(0, len(category_name)):
        category_names.append(category_name[number][0])
        number += 1

    Category_1 = StringVar(LastFrame)

    option = OptionMenu(LastFrame, Category_1, *category_names)
    option.pack(fill=X, pady=5)

    def option_changed():
        deleted_or_edited = Category_1.get()
        return deleted_or_edited

    Back_EditCategory = Button(LastFrame, text='Back', command=back).pack(side=LEFT, ipadx=20)
    Insert_EditCategory = Button(LastFrame, text='Delete', command=lambda: delete_something(option_changed()))
    Insert_EditCategory.pack(side=LEFT, ipadx=20)
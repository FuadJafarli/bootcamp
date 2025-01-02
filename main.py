from tkinter import *
from PIL import ImageTk, Image
from json import *
from tkinter import messagebox
from tkinter import ttk

window = Tk()
window.title("Freelance")
window.geometry("1200x700+200+150")
window.resizable(False, False)


# def Color(button,on,off):
#     button.bind("<Enter>",func=lambda e:button.config(background=on))
#     button.bind("<Leave>",func= lambda e: button.config(background=off))


def StartFrame():
    # control
    def login():
        LoginFrame()

    start_frame = Frame(window, width=1200, height=700, bg="#213555")
    start_frame.place(x=0, y=0)

    image = Image.open("freelance.jpg")
    resize_image = image.resize((600, 700))
    img = ImageTk.PhotoImage(resize_image)

    label1 = Label(image=img)
    label1.image = img
    label1.place(x=0, y=0)

    welcome_label = Label(start_frame, text="HI! Welcome to the freelancejobfinder")
    welcome_label.config(bg="#213555",
                         fg="#F5EFE7",
                         font=("Comic Sans MS", 20, "bold"))
    welcome_label.place(x=650, y=100)

    daxil_ol = Button(start_frame, text="Enter Site", command=login)
    daxil_ol.config(bg="#6d9384",
                    fg="#f4f0e4",
                    width=25,
                    height=2,
                    border=1,
                    activebackground="#f4f0e4",
                    activeforeground="#3E5879",
                    )
    daxil_ol.place(x=800, y=400)

    # glowingbutton=Button(start_frame,bg="yellow")
    # glowingbutton.pack()
    # Color(glowingbutton,"red","yellow")
    # glowingbutton.place(x=900, y=600)


def LoginFrame():
    def back():
        StartFrame()

    def next():
        SigninFrame()

    def signin():
        login = enteruser.get()
        password = enterpass.get()
        print(f"login: {login} ---> password: {password}")
        with open("sitesiyahi.json", "r") as file:
            reg = load(file)
        for i in reg:
            if i != []:
                if login == "admin" and password == "admin":
                    FirstFrameAdmin()
                    return
                else:
                    if i[0] == login:
                        if i[1] == password:
                            FirstFrame()
                            return

        messagebox.showerror(title="Error", message=f"Error in either username or password")

    def checkbutton():
        if deyishen.get() == 1:
            enterpass.config(show="")
        else:
            enterpass.config(show="*")

    login_frame = Frame(window, width=1200, height=700, bg="#213555")
    login_frame.place(x=0, y=0)

    reg_label = Label(login_frame, text="Login")
    reg_label.config(bg="#213555",
                     fg="#F5EFE7",
                     font=("Comic Sans MS", 24, "bold")
                     )
    reg_label.place(x=450, y=100)

    username = Label(text="Username")
    username.config(font=('Comic Sans MS', 18), fg='#6d9384', bg='#213555')
    username.place(x=450, y=170)

    enteruser = Entry(login_frame)
    enteruser.config(width=15, font=("calibri", 18))
    enteruser.place(x=450, y=210)

    password = Label(text="Password")
    password.config(font=('Comic Sans MS', 18), fg='#6d9384', bg='#213555')
    password.place(x=450, y=250)

    enterpass = Entry(login_frame)
    enterpass.config(width=15, font=("calibri", 18), show="*")
    enterpass.place(x=450, y=290)

    back_btn = Button(login_frame, text="Back", command=back)
    back_btn.config(bg="#ff0000",
                    fg="#f4f0e4",
                    width=10,
                    height=2,
                    border=1,
                    activebackground="#f4f0e4",
                    activeforeground="#3E5879"
                    )
    back_btn.place(x=0, y=0)

    deyishen = IntVar()
    check_button = Checkbutton(variable=deyishen, command=checkbutton, width=1, bg="green", activebackground="orange")
    check_button.place(x=650, y=290)

    login = Button(login_frame, text="Login", command=signin)
    login.config(bg="#6d9384",
                 fg="#f4f0e4",
                 width=25,
                 height=2,
                 border=1,
                 activebackground="#f4f0e4",
                 activeforeground="#3E5879",
                 )
    login.place(x=450, y=350)

    signin = Button(login_frame, text="Don't have an account?", command=next)
    signin.config(bg="#213555",
                  fg="#f4f0e4",
                  width=25,
                  height=2,
                  border=0,
                  activebackground="#213555",
                  activeforeground="#3E5879",
                  )
    signin.place(x=450, y=400)


def SigninFrame():
    def checkbutton():
        if deyishen.get() == 1:
            enterpass.config(show="")
        else:
            enterpass.config(show="*")

    def Signup():

        if enteruser.get() == "" or enterpass.get() == "" or enterpass2.get() == "":
            messagebox.showerror(title="error", message="Can not be empty")
        elif enterpass.get() != enterpass2.get():
            messagebox.showerror(title="error", message="Error in password repeat")
        else:
            with open("sitesiyahi.json", "r") as file:
                reg_file = load(file)
            new_list = []
            login = enteruser.get()
            password2 = enterpass.get()

            for i in reg_file:
                if i != []:
                    if i[0] == login:
                        messagebox.showinfo(title="Hint", message="This username is existing")
                        LoginFrame()
                        return

            new_list.append(login)
            new_list.append(password2)

            reg_file.append(new_list)

            with open("sitesiyahi.json", "w") as file:
                dump(reg_file, file)

            enteruser.delete(0, END)
            enterpass.delete(0, END)
            enterpass2.delete(0, END)
            messagebox.showinfo(title="✅", message="Registration is done")
            LoginFrame()

    login_frame = Frame(window, width=1200, height=700, bg="#213555")
    login_frame.place(x=0, y=0)

    username = Label(text="Username")
    username.config(font=('Comic Sans MS', 18), fg='#6d9384', bg='#213555')
    username.place(x=450, y=170)

    enteruser = Entry()
    enteruser.config(width=15, font=("calibri", 18))
    enteruser.place(x=450, y=210)

    password = Label(text="Password")
    password.config(font=('Comic Sans MS', 18), fg='#6d9384', bg='#213555')
    password.place(x=450, y=250)

    enterpass = Entry()
    enterpass.config(width=15, font=("calibri", 18), show="*")
    enterpass.place(x=450, y=290)

    deyishen = IntVar()
    check_button = Checkbutton(variable=deyishen, command=checkbutton, width=1, bg="green", activebackground="orange")
    check_button.place(x=650, y=290)

    password = Label(text="Repeat Password")
    password.config(font=('Comic Sans MS', 18), fg='#6d9384', bg='#213555')
    password.place(x=450, y=330)

    enterpass2 = Entry()
    enterpass2.config(width=15, font=("calibri", 18), show="*")
    enterpass2.place(x=450, y=370)

    reg_label = Label(login_frame, text="SIGN UP")
    reg_label.config(bg="#213555",
                     fg="#F5EFE7",
                     font=("Comic Sans MS", 24, "bold"))
    reg_label.place(x=450, y=100)

    signup = Button(login_frame, text="Sign up ", command=Signup)
    signup.config(bg="#6d9384",
                  fg="#f4f0e4",
                  width=25,
                  height=2,
                  border=1,
                  activebackground="#f4f0e4",
                  activeforeground="#3E5879",
                  )
    signup.place(x=450, y=430)

    back_btn = Button(login_frame, text="Back", command=LoginFrame)
    back_btn.config(bg="#ff0000",
                    fg="#f4f0e4",
                    width=10,
                    height=2,
                    border=1,
                    activebackground="#f4f0e4",
                    activeforeground="#3E5879",
                    )
    back_btn.place(x=0, y=0)


def FirstFrameAdmin():
    with open("jobs_list.json", "r") as file:
        jobs = load(file)

    def deljob():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)

        jobname = del_entry.get()
        count = 0

        newfile = []

        for job in jobs:
            if job != []:
                if job[0] == jobname:
                    count += 1
                else:
                    newfile.append(job)
        del_entry.delete(0, END)

        for item in tree.get_children():
            tree.delete(item)

        with open("jobs_list.json", "w") as file:
            dump(newfile, file)

        for file in newfile:
            if file != "":
                tree.insert("", END, values=file)

        if count == 0:
            messagebox.showerror(title="error", message=f"{jobname} does not exist")

    def add():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)
        newjob = []
        newjob.append(entry1.get().capitalize())
        newjob.append(entry2.get().capitalize())
        newjob.append(entry3.get().capitalize())
        newjob.append(entry4.get())
        newjob.append(entry5.get())

        if entry1.get() == "" or entry2.get() == "" or entry3.get() == "" or entry4.get() == "" or entry5.get() == "":
            messagebox.showerror(title="Error", message="Invalid syntax")
            return FirstFrameAdmin()
        elif entry4.get().isdigit() == False or entry5.get().isdigit() == False:
            messagebox.showerror(title="Error", message="Wage and work hours must be digits")
            return FirstFrameAdmin()

        jobs.append(newjob)

        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)

        with open("jobs_list.json", "w") as file:
            dump(jobs, file)

        for item in tree.get_children():
            tree.delete(item)

        for job in jobs:
            if job != "":
                tree.insert("", END, values=job)

    def findjob():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)

        count = 1

        jobname = del_entry.get()
        for job in jobs:
            if job != 0:
                if job[0] == jobname:
                    count += 1
                    messagebox.showinfo(title=f"{jobname}",
                                        message=f"Job software: {job[1]}\nCompany: {job[2]}\nWage: {job[3]}\nWork hours: {job[4]}")

        if count == 0:
            messagebox.showwarning(message=f"This job could not be found")

    def sort():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)

        sorted_jobs = sorted(jobs, key=lambda x: x[0])

        with open("jobs_list.json", "w") as file:
            dump(sorted_jobs, file)

        for item in tree.get_children():
            tree.delete(item)

        for jobs in sorted_jobs:
            tree.insert("", END, values=jobs)

    def edit():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)
            jobname = del_entry.get()
            for job in jobs:
                if job != 0:
                    if job[0] == jobname:
                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        entry3.delete(0, END)
                        entry4.delete(0, END)
                        entry5.delete(0, END)

                        entry1.insert(0, job[0])
                        entry2.insert(0, job[1])
                        entry3.insert(0, job[2])
                        entry4.insert(0, job[3])
                        entry5.insert(0, job[4])

    def edit2():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)
            jobname = del_entry.get()
            for job in jobs:
                if job != 0:
                    if job[0] == jobname:
                        job[0] = entry1.get()
                        job[1] = entry2.get()
                        job[2] = entry3.get()
                        job[3] = entry4.get()
                        job[4] = entry5.get()

                        entry1.delete(0, END)
                        entry2.delete(0, END)
                        entry3.delete(0, END)
                        entry4.delete(0, END)
                        entry5.delete(0, END)
        del_entry.delete(0, END)

        with open("jobs_list.json", "w") as file:
            dump(jobs, file)

        for item in tree.get_children():
            tree.delete(item)

        for job in jobs:
            if job != "":
                tree.insert("", END, values=job)

    first_frame = Frame(window, width=1200, height=700, bg="#89cff0")
    first_frame.place(x=0, y=0)

    columns = ("name", "software", "company", "wage", "work")

    welcome_label = Label(first_frame, text="Freelance jobs")
    welcome_label.config(bg="#89cff0", fg="#d5ff87", font=("Calibri", 24, "bold"))
    welcome_label.place(x=450, y=10)

    back_btn = Button(first_frame, text="Back", command=LoginFrame)
    back_btn.config(bg="#ff0000",
                    fg="#f4f0e4",
                    width=10,
                    height=2,
                    border=1,
                    activebackground="#f4f0e4",
                    activeforeground="#3E5879"
                    )
    back_btn.place(x=0, y=662)

    tree = ttk.Treeview(first_frame, columns=columns, show="headings")
    tree.place(x=10, y=10)

    tree.heading("name", text="Job name")
    tree.heading("software", text="Job software")
    tree.heading("company", text="Company")
    tree.heading("wage", text="Wage")
    tree.heading("work", text="Work hours")

    for job in jobs:
        tree.insert("", END, values=job)

    entry1 = Entry(first_frame)
    entry1.place(x=20, y=290)

    entry2 = Entry(first_frame)
    entry2.place(x=200, y=290)

    entry3 = Entry(first_frame)
    entry3.place(x=420, y=290)

    entry4 = Entry(first_frame)
    entry4.place(x=630, y=290)

    entry5 = Entry(first_frame)
    entry5.place(x=850, y=290)

    del_entry = Entry(first_frame)
    del_entry.place(x=20, y=250)

    del_btn = Button(first_frame, text="delete", command=deljob)
    del_btn.config(width=5)
    del_btn.place(x=160, y=250)

    find_btn = Button(first_frame, text="find", command=findjob)
    find_btn.config(width=5)
    find_btn.place(x=220, y=250)

    sort_btn = Button(first_frame, text="sort", command=sort)
    sort_btn.config(width=5)
    sort_btn.place(x=280, y=250)

    sort_btn = Button(first_frame, text="edit", command=edit)
    sort_btn.config(width=5)
    sort_btn.place(x=340, y=250)

    add_btn = Button(first_frame, text="add", command=add)
    add_btn.place(x=1000, y=290)

    add_btn = Button(first_frame, text="change", command=edit2)
    add_btn.place(x=1050, y=290)


def FirstFrame():
    with open("jobs_list.json", "r") as file:
        jobs = load(file)

    def findjob():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)

        jobname = find_entry.get()
        count = 0
        for job in jobs:
            if job != 0:
                if job[0] == jobname:
                    count += 1
                    label = Label(first_frame, text=f"{job[1]}\t{job[2]}\t{job[3]}\t{job[4]}")
                    label.config(bg="#89cff0", font=("Calibri", 18, "bold"))
                    label.place(x=10, y=400)

    def sort():
        with open("jobs_list.json", "r") as file:
            jobs = load(file)

        sorted_jobs = sorted(jobs, key=lambda x: x[0])

        with open("jobs_list.json", "w") as file:
            dump(sorted_jobs, file)

        for item in tree.get_children():
            tree.delete(item)

        for jobs in sorted_jobs:
            tree.insert("", END, values=jobs)

    first_frame = Frame(window, width=1200, height=700, bg="#89cff0")
    first_frame.place(x=0, y=0)

    columns = ("name", "software", "company", "wage", "work")

    welcome_label = Label(first_frame, text="Freelance jobs")
    welcome_label.config(bg="#89cff0", fg="#d5ff87", font=("Calibri", 24, "bold"))
    welcome_label.place(x=450, y=10)

    back_btn = Button(first_frame, text="Back", command=LoginFrame)
    back_btn.config(bg="#ff0000",
                    fg="#f4f0e4",
                    width=10,
                    height=2,
                    border=1,
                    activebackground="#f4f0e4",
                    activeforeground="#3E5879"
                    )
    back_btn.place(x=0, y=662)

    tree = ttk.Treeview(first_frame, columns=columns, show="headings")
    tree.place(x=10, y=10)

    tree.heading("name", text="Job name")
    tree.heading("software", text="Job software")
    tree.heading("company", text="Company")
    tree.heading("wage", text="Job wage")
    tree.heading("work", text="Work hours")

    for job in jobs:
        tree.insert("", END, values=job)

    find_entry = Entry(first_frame)
    find_entry.place(x=20, y=250)

    find_btn = Button(first_frame, text="find", command=findjob)
    find_btn.config(width=5)
    find_btn.place(x=220, y=250)

    sort_btn = Button(first_frame, text="sort", command=sort)
    sort_btn.config(width=5)
    sort_btn.place(x=280, y=250)


# FirstFrameAdmin()
StartFrame()
window.mainloop()
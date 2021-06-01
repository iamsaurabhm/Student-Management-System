import collections
from tkinter import *
from tkinter import ttk
import pymysql

class StudentManagementSystem:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#004c4c")

        #=====Title===========
        title = Label(root, text="Student Management System", font=("bankgothic", 30), bg="teal", pady=5, bd=4, relief=GROOVE)
        title.pack(fill=X, side=TOP)

        #=====Defining variable=========
        self.regt = StringVar()
        self.name = StringVar()
        self.roll = StringVar()
        self.gender = StringVar()
        self.email = StringVar()
        self.contact = StringVar()
        self.dob = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()
        

        
        #======================Input student details frame=========================
        inp_f = Frame(root, bd=3, relief=GROOVE, bg="teal" )
        inp_f.place(x=30, y=80, width=380, height=557)

        # Enter students detail
        sdet_lbl = Label(inp_f, text="Students Detail", font=("azonix", 15), bg="teal")
        sdet_lbl.grid(row=0, columnspan=2, padx=76, pady=15)

        sreg_lbl = Label(inp_f, text="Regt No.", font=("times new roman", 15), bg="teal")
        sreg_lbl.grid(row=1, column=0, padx=25, pady=10, sticky="w")
        sreg_txt = Entry(inp_f, textvariable=self.regt, font=("times new roman", 12), bd=2, relief=SUNKEN)
        sreg_txt.grid(row=1, column=1, sticky="w", padx=25, pady=10,)
        
        sname_lbl = Label(inp_f, text="Name", font=("times new roman", 15), bg="teal")
        sname_lbl.grid(row=2, column=0, padx=25, pady=10, sticky="w")
        sname_txt = Entry(inp_f, textvariable=self.name, font=("times new roman", 12), bd=2, relief=SUNKEN)
        sname_txt.grid(row=2, column=1, sticky="w", padx=25, pady=10,)


        sroll_lbl = Label(inp_f, text="Roll No.", font=("times new roman", 15), bg="teal")
        sroll_lbl.grid(row=3, column=0, padx=25, pady=10, sticky="w")
        sroll_txt = Entry(inp_f, textvariable=self.roll, font=("times new roman", 12), bd=2, relief=SUNKEN)
        sroll_txt.grid(row=3, column=1, sticky="w", padx=25, pady=10,)

        sgen_lbl = Label(inp_f, text="Gender", font=("times new roman", 15), bg="teal")
        sgen_lbl.grid(row=4, column=0, padx=25, pady=10, sticky="w")

        cmbo_gen = ttk.Combobox(inp_f, textvariable=self.gender, font=("times new roman", 12), width=18, state="readonly")
        cmbo_gen['values'] = ("Male", "Female", "transgender")
        cmbo_gen.grid(row=4, column=1)

        semail_lbl = Label(inp_f, text="Email", font=("times new roman", 15), bg="teal")
        semail_lbl.grid(row=5, column=0, padx=25, pady=10, sticky="w")
        semail_txt = Entry(inp_f, textvariable=self.email, font=("times new roman", 12), bd=2, relief=SUNKEN)
        semail_txt.grid(row=5, column=1, sticky="w", padx=25, pady=10,) 

        scon_lbl = Label(inp_f, text="Contact No.", font=("times new roman", 15), bg="teal")
        scon_lbl.grid(row=6, column=0, padx=25, pady=10, sticky="w")
        scon_txt = Entry(inp_f, textvariable=self.contact, font=("times new roman", 12), bd=2, relief=SUNKEN)
        scon_txt.grid(row=6, column=1, sticky="w", padx=25, pady=10,)    

        sdob_lbl = Label(inp_f, text="D.O.B", font=("times new roman", 15), bg="teal")
        sdob_lbl.grid(row=7, column=0, padx=25, pady=10, sticky="w")
        sdob_txt = Entry(inp_f, textvariable=self.dob, font=("times new roman", 12), bd=2, relief=SUNKEN)
        sdob_txt.grid(row=7, column=1, sticky="w", padx=25, pady=10,) 

        sadrs_lbl = Label(inp_f, text="Address", font=("times new roman", 15), bg="teal")
        sadrs_lbl.grid(row=8, column=0, padx=25, pady=10, sticky="w")
        self.sadrs_txt = Text(inp_f, font=("times new roman", 12), width=20, height=3)
        self.sadrs_txt.grid(row=8, column=1, sticky="w", padx=25, pady=10,)

        #Button Frame
        bt_f = Frame(inp_f, bd=3, relief=GROOVE, bg="teal" )
        bt_f.place(x=2, y=483, width=370, height=50)

        add_btn = Button(bt_f, command=self.add_stu, text="ADD", width=9, bd=3, )
        add_btn.place(x=15, y=9)

        updt_btn = Button(bt_f, command=self.update_data, text="UPDATE", width=9, bd=3, )
        updt_btn.place(x=102, y=9)

        del_btn = Button(bt_f, command=self.delete_data, text="DELETE", width=9, bd=3, )
        del_btn.place(x=188, y=9)

        clr_btn = Button(bt_f, command=self.clear, text="CLEAR", width=9, bd=3, )
        clr_btn.place(x=274, y=9)


        #==========================Students list frame=========================
        list_f = Frame(root, bd=3, relief=GROOVE, bg="teal" )
        list_f.place(x=450, y=80, width=792, height=557)

        srch_lbl = Label(list_f, text="Search By", font=("times new roman", 18), bg="teal")
        srch_lbl.grid(row=0, column=0, padx=20, pady=15)

        cmbo_srch = ttk.Combobox(list_f, textvariable=self.search_by, font=("times new roman", 14), width=14, state="readonly")
        cmbo_srch['values'] = ("Name", "Email", "Regt")
        cmbo_srch.grid(row=0, column=1)

        srch_txt = Entry(list_f, textvariable=self.search_txt, font=("times new roman", 12),  bd=3, relief=SUNKEN)
        srch_txt.grid(row=0, column=2,padx=25)
        
        srch_btn = Button(list_f, command=self.search_data, text="Search", font=("times new roman", 10), width=12)
        srch_btn.grid(row=0, column=3)

        showallbtn = Button(list_f, command=self.fetch_data, text="Show All", font=("times new roman", 10), width=12)
        showallbtn.grid(row=0, column=5, padx=20, pady=20)

        #========tabular list of students details===============
        tab_frame = Frame(list_f, bd=4, relief=RIDGE)
        tab_frame.place(x=20, y=70, width=750, height=482)

        scroll_x = Scrollbar(tab_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(tab_frame, orient=VERTICAL)
        self.stu_table = ttk.Treeview(tab_frame, columns=("regt", "name", "roll no", "gender", "email", "contact", "dob", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.stu_table.xview)
        scroll_y.config(command=self.stu_table.yview)
        self.stu_table.heading("regt", text="Regt No.")
        self.stu_table.heading("name", text="Name")
        self.stu_table.heading("roll no", text="Roll No")
        self.stu_table.heading("gender", text="Gender")
        self.stu_table.heading("email", text="Email")
        self.stu_table.heading("contact", text="Contact")
        self.stu_table.heading("dob", text="D.O.B")
        self.stu_table.heading("address", text="Address")
        self.stu_table['show'] = 'headings'
        self.stu_table.column("regt", width=80)
        self.stu_table.column("name", width=150)
        self.stu_table.column("roll no", width=80 )
        self.stu_table.column("gender", width=100)
        self.stu_table.column("email", width=150)
        self.stu_table.column("contact", width=100)
        self.stu_table.column("dob",width=100)
        self.stu_table.column("address", )
        self.stu_table.pack(fill=BOTH, expand=1)
        self.stu_table.bind("<ButtonRelease-1>", self.get_detail)

        self.fetch_data()
        

    def add_stu(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("insert into students_detail (regt, name, roll, gender, email, contact, dob, address) values(%s,%s,%s,%s,%s,%s,%s,%s)",
                                                                            (self.regt.get(),
                                                                             self.name.get(),
                                                                             self.roll.get(),
                                                                             self.gender.get(),
                                                                             self.email.get(),
                                                                             self.contact.get(),
                                                                             self.dob.get(),
                                                                             self.sadrs_txt.get('1.0', END)
                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        
        con.close()
    
    def clear(self):
        self.regt.set(""),
        self.name.set(""),
        self.roll.set(""),
        self.gender.set(""),
        self.email.set(""),
        self.contact.set(""),
        self.dob.set(""),
        self.sadrs_txt.delete('1.0',END)

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students_detail")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for row in rows:
                self.stu_table.insert('', END, value=row)
            con.commit()
        con.close()

    def get_detail(self, event):
        cursor_row = self.stu_table.focus()
        content = self.stu_table.item(cursor_row)
        row = content['values']
        self.regt.set(row[0]),
        self.name.set(row[1]),
        self.roll.set(row[2]),
        self.gender.set(row[3]),
        self.email.set(row[4]),
        self.contact.set(row[5]),
        self.dob.set(row[6]),
        self.sadrs_txt.delete('1.0',END),
        self.sadrs_txt.insert(END, row[7])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("update students_detail set name=%s, roll=%s, gender=%s, email=%s, contact=%s, dob=%s, address=%s where regt=%s",
                                                                            (
                                                                             self.name.get(),
                                                                             self.roll.get(),
                                                                             self.gender.get(),
                                                                             self.email.get(),
                                                                             self.contact.get(),
                                                                             self.dob.get(),
                                                                             self.sadrs_txt.get('1.0', END),
                                                                             self.regt.get()
                                                                            ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from students_detail where regt=%s", self.regt.get())
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students_detail where " + str(self.search_by.get())+ " LIKE '%" + str(self.search_txt.get())+ "%' ")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.stu_table.delete(*self.stu_table.get_children())
            for row in rows:
                self.stu_table.insert('', END, value=row)
            con.commit()
        con.close()




root = Tk()
obj = StudentManagementSystem(root)
root.mainloop()


# add_btn.grid(row=0, column=0, padx=10, pady=8 )
# updt_btn.grid(row=0, column=1, padx=10, pady=8 
# del_btn.grid(row=0, column=2, padx=10, pady=8 )
# clr_btn.grid(row=0, column=3, padx=10, pady=8 )
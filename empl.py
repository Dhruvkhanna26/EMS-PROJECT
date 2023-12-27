from ast import Del, Import
from cProfile import label
import dbm
from email import message
#from dbm import _Database
from logging import exception
from multiprocessing import connection
from os import stat
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
from tkinter import messagebox



class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title('Employee Management System')


        #variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()



        lbl_title=Label(self.root,text='EMPLOYEE MANAGEMENT SYSTEM',font=('times new roman',37,'bold'),fg='darkblue',bg='white')
        lbl_title.place(x=0,y=0,width=1530,height=50)

       #logo
        # Load image
        img_logo = Image.open('projectpic/logo.png')
        img_logo = img_logo.resize((249,50), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.image_label = Label(self.root, image=self.photo_logo)
        self.image_label.place(x=174,y=0,width=249,height=50)
        


        #Image Frame
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=50,width=1530,height=130)


        #1st image
        img1 = Image.open('projectpic/img1.jpeg')
        img1 = img1.resize((540,200), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photo1 = ImageTk.PhotoImage(img1)

        self.img_1 = Label(img_frame, image=self.photo1)
        self.img_1.place(x=0,y=0,width=540,height=200)

        #2nd image
        img2 = Image.open('projectpic/img3.jpg')
        img2 = img2.resize((540,160), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photo2 = ImageTk.PhotoImage(img2)

        self.img_2 = Label(img_frame, image=self.photo2)
        self.img_2.place(x=540,y=0,width=540,height=160)
         #3nd image
        img3 = Image.open('projectpic/img2.png')
        img3 = img3.resize((540,160), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photo3 = ImageTk.PhotoImage(img3)

        self.img_3 = Label(img_frame, image=self.photo3)
        self.img_3.place(x=1080,y=0,width=350,height=160)

        #Main Frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        main_frame.place(x=10,y=180,width=1420,height=710)

        #upper frame
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        upper_frame.place(x=10,y=10,width=1400,height=265)

        #Labels and entry fields
        lbl_dep=Label(upper_frame,text='Department:',font=('arial',11,'bold'),bg='white',fg='black')
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(upper_frame,textvariable=self.var_dep,font=('arial',12,'bold'),width=20,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #Name
        lbl_Name=Label(upper_frame,text='Name:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)

        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        #lbl_designation
        lbl_designation=Label(upper_frame,text='Designation:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_designation.grid(row=1,column=0,padx=2,pady=7,sticky=W)

        txt_designation=ttk.Entry(upper_frame,textvariable=self.var_designation,width=22,font=("arial",11,"bold"))
        txt_designation.grid(row=1,column=1,padx=2,pady=7)

        #email
        lbl_email=Label(upper_frame,text='Email:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)

        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)        

        #address
        lbl_address=Label(upper_frame,text='Address:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)

        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_address.grid(row=2,column=1,padx=2,pady=7)

        #married
        lbl_married_status=Label(upper_frame,text='Married status:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_married_status.grid(row=2,column=2,padx=2,pady=7,sticky=W)

        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=('arial',12,'bold'),width=20,state='readonly')
        com_txt_married['value']=('Married','Unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)

        #dob
        lbl_dob=Label(upper_frame,text='DOB:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)

        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        #doj
        lbl_doj=Label(upper_frame,text='DOJ:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)

        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)


        #id proof
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=('arial',12,'bold'),width=16,state='readonly')
        com_txt_proof['value']=('Select ID Proof','PAN CARD','AADHAR CARD','DRIVING LICENCE')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)

        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
        
        #Gender
        lbl_gender=Label(upper_frame,text='Gender:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)

        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=('arial',12,'bold'),width=20,state='readonly')
        com_txt_gender['value']=('Male','Female','Other')
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)
        
        #phone
        lbl_phone=Label(upper_frame,text='Phone No:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)

        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

        #country
        lbl_country=Label(upper_frame,text='Country:',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)

        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        #CTC
        lbl_CTC=Label(upper_frame,text='Salary(CTC):',font=('arial',12,'bold'),bg='white',fg='black')
        lbl_CTC.grid(row=2,column=4,padx=2,pady=7,sticky=W)

        txt_CTC=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_CTC.grid(row=2,column=5,padx=2,pady=7)

        #MASK IMAGE
        img_masked = Image.open('projectpic/img4.png')
        img_masked = img_masked.resize((220,220), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photomask = ImageTk.PhotoImage(img_masked)

        self.img_masked = Label(upper_frame, image=self.photomask)
        self.img_masked.place(x=900,y=0,width=220,height=220)

        #button Frame
        button_frame=Frame(upper_frame,bd=2,relief=RIDGE,bg='white')
        button_frame.place(x=1200,y=20,width=170,height=170)

        btn_add=Button(button_frame,text='Save',command=self.add_data ,font=('arial',15,'bold'),width=14,bg='#0000FF',fg='white')
        btn_add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(button_frame,text='Update',command=self.update_data,font=('arial',15,'bold'),width=14,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn_delete=Button(button_frame,command=self.delete_data , text='Delete',font=('arial',15,'bold'),width=14,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=1,pady=5)

        btn_clear=Button(button_frame,command=self.reset_data,text='Clear',font=('arial',15,'bold'),width=14,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=1,pady=5)

       




        #down frame
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg='white',text='Employee Information',font=('times new roman',11,'bold'),fg='red')
        down_frame.place(x=10,y=290,width=1400,height=390)

        #search Frame
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg='white',text='Search Employee Information',font=('times new roman',11,'bold'),fg='red')
        search_frame.place(x=0,y=0,width=1390,height=220)

        search_by=Label(search_frame,font=('arial',11,'bold'),text='Search by:',fg='white',bg='red')
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        #Search

        self.var_com_search=StringVar()
       
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=('arial',12,'bold'),width=18,state='readonly')
        com_txt_search['value']=('Select Option','Phone','id_proof')
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn_search=Button(search_frame,command=self.search_data,text='Search',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(search_frame,command=self.fetch_data,text='Show All',font=('arial',11,'bold'),width=14,bg='blue',fg='white')
        btn_ShowAll.grid(row=0,column=4,padx=5)

        stayhome=Label(search_frame,font=('times new roman',30,'bold'),text='WEAR MASK',fg='red',bg='white')
        stayhome.place(x=700,y=5,width=600,height=25)

        img_logo_mask = Image.open('projectpic/img5.jpg')
        img_logo_mask = img_logo_mask.resize((75, 75), resample=Image.BICUBIC)  # Use BICUBIC instead

        self.photo_logo_mask = ImageTk.PhotoImage(img_logo_mask)

        self.image_label_mask = Label(search_frame, image=self.photo_logo_mask)
        self.image_label_mask.place(x=825,y=0,width=75,height=45)

        #========Employee table============

        #Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RIDGE,bg='white')
        table_frame.place(x=0,y=60,width=1390,height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.employee_table=ttk.Treeview(table_frame,column=('dep','name','design.','email','address','married','dob','doj','idproofcomb','idproof','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading('dep',text='Department')
        self.employee_table.heading('name',text='Name')
        self.employee_table.heading('design.',text='Designation')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('married',text='Married_Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID_type')
        self.employee_table.heading('idproof',text='ID_Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')

        self.employee_table['show']='headings'
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('design.',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('married',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)
        
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    #==========Function declarations===============
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn = mysql.connector.connect(
                         host='localhost',
                         user='dhruvk',  # Corrected username
                         password='Dhruvson@2602',  # Corrected password
                         database='stud_info',
                         auth_plugin='mysql_native_password'
                )
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_name.get(),
                                                                                                                self.var_designation.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_married.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_doj.get(),
                                                                                                                self.var_idproofcomb.get(),
                                                                                                                self.var_idproof.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_country.get(),
                                                                                                                self.var_salary.get () 
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('success','Employee has been added!',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

        #fetch data                        
    def fetch_data(self):
        conn = mysql.connector.connect(
                        host='localhost',
                        user='dhruvk',  # Corrected username
                        password='Dhruvson@2602',  # Corrected password
                     database='stud_info',
                        auth_plugin='mysql_native_password'
              )
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee1')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()
    
    #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values']

        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designation.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure update this employee data')
                if update>0:
                    conn = mysql.connector.connect(
                         host='localhost',
                         user='dhruvk',  # Corrected username
                         password='Dhruvson@2602',  # Corrected password
                         database='stud_info',
                         auth_plugin='mysql_native_password'
                     )
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee1 set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s', (
                                                                                            self.var_dep.get(),
                                                                                            self.var_name.get(),
                                                                                            self.var_designation.get(),
                                                                                            self.var_email.get(),
                                                                                            self.var_address.get(),
                                                                                            self.var_married.get(),
                                                                                            self.var_dob.get(),
                                                                                            self.var_doj.get(),
                                                                                            self.var_idproofcomb.get(),
                                                                                            self.var_gender.get(),
                                                                                            self.var_phone.get(),
                                                                                            self.var_country.get(),
                                                                                            self.var_salary.get(), 
                                                                                            self.var_idproof.get()
))

                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Succesfully Updated',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)

    #DELETE
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                Delete=messagebox.askyesno('Delete','Are you sure you want to Delete this employee',parent=self.root)
                if Delete>0:
                    conn = mysql.connector.connect(
                         host='localhost',
                         user='dhruvk',  # Corrected username
                         password='Dhruvson@2602',  # Corrected password
                         database='stud_info',
                         auth_plugin='mysql_native_password'
                     )
                    my_cursor=conn.cursor()
                    sql='delete from employee1 where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Deleted','Employee Succesfully Deleted',parent=self.root)

            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    
    #RESET
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designation.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

    #search 
    def search_data(self):
        if self.var_com_search.get()=='' or self.var_search.get()=='':
            messagebox.showerror('Error','Please select option')
        else:
            try:
                 conn = mysql.connector.connect(
                         host='localhost',
                         user='dhruvk',  # Corrected username
                         password='Dhruvson@2602',  # Corrected password
                         database='stud_info',
                         auth_plugin='mysql_native_password'
                     )
                 my_cursor=conn.cursor()
                 my_cursor.execute('select * from employee1 where ' +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                 rows=my_cursor.fetchall()
                 if len(rows)!=0:
                     self.employee_table.delete(*self.employee_table.get_children())
                     for i in rows:
                         self.employee_table.insert("",END,values=i)
                     conn.commit
                     conn.close()
            except Exception as es:
                messagebox.showerror('Error',f'Due to:{str(es)}',parent=self.root)
    

        

if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()

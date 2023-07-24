
import tkinter as tk
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk

class window_1:
    def __init__(self, master):

        self.master = master
        self.frame = tk.Frame(self.master)
            
        db=pymysql.connect('localhost','root','Wb#scc284')
        cur=db.cursor()
               #TABLE AND DATABASE
                                                                #   CREATION
        sql_1='create database if not exists tk;'                         #   SYNTAXES
                                                                            
        sql_2='use tk;'                                     
                
        sql_3='''
        create table if not exists student_data(first_name varchar(20),
        middle_name varchar(20),
        last_name varchar(20),
        residential_address varchar(20),
        phone_number int(10),
        telephone_number int(12),
        email_address varchar(40),
        fathers_name varchar(30),
        mothers_name varchar(30),
        fathers_occupation varchar(30),
        mothers_occupation varchar(30),
        gender varchar(5),
        age int(3),
        class varchar(3));
        '''

        sql_4='''create table if not exists informations(
        sno int,
        Name_teachers varchar(20),
        password int 
        );'''

        sql_5='insert into informations values(1,"Sunil",456321);'
        sql_6='insert into informations values(2,"Anand",567342);'
        sql_7='insert into informations values(3,"Dinesh",900876);'
        sql_8='insert into informations values(4,"Divya",145327);'
        sql_9='insert into informations values(5,"Anwesha",976451);'
        sql_10='insert into informations values(6,"Sandip",600873);'
        sql_11='insert into informations values(7,"Satyaki",785432);'
        sql_12='insert into informations values(8,"Anamika",157860);'
        sql_13='insert into informations values(9,"Binoy",400876);'
        sql_14='insert into informations values(10,"Fatima",980043);'
        sql_15='insert into informations values(11,"Mohona",765431);'
        sql_16='insert into informations values(12,"Ritisha",567890);'
        sql_17='insert into informations values(13,"Preeyanka",345321);'
        sql_18='insert into informations values(14,"Adarsh",908987);'
        sql_19='insert into informations values(15,"Deep",657768);'
        sql_20='insert into informations values(16,"Diya",456657);'
        sql_21='insert into informations values(17,"Arijit",989098);'
        sql_22='insert into informations values(18,"Riya",234431);'
        sql_23='insert into informations values(19,"Rajdeep",145564);'
        sql_24='insert into informations values(20,"Jaya",109085);'
        sql_25='drop table if exists informations;'
            

        cur.execute(sql_1)
        cur.execute(sql_2)
        cur.execute(sql_25)
        cur.execute(sql_3)
        cur.execute(sql_4)
        cur.execute(sql_5)
        cur.execute(sql_6)
        cur.execute(sql_7)
        cur.execute(sql_8)
        cur.execute(sql_9)
        cur.execute(sql_10)
        cur.execute(sql_11)
        cur.execute(sql_12)
        cur.execute(sql_13)
        cur.execute(sql_14)
        cur.execute(sql_15)
        cur.execute(sql_16)
        cur.execute(sql_17)
        cur.execute(sql_18)
        cur.execute(sql_19)
        cur.execute(sql_20)
        cur.execute(sql_21)
        cur.execute(sql_22)
        cur.execute(sql_23)
        cur.execute(sql_24)


        
        db.commit()
        db.close()
         
        self.img=ImageTk.PhotoImage(Image.open('pk2.JPG'))
        self.img_label=tk.Label(self.frame,image=self.img)
        self.img_label.grid(row=0,column=1)
            
        self.l1 = tk.Label(self.frame, text="WELCOME TO ADMISSION ZONE \n\n OF \n\n KENDRIYA VIDYALAYA SANGATHAN",font='Algerian 25 bold italic',fg='red')
        self.l1.place(x=400,y=10)
            

        self.img_lb=ImageTk.PhotoImage(Image.open('kvs-logo-with-bg.jpg'))
        self.logo=tk.Label(self.frame,image=self.img_lb)
        self.logo.place(x=580,y=200)
          
            

        self.B = tk.Button(self.frame, text ="TEACHER",cursor='circle', command = self.call_teach, activebackground= 'grey',fg='red', bg ='light blue',font='Caribian 15 bold',borderwidth=10)
        self.B.place(x=343,y=350)
        self.D = tk.Button(self.frame,text='PARENT/STUDENTS',cursor='circle',command = self.call_stud , activebackground = 'grey' , bg ='light blue',font='Caribian 15 bold',borderwidth=10)
        self.D.place(x=300,y=450)
        self.B1=tk.Button(self.frame, text ="   CREDIT   ",cursor='circle', command = self.credit,  bg ='light blue',font='Caribian 15 bold',borderwidth=10)
        self.B1.place(x=1210,y=500)
        self.B2=tk.Button(self.frame, text ="    EXIT!!    ",cursor='circle', command = self.close_windows,  bg ='grey',font='Caribian 15 bold',borderwidth=10)
        self.B2.place(x=1210,y=570)
        self.frame.pack()
            



    def call_teach(self):        #___---CREATING NEW WINDOW FOR  TEACHERS---___

        self.newWindow = tk.Toplevel(self.master)
        self.app = teachers_window(self.newWindow)

    def call_stud(self):        #___---CREATING NEW WINDOW FOR STUDENT---___

        self.newWindow = tk.Toplevel(self.master)
        self.app = student_window(self.newWindow)
    def credit(self):
        a='''THIS SOFTWARE IS DEVELOPED BY GROUP-1
  GL : DIPNARAYAN SEN
  GM : SUBHAM SARKAR
  GM : MADHUSHREE GHOSH'''
        MsgBox = tk.messagebox.showinfo ("Credit",a)

    def close_windows(self):

        self.master.destroy()

#_________________________________---TEACHERS WINDOW----_____________________________________________________
        
class teachers_window:

    def __init__(self, teacher):

        self.teacher = teacher
        self.teacher.title('LOGIN WINDOW')
        self.teacher.geometry("1280x768+0+0")

        self.img1=ImageTk.PhotoImage(Image.open('loginbg.jpg'))
        self.img1_label=tk.Label(self.teacher,image=self.img1)
        self.img1_label.grid(row=0,column=1)

        title=tk.Label(self.teacher,text="WELCOME TO LOGIN SYSTEM OF TEACHERS",font=("Adobe Fan Heiti Std",40),bg='deep sky blue',fg='white')
        title.place(x=0,y=0,relwidth=1)
        self.frame=tk.Frame(self.teacher)
        self.frame.place(x=410,y=150)
        lbl=tk.Label(self.frame,text="USER LOGIN",font=("Adobe Fan Heiti Std",30))
        lbl.grid(row=0,columnspan=2)
        
        
        self.img2=ImageTk.PhotoImage(Image.open('loginlogo.png'))
        lb2=tk.Label(self.frame,image=self.img2)
        lb2.grid(row=1,columnspan=2,pady=20)
        self.L1 = tk.Label(self.frame, text="  USERNAME  ",font=('Adobe Fan Heiti Std',15))
        self.L1.grid(row=2,column=0,pady=20)
        self.E1 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2)
        self.E1.grid(row=2,column=1,pady=20,padx=20)

        self.L2 = tk.Label(self.frame, text="  PASSWORD  ",font=('Adobe Fan Heiti Std',15))
        self.L2.grid(row=3,column=0,pady=20)
        self.E2 = tk.Entry(self.frame,show='*',font='Caribian 15',borderwidth=2)
        self.E2.grid(row=3,column=1,pady=20,padx=20)

        self.B1=tk.Button(self.frame, text ="  SUBMIT  ",cursor='circle', command = self.check_data,  bg ='light blue',font=('Adobe Fan Heiti Std',15))
        self.B1.grid(row=4,columnspan=2,pady=20)
        self.B2=tk.Button(self.frame, text ="  QUIT  ",cursor='circle', command = self.close_windows,  bg ='light blue',font=('Adobe Fan Heiti Std',15))
        self.B2.grid(row=5,columnspan=2,pady=20)


        


        


    def print_data(self):

        db=pymysql.connect('localhost','root','12345','tk')
        cur=db.cursor()
        cur.execute("select * from student_data;")
        for a in cur.fetchall():
            print(a)
        db.commit()
        db.close()

    def check_data(self):
        user_name=self.E1.get()
        password=self.E2.get()
        db=pymysql.connect('localhost','root','12345','tk')
        cur=db.cursor()
        sql_25="select password from informations where Name_teachers='"+user_name+"';"
        cur.execute(sql_25)
        for get_pass in cur.fetchone():
            if int(get_pass) == int(password):
                messagebox.showinfo("VERIFICATION", "USERNAME AND PASSWORD VERIFIED!!")
                db.commit()
                db.close()
                self.data = tk.Toplevel(self.teacher)
                self.app = show_data(self.data)



    def close_windows(self):

        self.teacher.destroy()

class show_data:
    
    def __init__(self, show):
        self.show = show
        title=tk.Label(self.show,text="LIST OF STUDENTS WHO HAVE RESISTERED",font=("Adobe Fan Heiti Std",40),bg='deep sky blue',fg='white')
        title.place(x=0,y=0,relwidth=1)

        self.show.title('registered student')
        self.show.geometry("1366x768+0+0")
        
        

        self.frame = tk.Frame(self.show)
        self.frame.place(x=25,y=100)

        db=pymysql.connect('localhost','root','12345','tk')
        cur=db.cursor()
        

        self.lb1= tk.Label(self.frame,text = "first_name".upper(),bg='deep sky blue',fg='white')  
        self.lb1.grid(row=0,column=0)#,padx=5,pady=5)
        self.lb2 = tk.Label(self.frame,text = "middle_name".upper())  
        self.lb2.grid(row=0,column=1)#,padx=5,pady=5)
        self.lb3 = tk.Label(self.frame,text = "last_name".upper(),bg='deep sky blue',fg='white')  
        self.lb3.grid(row=0,column=2)#,padx=5,pady=5)

        self.lb4 = tk.Label(self.frame,text = "residential_address".upper())  
        self.lb4.grid(row=0,column=3)#,padx=5,pady=5)
        self.lb5 = tk.Label(self.frame,text = "phone_number".upper(),bg='deep sky blue',fg='white')  
        self.lb5.grid(row=0,column=4)#,padx=5,pady=5)
        self.lb6 = tk.Label(self.frame,text = "telephone_number".upper())  
        self.lb6.grid(row=0,column=5)#,padx=5,pady=5)
        self.lb7 = tk.Label(self.frame,text = "email_address".upper(),bg='deep sky blue',fg='white')  
        self.lb7.grid(row=0,column=6)#,padx=5,pady=5)
        self.lb8 = tk.Label(self.frame,text = "fathers_name".upper())  
        self.lb8.grid(row=0,column=7)#,padx=5,pady=5)
        self.lb9 = tk.Label(self.frame,text = "mothers_name".upper(),bg='deep sky blue',fg='white')  
        self.lb9.grid(row=0,column=8)#,padx=5,pady=5)
        self.lb10 = tk.Label(self.frame,text = "fathers_occupation".upper())  
        self.lb10.grid(row=0,column=9)#,padx=5,pady=5)
        self.lb11 = tk.Label(self.frame,text = "mothers_occupation".upper(),bg='deep sky blue',fg='white')  
        self.lb11.grid(row=0,column=10)#,padx=5,pady=5)
        self.lb12 = tk.Label(self.frame,text = "gender".upper())  
        self.lb12.grid(row=0,column=11)#,padx=5,pady=5)
        self.lb13 = tk.Label(self.frame,text = "age".upper(),bg='deep sky blue',fg='white')  
        self.lb13.grid(row=0,column=12)#,padx=5,pady=5)
        self.lb14 = tk.Label(self.frame,text='class'.upper())
        self.lb14.grid(row=0,column=13)#,padx=5,pady=5)

        

        cur.execute("select * from student_data;")
        r=1
        c=0
        i=13
##        val=list(val)
##        print(val)
        for a in cur.fetchall():
            c=0
            for b in a:
                self.lb=tk.Label(self.frame,text=str(b))
                self.lb.grid(row=r,column=c)#,padx=5,pady=5)
                c=c+1
            r=r+1

       



#_________________________________---STUDENT WINDOW----_____________________________________________________

class student_window:

    def __init__(self, stu):
        self.stu=stu
        self.stu.title("ADMISSION FORM")
        self.stu.geometry("1366x768+0+0")
        self.bgstu=ImageTk.PhotoImage(Image.open('bgstu.jpg'))
        self.bgstu_label=tk.Label(self.stu,image=self.bgstu)
        self.bgstu_label.place(x=0,y=0)

        txt="                             APPLICATION FORM                               "
        self.l=tk.Label(self.stu,text=txt,font=("Adobe Fan Heiti Std",40),bg='red',fg='white')
        self.l.grid(row=0,column=0)
        self.frame = tk.Frame(self.stu,bg='black')
        self.frame.place(x=155,y=100)
        self.L1=tk.Label(self.frame, text="first name".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L1.grid(row=0,column=0,padx=10,pady=10)
        self.E1 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E1.grid(row=0,column=1,padx=10,pady=10)

        self.L2 = tk.Label(self.frame, text="middle name".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L2.grid(row=1,column=0,padx=10,pady=10)
        self.E2 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E2.grid(row=1,column=1,padx=10,pady=10)

        self.L3 = tk.Label(self.frame, text="last name".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L3.grid(row=2,column=0,padx=10,pady=10)
        self.E3 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E3.grid(row=2,column=1,padx=10,pady=10)

        self.L4 = tk.Label(self.frame, text="residential city".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L4.grid(row=3,column=0,padx=10,pady=10)
        self.E4 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E4.grid(row=3,column=1,padx=10,pady=10)

        self.L5 = tk.Label(self.frame, text="phone number".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L5.grid(row=4,column=0,padx=10,pady=10)
        self.E5 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E5.grid(row=4,column=1,padx=10,pady=10)

        self.L6 = tk.Label(self.frame, text="telephone number".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L6.grid(row=5,column=0,padx=10,pady=10)
        self.E6 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E6.grid(row=5,column=1,padx=10,pady=10)
            
        self.L7 = tk.Label(self.frame, text="email address".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L7.grid(row=6,column=0,padx=10,pady=10)
        self.E7 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E7.grid(row=6,column=1,padx=10,pady=10)


        self.L8= tk.Label(self.frame, text="father's name".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L8.grid(row=7,column=0,padx=10,pady=10)
        self.E8 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E8.grid(row=7,column=1,padx=10,pady=10)

        self.L9 = tk.Label(self.frame, text="mothers name".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L9.grid(row=8,column=0,padx=10,pady=10)
        self.E9 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E9.grid(row=8,column=1,padx=10,pady=10)

        self.L10= tk.Label(self.frame, text="father's occupation".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L10.grid(row=0,column=2,padx=10,pady=10)
        self.E10 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E10.grid(row=0,column=3,padx=10,pady=10)

        self.L11 = tk.Label(self.frame, text="mother's occupation".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L11.grid(row=1,column=2,padx=10,pady=10)
        self.E11 = tk.Entry(self.frame,font='Caribian 15',borderwidth=2,bg='tomato',fg='white')
        self.E11.grid(row=1,column=3,padx=10,pady=10)

    #    self.g=tk.StringVar()
        self.L12= tk.Label(self.frame, text="  gender  ".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L12.grid(row=2,column=2,padx=10,pady=10)
        
   #     tk.Radiobutton(self.frame,text='MALE',variable=self.g,value='MALE',bg='black',fg='white').grid(row=2,column=4)

    #    tk.Radiobutton(self.frame,text='FEMALE',variable=self.g,value='FEMALE',bg='black',fg='white').grid(row=2,column=3)
        

        self.E12 = tk.Entry(self.frame,font='Caribian 15 bold',borderwidth=2,bg='tomato',fg='white')
        self.E12.grid(row=2,column=3,padx=10,pady=10)


        self.L13= tk.Label(self.frame, text="  age  ".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L13.grid(row=3,column=2,padx=10,pady=10)
        self.E13 = tk.Entry(self.frame,font='Caribian 15 bold',borderwidth=2,bg='tomato',fg='white')
        self.E13.grid(row=3,column=3,padx=10,pady=10)



        self.L14= tk.Label(self.frame, text="  class  ".upper(),font='Caribian 15 bold',borderwidth=10,bg='black',fg='white')
        self.L14.grid(row=4,column=2,padx=10,pady=10)
        self.E14 = tk.Entry(self.frame,font='Caribian 15 bold',borderwidth=2,bg='tomato',fg='white')
        self.E14.grid(row=4,column=3,padx=10,pady=10)










        self.B1=tk.Button(self.frame, text ="SUBMIT",font='Caribian 15 bold',cursor='circle',command = self.save_data ,bg='black',fg='white')
        self.B1.grid(row=7,column=3,padx=50,pady=10)
        self.B2=tk.Button(self.frame, text ="PRINT", command = self.print_data,  bg ='light blue')

        self.B3=tk.Button(self.frame, text ="EXIT",font='Caribian 15 bold',cursor='circle', command = self.close_windows,bg='black',fg='white')
        self.B3.grid(row=8,column=3,padx=50,pady=10)

##
##        self.image_lb=ImageTk.PhotoImage(Image.open('logo for the student.jpg'))
##        self.logo1=tk.Label(self.frame,image=self.image_lb)
##        self.logo1.place(x=250,y=20)





    def save_data(self):    #____----SAVE'S DATA TO DATABASE---____#

        db=pymysql.connect('localhost','root','12345','tk')
        cur=db.cursor()

        a="insert into student_data values('"            #___PREPRATION OF SQL COMMAND___#
        b=self.E1.get()
        c=self.E2.get()
        d=self.E3.get()
        e=self.E4.get()
        f=self.E5.get()
        g=self.E6.get()
        h=self.E7.get()
        i=self.E8.get()

        j=self.E9.get()
        k=self.E10.get()
        l=self.E11.get()
        m=self.E12.get()
        n=self.E13.get()
        o=self.E14.get()


        if b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i=='' or j=='' or k=='' or l=='' or m=='' or n=='' or o=='' :
            MsgBox = tk.messagebox.showinfo ("INCOMPLETE INPUT","ALL THE ENTRIES SHOULD BE FILLED",icon = 'warning')
            return None
        	
        if len(self.E5.get())<10:
            MsgBox = tk.messagebox.showinfo ("WRONG INPUT","PHONE NO. SHOULD BE OF 10 DIGITS",icon = 'warning')
            return None
        if len(self.E5.get())>10:
            MsgBox = tk.messagebox.showinfo ("WRONG INPUT","PHONE NO. SHOULD BE OF 10 DIGITS",icon = 'warning')
            return None


        
        sql=a+b+"','"+c+"','"+d+"','"+e+"',"+f+","+g+",'"+h+"','"+i+"','"+j+"','"+k+"','"+l+"','"+m+"',"+n+",'"+o+"');"
        print(sql)
                   
        cur.execute(sql)

       # try:
            
       # except:
       #     MsgBox = tk.messagebox.showinfo ("ERROR IN SAVING DATA","PLEASE ENSURE ALL THE ENTRIES ARE FILLED CORRECTLY!!",icon = 'warning')
        #    return None
        db.commit()
        db.close()
        self.E1.delete(0,len(b))
        self.E2.delete(0,len(c))
        self.E3.delete(0,len(d))
        self.E4.delete(0,len(e))
        self.E5.delete(0,len(f))
        self.E6.delete(0,len(g))
        self.E7.delete(0,len(h))
        self.E8.delete(0,len(i))
        self.E9.delete(0,len(j))
        self.E10.delete(0,len(k))
        self.E11.delete(0,len(l))
        self.E12.delete(0,len(m))
        self.E13.delete(0,len(n))
        self.E14.delete(0,len(o))
        
     #   self.E3.

    def print_data(self):           #_____________----EXTRACTION OF DATA----___________#

        db=pymysql.connect('localhost','root','12345','tk')
        cur=db.cursor()
        cur.execute("select * from student_data;")
        for a in cur.fetchall():
            print(a)
        db.commit()
        db.close()

    def close_windows(self):

        self.stu.destroy()

#_______________________________----GLOBAL---_________________________________________________________________

def main(): 
    root = tk.Tk()
    app = window_1(root)
    root.mainloop(app)

if __name__ == '__main__':
    main()    

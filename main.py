import mysql.connector as ms
pass1=input("Enter Database Password : ")
try:
    cn=ms.connect(host="localhost",user="root",passwd=pass1)
    cur=cn.cursor()
except:
    print("***** Incorrect Password *****")
    exit()

print("""
        ================================
              Welcome to Hospital
        ================================""")

cur.execute("create database if not exists hospital")
cur.execute("use hospital")
cur.execute("create table if not exists patients\
                 (pid int(10) primary key,\
                 name varchar(30) not null,\
                 mobile varchar(10),\
                 age int(3),\
                 city varchar(50),\
                 doc_rec varchar(30))")
cur.execute("create table if not exists doctors\
                (name varchar(30) primary key,\
                department varchar(40),\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                fees int(10),\
                salary int(10))")
cur.execute("create table if not exists nurses\
                (name varchar(30) primary key,\
                age int(2),\
                city varchar(30),\
                mobile varchar(15),\
                salary int(10))")
cur.execute("create table if not exists workers\
                 (name varchar(30) primary key,\
                 age int(2),\
                 city varchar(30),\
                 mobile varchar(15),\
                 salary int(10))")

cur.execute("create table if not exists users\
                 (username varchar(30) primary key,\
                  password varchar(30) default'000')")



def sign_up():
    print("""

            ============================================
            *******Please enter new user details********
            ============================================""")
    u=input("Enter New User Name!!:")
    p=input("Enter password (Combination of Letters, Digits etc.):")
    cur.execute("insert into users values('"+u+"','"+p+"')")
    cn.commit()
    print("""
        ========================================================
        ********Congratulations!!!, New User Created...*********
        ======================================================== """)

def login():
            print("""
                ==========================================================
                ***********  Loginwith Username and Password   **********
                =========================================================== """)
            un=input("Username :")
            ps=input("Password :")
            cur.execute("Select password from users where username='"+un+"'")
            rec=cur.fetchall()
            for i in rec:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        print("""
           **********************""")
                        print("""
                            1.Admin Tasks
                            2.Patient (Admit and Discharge)
                            3.Sign Out """)
                        a=int(input("Enter your choice:"))
                        if a==1:
                            print("""
                                1. Show Details
                                2. Add new member
                                3. Delete existing member
                                4. Exit""")
                            b=int(input("Enter your choice:"))
                            if b==1:
                                print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers""")
                                c=int(input("ENTER YOUR CHOICE:"))
                                if c==1:
                                    cur.execute("select * from doctors")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        b=0
                                        v=list(i)
                                        k=["NAME","DEPARTEMNT","AGE","CITY","MOBILE","FEES","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                elif c==2:
                                    cur.execute("select * from nurses")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                                elif c==3:
                                    cur.execute("select * from workers")
                                    rec=cur.fetchall()
                                    for i in rec:
                                        v=list(i)
                                        k=["NAME","AGE","CITY","MOBILE","SALARY"]
                                        d=dict(zip(k,v))
                                        for i in d:
                                            print(i,":",d[i])
                                        print()
                            elif b==2:
                                print("""
                                    1. Doctor
                                    2. Nurse
                                    3. Worker """)
                                c=int(input("Enter your choice:"))
                                if c==1:
                                  name=input("Enter name of doctor:")
                                  dep=input("Enter department:")
                                  age=input("Enter age:")
                                  city=input("Enter city doctor belongs to:")
                                  mno=input("Enter 10 digit mobile no.:")
                                  fees=input("Enter fees:")
                                  sal=input("Enter Salary of doctor:")
                                  cur.execute("insert into doctors values('"+name+"','"+dep+"','"+age+"','"+city+"','"+mno+"','"+fees+"','"+sal+"')")
                                  cn.commit()
                                  print("New doctor details has been added successfully. ")
                                elif c==2:
                                  name=input("Enter name of nurse:")
                                  age=input("Enter age:")
                                  city=input("Enter city nurse belongs to:")
                                  mno=input("Enter mobile no.:")
                                  sal=int(input("Enter salary:"))
                                  cur.execute("insert into nurses values('"+name+"','"+age+"','"+city+"','"+mno+"','"+str(sal)+"')")
                                  cn.commit()
                                  print("New nurse details has been added successfully.")
                                elif c==3:
                                  name=input("Enter name of worker:")
                                  age=input("Enter Age:")
                                  city=input("Enter city:")
                                  mno=input("Enter mobile no:")
                                  ms=input("Enter Salary:")
                                  cur.execute("insert into workers values('"+name+"','"+age+"','"+city+"','"+mno+"','"+ms+"')")
                                  cn.commit()
                                  print("SUCCESSFULLY ADDED")
                            elif b==3:
                               print("""
                                    1. Doctors
                                    2. Nurses
                                    3. Workers
                                                                                """)
                               c=int(input("Enter your choice:"))
                               if c==1:
                                   name=input("Enter doctor name to delete:")
                                   cur.execute("select * from doctors where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("You really want to delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("Delete from doctors where name='"+name+"'")
                                       cn.commit()
                                       print("Doctor has been deleted successfully")
                                   else:
                                       print("Error in deletion....")
                                   
                               elif c==2:
                                   name=input("Enter name of nurse:")
                                   cur.execute("select * nurses where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Are you really want to delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("delete from nurses where name='"+name+"'")
                                       cn.commit()
                                       print("Nurse has been deleted successfully.")
                                   else:
                                       print("Error in deletion")
                               elif c==3:
                                   name=input("Enter name of worker:")
                                   cur.execute("select * from workers where name='"+name+"'")
                                   rec=cur.fetchall()
                                   print(rec)
                                   p=input("Are you really want to delete this data? (y/n):")
                                   if p=="y":
                                       cur.execute("Delete from workers where name='"+name+"'")
                                       cn.commit()
                                       print("Worker has been deleted.")
                                   else:
                                       print("Error in deletion.")
                            elif b==4:
                                print("Thank you! See you again! Have nice Day!")
                                break
                           
                        elif a==2:
                            
                            print("""
                                    1. Show patient record
                                    2. Admit new patient
                                    3. Discharge Patient
                                    4. Exit
                                                                      """)
                            b=int(input("ENTER YOUR CHOICE:"))
                            if b==1:
                                cur.execute("select * from patients")
                                rec=cur.fetchall()
                                for i in rec:
                                    b=0
                                    v=list(i)
                                    k=["NAME","GENDER","AGE","CITY","MOBILE NO"]
                                    d=dict(zip(k,v))
                                    for i in d:
                                        print(i,":",d[i])

                            elif b==2:
                                cur.execute("SELECT pid FROM patients")
                                l=cur.fetchall()
                                M=[]
                                m=len(l)
                                for i in range(m):
                                    M.append(l[i][0])
                                pid=max(M)+1
                                name=str(input("Enter name of patient: ")) 
                                age=str(input("Enter age: "))
                                city=str(input("Enter City: "))
                                mn=str(input("Enter Mobile no.: "))
                                cur.execute("select name from doctors")
                                rec=cur.fetchall()
                                dr=str(input("Enter doctorname to be recommended:"))
                                cur.execute ("insert into patients values('"+str(pid)+"','"+str(name)+"','"+str(mn)+"','"+str(age)+"','"+str(city)+"','"+str(dr)+"')")
                                cn.commit()            

                                print("""
                                ====================================
                                 *******New patient admitted*******
                                ====================================
                                                """)
                            elif b==3:
                                name=input("Enter the name of patient to discharge:")
                                cur.execute("select * from patients where name='"+name+"'")
                                rec=cur.fetchall()
                                print(rec)
                                bill=input("Bill payemt (y/n):")
                                if bill=="y":
                                    cur.execute("Delete from patients where name like'%"+name+"%'")
                                    cn.commit()
                                elif bill=="n":
                                    print("Please pay your pending bill amount to discahrge patient.")
                                else:
                                    print("Bill payment status is unknown....")
                            elif b==4:
                                break
                        elif a==3:
                            break
                else:
                    print("Invalid Credential")
            
#Main Menu
r=0
while r!=4:
    print("""
1. Sign Up (New User)
2. Log In
3. Exit 
************************ """)

    r=int(input("Enter your choice:"))    
    #New User Registration
    if r==1:
        sign_up()
    elif r==2:
        login()                 
    elif r==3:
      print("Thank you for using Hospital App, Have a nice day!")
      break

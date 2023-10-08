from tkinter import *
from tkinter.messagebox import *
from tkinter.scrolledtext import *
from sqlite3 import *
import pandas as pd
import matplotlib.pyplot as plt
import requests,json
import json
from urllib.request import urlopen


root=Tk()
root.title("E.M.S")
root.geometry("500x600+50+50")
f=("Arial",20,"bold")
root.configure(bg="light green")
def f1():
root.withdraw()

aw.deiconify()
def f2():
aw.withdraw()
root.deiconify()
def f3():
root.withdraw()
vw.deiconify()
vw_em_data.delete(1.0,END)
con=None
try:
con=connect("ems.db")
cursor=con.cursor()
sql="select * from emp order by id"
cursor.execute(sql)
data=cursor.fetchall()
info=""
for d in data:
info=info+"id="+str(d[0])+" "+"name="+str(d[1])+"
"+"salary="+str(d[2])+"\n"
vw_em_data.insert(INSERT,info)
except Exception as e:
showerror("issue","e")
finally:
if con is not None:
con.close()
def f4():
vw.withdraw()
root.deiconify()
def f5():
con=None
special_characters="@#$%^!&*()_+=,?<>/"
# VALIDATION FOR ADD WINDOW
if aw_ent_id.get()=="" or aw_ent_name.get()=="" or
aw_ent_salary.get()=="":
showerror("Error","All fields are compulsory")
elif any(c in special_characters for c in aw_ent_id.get()):
showerror("Error","id cannot have special characters")
elif aw_ent_id.get().isalpha():
showerror("Error","id cannot have alphabets")
elif aw_ent_name.get().isnumeric()==True:
showerror("Error","name cannot have digit")
elif any(c in special_characters for c in aw_ent_name.get()):
showerror("Error","name cannot have special
characters")
elif len(aw_ent_name.get()) < 2 :
showinfo("Error","name must have min 2 characters")
elif any(c in special_characters for c in aw_ent_salary.get()):
showerror("Error","salary cannot have special
characters")
elif aw_ent_salary.get().isalpha():
showerror("Error","salary cannot have alphabets")
elif int(aw_ent_salary.get()) < 8000:
showerror("Error","salary should be minimum 8k")
elif int(aw_ent_id.get()) <= 0:
showerror("Error","id must be positive")
else:
try:
con=connect("ems.db")
cursor=con.cursor()
sql="insert into emp values('%d','%s','%d')"
id=int(aw_ent_id.get())
name=aw_ent_name.get()
salary=int(aw_ent_salary.get())
cursor.execute(sql%(id,name,salary))
con.commit()
showinfo("Success","record created")
except Exception as e:
con.rollback()
showerror("issue",e)
finally:
if con is not None:
con.close()
aw_ent_id.delete(0,END)
aw_ent_name.delete(0,END)
aw_ent_salary.delete(0,END)
aw_ent_id.focus()
def f6():
root.withdraw()
uw.deiconify()
def f7():
uw.withdraw()
root.deiconify()
# UPDATE DATABASE CONNECTIVITY
def f8():
con=None
special_characters="@#$%^!&*()_+=,?<>/"
# VALIDATION FOR UPDATE WINDOW
if uw_ent_id.get()=="" or uw_ent_name.get()=="" or
uw_ent_salary.get()=="":
showerror("Error","All fields are compulsory")
elif any(c in special_characters for c in uw_ent_id.get()):
showerror("Error","id cannot have special characters")
elif uw_ent_id.get().isalpha():
showerror("Error","id cannot have alphabets")
elif uw_ent_name.get().isnumeric()==True:
showerror("Error","name cannot have digit")
elif any(c in special_characters for c in uw_ent_name.get()):
showerror("Error","name cannot have special
characters")
elif len(uw_ent_name.get()) < 2 :
showerror("Error","name must have min 2 characters")
elif any(c in special_characters for c in uw_ent_salary.get()):
showerror("Error","salary cannot have special
characters")
elif uw_ent_salary.get().isalpha():
showerror("Error","salary cannot have alphabets")
elif int(uw_ent_salary.get()) < 8000:
showerror("Error","salary should be minimum 8k")
elif int(uw_ent_id.get()) <= 0:
showerror("Error","id must be positive")
else:
try:
con=connect("ems.db")
cursor=con.cursor()
sql="update emp set name='%s',salary='%d' where
id='%d'"
id=int(uw_ent_id.get())
name=uw_ent_name.get()
salary=int(uw_ent_salary.get())
cursor.execute(sql%(name,salary,id))
if cursor.rowcount==1:
con.commit()
showinfo("done","record updated")
else:
showinfo("sorry","record does not exist")
except Exception as e:
con.rollback()
print("issue",e)
finally:
if con is not None:
con.close()
uw_ent_id.delete(0,END)
uw_ent_name.delete(0,END)
uw_ent_salary.delete(0,END)
uw_ent_id.focus()
def f9():
root.withdraw()
dw.deiconify()
def f10():
dw.withdraw()
root.deiconify()
# DELETE RECORD DATABASE CONNECTIVITY
def f11():
con=None
special_characters="@#$%^!&*()_+=,?<>/"
#VALIDATION FOR DELETE WINDOW
if dw_ent_id.get()=="":
showerror("Error","id cannot be empty")
elif any(c in special_characters for c in dw_ent_id.get()):
showerror("Error","id cannot have special characters")
elif dw_ent_id.get().isalpha():
showerror("Error","id cannot have alphabets")
elif int(dw_ent_id.get()) <= 0:
showerror("Error","id must be positive")
else:
try:
con=connect("ems.db")
cursor=con.cursor()
sql="delete from emp where id='%d'"
id=int(dw_ent_id.get())
cursor.execute(sql % (id))
if cursor.rowcount==1:
con.commit()
showinfo("done","record deleted")
else:
showinfo("Error","record does not exist")
except Exception as e:
con.rollback()
print("issue",e)
finally:
if con is not None:
con.close()
dw_ent_id.delete(0,END)
dw_ent_id.focus()
# CODE FOR CHART REPRESENTATION
def f12():
con=connect("ems.db")
cursor = con.cursor()
cursor.execute("select name, salary from emp order by salary
desc limit 5")
result = cursor.fetchall
name = []
salary = []
for i in cursor:
name.append(i[0])
salary.append(i[1])
#print("Name of Employee = ", name)
#print("Salary of Employee = ", salary)
plt.bar(name, salary,width=0.60,color="green")
plt.ylim(0, 100000)
plt.xlabel("Name of
Employee",fontweight="bold",fontsize=10)
plt.ylabel("Salary of
Employee",fontweight="bold",fontsize=10)
plt.title("Employee
Information",fontweight="bold",fontsize=10)
#plt.legend()
plt.grid()
plt.show()
# MainMenu
btn_add=Button(root,text="Add
",font=f,width=15,bd=4,command=f1)
btn_add.pack(pady=10)
btn_view=Button(root,text="View
",font=f,width=15,bd=4,command=f3)
btn_view.pack(pady=10)
btn_update=Button(root,text="Update
",font=f,width=15,bd=4,command=f6)
btn_update.pack(pady=10)
btn_delete=Button(root,text="Delete
",font=f,width=15,bd=4,command=f9)
btn_delete.pack(pady=10)
btn_charts=Button(root,text="Charts",font=f,width=15,bd=4,comm
and=f12)
btn_charts.pack(pady=10)
# label and entry for loc and temp
lab_loc=Label(root,text="Location:",font=f)
lab_loc.place(x=20,y=450)
ent_loc_ans=Entry(root,font=f,width=9)
ent_loc_ans.place(x=20,y=500)
lab_temp=Label(root,text="Temperature:",font=f)
lab_temp.place(x=250,y=450)
ent_temp_ans=Entry(root,font=f,width=9)
ent_temp_ans.place(x=250,y=500)
#code to get temperature
apiKey="bcb7eafeb56fc824019e5314244e8731"
baseURL="https://api.openweathermap.org/data/2.5/weather?q=
"
cityName=("Mumbai")
completeURL=baseURL+cityName+"&appid="+apiKey
response=requests.get(completeURL)
data=response.json()
#print(data)
temp_k=data["main"]["temp"]
temp_c=temp_k - 273.14
#print("temp=",temp_c)
temp_c=round(temp_c,2)
ent_temp_ans.insert(INSERT,temp_c)
# code to get location
url='http://ipinfo.io/json'
response=urlopen(url)
data=json.load(response)
#print(data)
c=data['city']
#print(c)
ent_loc_ans.insert(INSERT,c)
# Add Window
aw=Toplevel(root)
aw.title("Add Employee")
aw.geometry("500x600+50+50")
aw.configure(bg="light blue")
aw_lab_id=Label(aw,text="enter id:",font=f,bg="light blue")
aw_ent_id=Entry(aw,font=f,bd=2)
aw_lab_name=Label(aw,text="Enter name:",font=f,bg="light blue")
aw_ent_name=Entry(aw,font=f,bd=2)
aw_lab_salary=Label(aw,text="Enter salary:",font=f,bg="light
blue")
aw_ent_salary=Entry(aw,font=f,bd=2)
aw_lab_id.pack(pady=10)
aw_ent_id.pack(pady=10)
aw_lab_name.pack(pady=10)
aw_ent_name.pack(pady=10)
aw_lab_salary.pack(pady=10)
aw_ent_salary.pack(pady=10)
aw_btn_save=Button(aw,text="Save",font=f,command=f5)
aw_btn_back=Button(aw,text="Back",font=f,command=f2)
aw_btn_save.pack(pady=20)
aw_btn_back.pack(pady=20)
aw.withdraw()
# View Window
vw=Toplevel(root)
vw.title("View Employee")
vw.geometry("600x600+50+50")
vw.configure(bg="light yellow")
vw_em_data=ScrolledText(vw,width=35,height=14,font=f)
vw_em_data.pack(pady=30)
vw_btn_back=Button(vw,text="Back",font=f,command=f4)
vw_btn_back.pack(pady=10)
vw.withdraw()
# Update Window
uw=Toplevel(root)
uw.title("Update Employee")
uw.geometry("500x600+50+50")
uw.configure(bg="light pink1")
uw_lab_id=Label(uw,text="enter id:",font=f,bg="light pink1")
uw_ent_id=Entry(uw,font=f,bd=2)
uw_lab_name=Label(uw,text="Enter name:",font=f,bg="light
pink1")
uw_ent_name=Entry(uw,font=f,bd=2)
uw_lab_salary=Label(uw,text="Enter salary:",font=f,bg="light
pink1")
uw_ent_salary=Entry(uw,font=f,bd=2)
uw_lab_id.pack(pady=10)
uw_ent_id.pack(pady=10)
uw_lab_name.pack(pady=10)
uw_ent_name.pack(pady=10)
uw_lab_salary.pack(pady=10)
uw_ent_salary.pack(pady=10)
uw_btn_save=Button(uw,text="Save",font=f,command=f8)
uw_btn_back=Button(uw,text="Back",font=f,command=f7)
uw_btn_save.pack(pady=20)
uw_btn_back.pack(pady=20)
uw.withdraw()
# Delete Window
dw=Toplevel(root)
dw.title("Delete Employee")
dw.geometry("500x600+50+50")
dw.configure(bg="light slate blue")
dw_lab_id=Label(dw,text="enter id:",font=f,bg="light slate blue")
dw_lab_id.pack(pady=20)
dw_ent_id=Entry(dw,font=f,bd=2)
dw_ent_id.pack(pady=20)
dw_btn_save=Button(dw,text="Save",font=f,command=f11)
dw_btn_back=Button(dw,text="Back",font=f,command=f10)
dw_btn_save.pack(pady=20)
dw_btn_back.pack(pady=20)
dw.withdraw()
# CHART WINDOW
cw=Toplevel(root)
cw.title("Chart of Employee")
cw.geometry("500x600+50+50")
cw.withdraw()
root.mainloop()
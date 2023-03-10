from tkinter import *
root=Tk()
root.geometry("500x300")

def getval():
    print("Accepted")

Label(root, text="Python Registration Form", font="ar 15 bold").grid(row=0, column=3)

name=Label(root, text="Name")
phone=Label(root, text="Phone")
email=Label(root, text="Email")
gender=Label(root, text="Gender")
age=Label(root, text="Age")

name.grid(row=1, column=2)
phone.grid(row=2, column=2)
email.grid(row=3, column=2)
gender.grid(row=4, column=2)
age.grid(row=5, column=2)

nameValue=StringVar
phoneValue=StringVar
emailValue=StringVar
genderValue=StringVar
ageValue=StringVar
checkvalue= IntVar

nameentry= Entry(root, textvariable=nameValue)
phoneentry= Entry(root, textvariable=phoneValue)
emailentry= Entry(root, textvariable=emailValue)
genderentry= Entry(root, textvariable=genderValue)
ageentry= Entry(root, textvariable=ageValue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
emailentry.grid(row=3, column=3)
genderentry.grid(row=4, column=3)
ageentry.grid(row=5, column=3)

checkbtn = Checkbutton(text="Remember me?", variable=checkvalue)
checkbtn.grid(row=6,column=3)

Button(text="Submit",command=getval).grid(row=7,column=3)
root.mainloop()

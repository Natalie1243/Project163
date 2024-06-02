from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Heart Diagnostic Report")
root.geometry("500x500")
root.configure(background='RosyBrown1')

question1_radioButton = StringVar(value = "0")

Question1  = Label(root, text = "Do you experience shortness of breath during routine activites?" , background = "RosyBrown1")
Question1.pack()
question1_r1 = Radiobutton(root, text  = "yes", variable = question1_radioButton, value = "yes", background = "RosyBrown1")
question1_r1.pack()
question1_r2 = Radiobutton(root, text  = "no", variable = question1_radioButton, value = "no", background = "RosyBrown1")
question1_r2.pack()

question2_radioButton = StringVar(value = "0")
Question2 = Label(root, text = "Do you have swelling in the feet/ ankles/legs (shoes feel tighter) or abdomen?", background = "RosyBrown1")
Question2.pack()
question2_r1 = Radiobutton(root, text  = "yes", variable = question2_radioButton, value = "yes", background = "RosyBrown1")
question2_r1.pack()
question2_r2 = Radiobutton(root, text  = "no", variable = question2_radioButton, value = "no", background = "RosyBrown1")
question2_r2.pack()

question3_radioButton = StringVar(value = "0")
Question3 = Label(root, text = "Do you feel any if these symptoms- confusion, disorientation or loss of memory?", background = "RosyBrown1")
Question3.pack()
question3_r1 = Radiobutton(root, text  = "yes", variable = question3_radioButton, value = "yes", background = "RosyBrown1")
question3_r1.pack()
question3_r2 = Radiobutton(root, text  = "no", variable = question3_radioButton, value = "no", background = "RosyBrown1")
question3_r2.pack()

question4_radioButton = StringVar(value = "0")
Question4 = Label(root, text = "Do you experience shortness of breath while at rest/lying down?", background = "RosyBrown1")
Question4.pack()
question4_r1 = Radiobutton(root, text  = "yes", variable = question4_radioButton, value = "yes", background = "RosyBrown1")
question4_r1.pack()
question4_r2 = Radiobutton(root, text  = "no", variable = question4_radioButton, value = "no", background = "RosyBrown1")
question4_r2.pack()

question5_radioButton = StringVar(value = "0")
Question5 = Label(root, text = "Do you experience persistent wheezing/ coughing that produces white or pink blood tinged mucus?", background = "RosyBrown1")
Question5.pack()
question5_r1 = Radiobutton(root, text  = "yes", variable = question5_radioButton, value = "yes", background = "RosyBrown1")
question5_r1.pack()
question5_r2 = Radiobutton(root, text  = "no", variable = question5_radioButton, value = "no", background = "RosyBrown1")
question5_r2.pack()

def heart_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question4_radioButton.get()=="yes":
        score = score+20
    if question5_radioButton.get()=="yes":
        score = score+20
        
    if score<= 10:
        messagebox.showinfo("Report", "You don't need to visit a doctor.")
    elif score > 10 and score <= 30:
        messagebox.showinfo("Report", "You might perhaps have to visit a doctor.")
    else:
        messagebox.showinfo("Report", "I strongly advise you to visit a doctor")

find_out = Button(root, text = "Find Out", command = heart_score)
find_out.pack()

root.mainloop()

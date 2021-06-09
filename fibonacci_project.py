from tkinter import *

root = Tk()

root.title("Fibonacci")
root.geometry("400x400")

enter_word = Entry(root)
label_series = Label(root)
label_sum = Label(root)

def Fibonacci():
    value= enter_word.get()
    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    sum2=0
    while (counter <= value):
         label_series["text"] += str(sum) + " "
         counter = counter + 1
         first_no = second_no
         second_no = sum
         sum2= sum2+ sum
         sum = first_no + second_no
         label_series['text'] = "Flower is fully bloomed"
         label_spiral["text"] = "Spirals in right direction are " + \
         str(first_no) + " and spirals in left direction are " + \
         str(second_no) + "\n. Total spirals are " + str(sum)
        
btn = Button(root, text="Show Fibonacci Series", command=Fibonacci)
btn.pack()
label_series.pack()
label_sum.pack()
root.mainloop()

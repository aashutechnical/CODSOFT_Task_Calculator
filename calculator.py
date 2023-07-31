from tkinter import *
first_number= second_number= operator=None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number, operator
    first_number =int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number,second_number,operator
    second_number=int(result_label['text'])

    if operator=='+':
        result_label.config(text=str(first_number+second_number))
    elif operator=='-':
        result_label.config(text=str(first_number-second_number))
    elif operator=='*':
        result_label.config(text=str(first_number*second_number))
    elif operator=='/':
        result_label.config(text=str(first_number/second_number))
    else:
        if second_number == 0:
            result_label.config(text=str(first_number/ second_number))
    

root = Tk()
root.title('CACULATOR')
root.geometry('280x380')
root.resizable(0,0)
root.configure(background='black')

result_label = Label(root,text='',bg='black',fg='white')
result_label.grid(row=0,column=0,columnspan=5,pady=(50,25),sticky='w')
result_label.config(font=('Helvetica',25,'bold'))

btn7 = Button(root,text='7',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(7))
btn7.grid(row=1,column=0)
btn7.config(font=('Helvetica',16))

btn8 = Button(root,text='8',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(8))
btn8.grid(row=1,column=1)
btn8.config(font=('Helvetica',16))

btn9 = Button(root,text='9',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(9))
btn9.grid(row=1,column=2)
btn9.config(font=('Helvetica',16))

btn_multiply = Button(root,text='X',bg='#5F9EA0',fg='white',width=5,height=2,command=lambda:get_operator('*'))
btn_multiply.grid(row=1,column=3)
btn_multiply.config(font=('Helvetica',16))

btn4 = Button(root,text='4',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(4))
btn4.grid(row=2,column=0)
btn4.config(font=('Helvetica',16))

btn5 = Button(root,text='5',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(5))
btn5.grid(row=2,column=1)
btn5.config(font=('Helvetica',16))

btn6 = Button(root,text='6',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(6))
btn6.grid(row=2,column=2)
btn6.config(font=('Helvetica',16))

btn_substract = Button(root,text='-',bg='#5F9EA0',fg='white',width=5,height=2,command=lambda:get_operator('-'))
btn_substract.grid(row=2,column=3)
btn_substract.config(font=('Helvetica',16))

btn1 = Button(root,text='1',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(1))
btn1.grid(row=3,column=0)
btn1.config(font=('Helvetica',16))

btn2 = Button(root,text='2',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(2))
btn2.grid(row=3,column=1)
btn2.config(font=('Helvetica',16))

btn3 = Button(root,text='3',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(3))
btn3.grid(row=3,column=2)
btn3.config(font=('Helvetica',16))

btn_add = Button(root,text='+',bg='#5F9EA0',fg='white',width=5,height=2,command=lambda:get_operator('+'))
btn_add.grid(row=3,column=3)
btn_add.config(font=('Helvetica',16))

btn_clr = Button(root,text='C',bg='#5F9EA0',fg='white',width=5,height=2,command=lambda:clear())
btn_clr.grid(row=4,column=0)
btn_clr.config(font=('Helvetica',16))

btn0 = Button(root,text='0',bg='#5F9EA0',fg='white',width=5,height=2,command= lambda :get_digit(0))
btn0.grid(row=4,column=1)
btn0.config(font=('Helvetica',16))

btn_equals = Button(root,text='=',bg='#5F9EA0',fg='white',width=5,height=2, command = get_result)
btn_equals.grid(row=4,column=2)
btn_equals.config(font=('Helvetica',16))

btn_divide = Button(root,text='/',bg='#5F9EA0',fg='white',width=5,height=2,command=lambda:get_operator('/'))
btn_divide.grid(row=4,column=3)
btn_divide.config(font=('Helvetica',16))










root.mainloop()


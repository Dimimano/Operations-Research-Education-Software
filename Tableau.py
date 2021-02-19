from tkinter import * 
from _overlapped import NULL
from tkinter.font import BOLD, ITALIC
from ttkthemes import themed_tk as tk
from tkinter import ttk
import imageio
from PIL import Image, ImageTk
import webbrowser




def SetDualPriceText(string1,string2,string3,string4,string5,string6):
    DualPrice1.config(text=string1)
    DualPrice2.config(text=string2)
    DualPrice3.config(text=string3)
    DualPrice4.config(text=string4)
    DualPrice5.config(text=string5)
    DualPrice6.config(text=string6)
    
def SetDualPriceColour(colour):
    DualPrice1.config(fg=colour)
    DualPrice2.config(fg=colour)
    DualPrice3.config(fg=colour)
    DualPrice4.config(fg=colour)
    DualPrice5.config(fg=colour)
    DualPrice6.config(fg=colour)
    
def SetReducedCostText(string1,string2,string3,string4,string5,string6):
    ReducedCost1.config(text=string1)
    ReducedCost2.config(text=string2)
    ReducedCost3.config(text=string3)
    ReducedCost4.config(text=string4)
    ReducedCost5.config(text=string5)
    ReducedCost6.config(text=string6)
    
def SetReducedCostColour(colour):
    ReducedCost1.config(fg=colour)
    ReducedCost2.config(fg=colour)
    ReducedCost3.config(fg=colour)
    ReducedCost4.config(fg=colour)
    ReducedCost5.config(fg=colour)
    ReducedCost6.config(fg=colour)
    
def SetDualPriceFontSize(size):
    DualPrice1.config(font=("Helvetica", size))
    DualPrice2.config(font=("Helvetica", size))
    DualPrice3.config(font=("Helvetica", size))
    DualPrice4.config(font=("Helvetica", size))
    DualPrice5.config(font=("Helvetica", size))
    DualPrice6.config(font=("Helvetica", size))
    
def SetReducedCostFontSize(size):
    ReducedCost1.config(font=("Helvetica", size))
    ReducedCost2.config(font=("Helvetica", size))
    ReducedCost3.config(font=("Helvetica", size))
    ReducedCost4.config(font=("Helvetica", size))
    ReducedCost5.config(font=("Helvetica", size))
    ReducedCost6.config(font=("Helvetica", size))
    
def SetRow1Colour(colour):
    A11.config(fg=colour)
    A12.config(fg=colour)
    A13.config(fg=colour)
    A14.config(fg=colour)
    A15.config(fg=colour)
    A16.config(fg=colour)

def SetRow2Colour(colour):
    A21.config(fg=colour)
    A22.config(fg=colour)
    A23.config(fg=colour)
    A24.config(fg=colour)
    A25.config(fg=colour)
    A26.config(fg=colour)
    
def SetRow3Colour(colour):
    A31.config(fg=colour)
    A32.config(fg=colour)
    A33.config(fg=colour)
    A34.config(fg=colour)
    A35.config(fg=colour)
    A36.config(fg=colour)
    
def SetRow4Colour(colour):
    A41.config(fg=colour)
    A42.config(fg=colour)
    A43.config(fg=colour)
    A44.config(fg=colour)
    A45.config(fg=colour)
    A46.config(fg=colour)  
    
def SetRow1Text(string1,string2,string3,string4,string5,string6):
    A11.config(text=string1)
    A12.config(text=string2)
    A13.config(text=string3)
    A14.config(text=string4)
    A15.config(text=string5)
    A16.config(text=string6) 

def SetRow2Text(string1,string2,string3,string4,string5,string6):
    A21.config(text=string1)
    A22.config(text=string2)
    A23.config(text=string3)
    A24.config(text=string4)
    A25.config(text=string5)
    A26.config(text=string6)
    
def SetRow3Text(string1,string2,string3,string4,string5,string6):
    A31.config(text=string1)
    A32.config(text=string2)
    A33.config(text=string3)
    A34.config(text=string4)
    A35.config(text=string5)
    A36.config(text=string6)
    
def SetRow4Text(string1,string2,string3,string4,string5,string6):
    A41.config(text=string1)
    A42.config(text=string2)
    A43.config(text=string3)
    A44.config(text=string4)
    A45.config(text=string5)
    A46.config(text=string6) 

def SetRHSColour(colour):
    RHS1.config(fg=colour)
    RHS2.config(fg=colour)
    RHS3.config(fg=colour)
    RHS4.config(fg=colour)
    
def SetRatioTestText(string1,string2,string3,string4):
    RatioTest1.config(text=string1)
    RatioTest2.config(text=string2)
    RatioTest3.config(text=string3)
    RatioTest4.config(text=string4)
    
def SetRatioTestColour(colour):
    RatioTest1.config(fg=colour)
    RatioTest2.config(fg=colour)
    RatioTest3.config(fg=colour)
    RatioTest4.config(fg=colour)  
    

root = tk.ThemedTk()
root.title('Tableau method')
root.iconbitmap(".icon\\simplex.ico")
root.get_themes()
root.set_theme("radiance")
root.geometry('1415x650')



IntroFrame = LabelFrame(root,padx=5,pady=5,background='white',relief=SUNKEN)
UOMimg = PhotoImage(file=".img\\UOM.png")
UOMimgLabel = Label(IntroFrame,background='white',pady=5)
UOMimgLabel.config(image=UOMimg)
UOMimgLabel.grid(row=0,column=0)
Intro1 = Label(IntroFrame,text='Department of Applied Informatics',font=("Helvetica", 18,BOLD),background='white')
Intro2 = Label(IntroFrame,text='Operations Research',font=("Helvetica", 18,BOLD),background='white')
Intro1.grid(row=2,column=0)
Intro2.grid(row=3,column=0)
IntroFrame.grid(row=0,column=10,padx=180,pady=30)


TableauFrame = LabelFrame(root,background='white')



Title = Label(TableauFrame,text = 'Primal Simplex Algorithm',font=("Helvetica", 15, BOLD),background='white')
Title.grid(row=0,column=3,columnspan=6)
orig_color = Title.cget("background")

BaseFunctionCoefficients = Label(TableauFrame, text='C',font=("Helvetica", 15),background='white') 
BaseFunctionCoefficients .grid(row=3,column=0)
Base = Label(TableauFrame, text='Base',font=("Helvetica", 13, BOLD),background='white')
Base.grid(row=3,column=1)

BaseFunctionCoefficient1 = Label(TableauFrame, text='0',font=("Helvetica", 20),background='white')
BaseFunctionCoefficient1.grid(row=5,column=0)
BaseFunctionCoefficient2 = Label(TableauFrame, text='0',font=("Helvetica", 20),background='white')
BaseFunctionCoefficient2.grid(row=6,column=0)
BaseFunctionCoefficient3 = Label(TableauFrame, text='0',font=("Helvetica", 20),background='white')
BaseFunctionCoefficient3.grid(row=7,column=0)
BaseFunctionCoefficient4 = Label(TableauFrame, text='0',font=("Helvetica", 20),background='white')
BaseFunctionCoefficient4.grid(row=8,column=0)

BaseVariable1 = Label(TableauFrame, text= 'x' + '\u2083',font=("Helvetica", 20),background='white')
BaseVariable1.grid(row=5,column=1)
BaseVariable2 = Label(TableauFrame, text= 'x' + '\u2084',font=("Helvetica", 20),background='white')
BaseVariable2.grid(row=6,column=1)
BaseVariable3 = Label(TableauFrame, text= 'x' + '\u2085',font=("Helvetica", 20),background='white')
BaseVariable3.grid(row=7,column=1)
BaseVariable4 = Label(TableauFrame, text= 'x' + '\u2086',font=("Helvetica", 20),background='white')
BaseVariable4.grid(row=8,column=1)

Variable1 = Label(TableauFrame, text = 'x' + '\u2081',font=("Helvetica", 20),background='white')
Variable1.grid(row=3,column=3)
Variable2 = Label(TableauFrame, text = 'x' + '\u2082',font=("Helvetica", 20),background='white')
Variable2.grid(row=3,column=4)
Variable3 = Label(TableauFrame, text = 'x' + '\u2083',font=("Helvetica", 20),background='white')
Variable3.grid(row=3,column=5)
Variable4 = Label(TableauFrame, text = 'x' + '\u2084',font=("Helvetica", 20),background='white')
Variable4.grid(row=3,column=6)
Variable5 = Label(TableauFrame, text = 'x' + '\u2085',font=("Helvetica", 20),background='white')
Variable5.grid(row=3,column=7)
Variable6 = Label(TableauFrame, text = 'x' + '\u2086',font=("Helvetica", 20),background='white')
Variable6.grid(row=3,column=8)

FunctionCoefficient1 = Label(TableauFrame, text= '5',font=("Helvetica", 20),background='white')
FunctionCoefficient1.grid(row=1,column=3)
FunctionCoefficient2 = Label(TableauFrame, text= '4',font=("Helvetica", 20),background='white')
FunctionCoefficient2.grid(row=1,column=4)
FunctionCoefficient3 = Label(TableauFrame, text= '0',font=("Helvetica", 20),background='white')
FunctionCoefficient3.grid(row=1,column=5)
FunctionCoefficient4 = Label(TableauFrame, text= '0',font=("Helvetica", 20),background='white')
FunctionCoefficient4.grid(row=1,column=6)
FunctionCoefficient5 = Label(TableauFrame, text= '0',font=("Helvetica", 20),background='white')
FunctionCoefficient5.grid(row=1,column=7)
FunctionCoefficient6 = Label(TableauFrame, text= '0',font=("Helvetica", 20),background='white')
FunctionCoefficient6.grid(row=1,column=8)

A11 = Label(TableauFrame, text = '6',font=("Helvetica", 20),background='white')
A11.grid(row=5,column=3)
A12 = Label(TableauFrame, text = '4',font=("Helvetica", 20),background='white')
A12.grid(row=5,column=4)
A13 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A13.grid(row=5,column=5)
A14 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A14.grid(row=5,column=6)
A15 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A15.grid(row=5,column=7)
A16 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A16.grid(row=5,column=8)

A21 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A21.grid(row=6,column=3)
A22 = Label(TableauFrame, text = '2',font=("Helvetica", 20),background='white')
A22.grid(row=6,column=4)
A23 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A23.grid(row=6,column=5)
A24 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A24.grid(row=6,column=6)
A25 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A25.grid(row=6,column=7)
A26 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A26.grid(row=6,column=8)

A31 = Label(TableauFrame, text = '-1',font=("Helvetica", 20),background='white')
A31.grid(row=7,column=3)
A32 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A32.grid(row=7,column=4)
A33 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A33.grid(row=7,column=5)
A34 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A34.grid(row=7,column=6)
A35 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A35.grid(row=7,column=7)
A36 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A36.grid(row=7,column=8)

A41 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A41.grid(row=8,column=3)
A42 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A42.grid(row=8,column=4)
A43 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A43.grid(row=8,column=5)
A44 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A44.grid(row=8,column=6)
A45 = Label(TableauFrame, text = '0',font=("Helvetica", 20),background='white')
A45.grid(row=8,column=7)
A46 = Label(TableauFrame, text = '1',font=("Helvetica", 20),background='white')
A46.grid(row=8,column=8)


RHS = Label(TableauFrame, text= 'R.H.S.',font=("Helvetica", 13,BOLD),background='white').grid(row=3,column=10,columnspan=2)
RHS1 = Label(TableauFrame, text= '24',font=("Helvetica", 20),background='white')
RHS1.grid(row=5,column=10,columnspan=2)
RHS2 = Label(TableauFrame, text= '6',font=("Helvetica", 20),background='white')
RHS2.grid(row=6,column=10,columnspan=2)
RHS3 = Label(TableauFrame, text= '1',font=("Helvetica", 20),background='white')
RHS3.grid(row=7,column=10,columnspan=2)
RHS4 = Label(TableauFrame, text= '2',font=("Helvetica", 20),background='white')
RHS4.grid(row=8,column=10,columnspan=2)

DualPrice1 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
DualPrice2 = Label(TableauFrame, text= '?', font=("Helvetica", 20, BOLD),background='white')
DualPrice3 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
DualPrice4 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
DualPrice5 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
DualPrice6 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')

ReducedCost1 = Label(TableauFrame, text= '5', font=("Helvetica", 20),background='white')
ReducedCost2 = Label(TableauFrame, text= '4', font=("Helvetica", 20),background='white')
ReducedCost3 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
ReducedCost4 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
ReducedCost5 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')
ReducedCost6 = Label(TableauFrame, text= '0', font=("Helvetica", 20),background='white')

RatioTest = Label(TableauFrame, text= 'Ratio Test',font=("Helvetica", 13,BOLD),background='white').grid(row=3,column=12,columnspan=2)
RatioTest1 = Label(TableauFrame, text= '4', font=("Helvetica", 20),background='white')
RatioTest2 = Label(TableauFrame, text= '6', font=("Helvetica", 20),background='white')
RatioTest3 = Label(TableauFrame, text= 'no limit', font=("Helvetica", 18),background='white')
RatioTest4 = Label(TableauFrame, text= 'no limit', font=("Helvetica", 18),background='white')

DualPrice = Label(TableauFrame, text = 'w',font=("Helvetica", 20),background='white').grid(row=10,column=1)
ReducedCost = Label(TableauFrame, text = 's',font=("Helvetica", 20),background='white').grid(row=11,column=1)
ObjectiveFunctionValue = Label(TableauFrame, text = '',font=("Helvetica", 20),background='white')
ObjectiveFunctionValue.grid(row=10,column=10,columnspan=2)
for i in range(12):
    VerticalLine1 = Canvas(TableauFrame, width=3, height=40)
    VerticalLine1.create_line(3, 0,3, 40)
    VerticalLine1.config(background='white')
    VerticalLine1.config(highlightbackground='white')
    VerticalLine1.grid(row=i,column=2)

for i in range(12):
    VerticalLine2 = Canvas(TableauFrame, width=3, height=40)
    VerticalLine2.create_line(3, 0,3, 40)
    VerticalLine2.config(background='white')
    VerticalLine2.config(highlightbackground='white')
    VerticalLine2.grid(row=i,column=9)

    
for i in range(14):
    HorizontalLine1 = Canvas(TableauFrame, width=40, height=3)
    HorizontalLine1.create_line(0,3,40,3)
    HorizontalLine1.config(background='white')
    HorizontalLine1.config(highlightbackground='white')
    HorizontalLine1.grid(row=2,column=i)
    
for i in range(14):
    HorizontalLine2 = Canvas(TableauFrame, width=40, height=3)
    HorizontalLine2.create_line(0,3,40,3)
    HorizontalLine2.config(background='white')
    HorizontalLine2.config(highlightbackground='white')
    HorizontalLine2.grid(row=4,column=i)
    
for i in range(14):
    HorizontalLine3 = Canvas(TableauFrame, width=40, height=3)
    HorizontalLine3.create_line(0,3,40,3)
    HorizontalLine3.config(background='white')
    HorizontalLine3.config(highlightbackground='white')
    HorizontalLine3.grid(row=9,column=i)



def click1():
    Question1Frame.grid(row=3,column=12,padx=55,pady=5,rowspan=4)
    StartIteration1Button.grid_remove()
    IntroFrame.grid_remove()
    ButtonFrame.grid_remove()

buttonStyle = ttk.Style()
buttonStyle.configure('TButton',font=('Helvetica', 15, BOLD),background=orig_color)  

ButtonFrame = LabelFrame(root,background='white')   
StartIteration1Button = ttk.Button(ButtonFrame,text = 'Start Iteration 1',command = click1)
StartIteration1Button.grid(row=1,column=0)
ReddyImg = PhotoImage(file=".img\\Reddy.png")
ReddyImgLabel =  Label(ButtonFrame,font=("Helvetica", 17),background='white')
ReddyImgLabel.config(image=ReddyImg)
ReddyImgLabel.grid(row=0,column=0)
ButtonFrame.grid(row=1,column=10)
TableauFrame.grid(row=0,column=0,padx=10,pady=10,columnspan=5,rowspan=10)


answer = BooleanVar()
answerInt = IntVar()
answer.set(NULL)
answerInt.set(NULL)
Score = 0   




def Question1Click(value):
    if value == True:
        Test1Answer1.config(background="lime green")
        Test1Answer1.config(state=DISABLED)
        Test1Answer2.config(state=DISABLED)
        Question2ButtonCorrect.grid(row=18,column=0,columnspan=3)
        Question1Frame.grid(row=3,column=12,padx=55,pady=25,rowspan=5)
        global Score
        Score = Score + 1
        
    else:
        Test1Answer2.config(background="firebrick")
        Test1Answer2.config(state=DISABLED)
        Test1Answer1.config(state=DISABLED)
        Question2ButtonWrong.grid(row=18,column=0,columnspan=3)
        Question1Frame.grid(row=3,column=12,padx=55,pady=25,rowspan=5)
        


Question1Frame = LabelFrame(root,background='white',padx=5,pady=5)
Question1 = Label(Question1Frame,text = 'Question 1: Which is the first step of the Primal Simplex Algorithm?',font=("Helvetica", 15, BOLD),background='white').grid(row=15,column=0)

Test1Answer1 = Radiobutton(Question1Frame, text='We need to select the entering variable (to the set of basic variables).', variable=answer, value=True,command=lambda: Question1Click(answer.get()),font=("Helvetica", 15),background='white')
Test1Answer1.grid(row=16,column=0)

Test1Answer2 = Radiobutton(Question1Frame, text='We need to select the leaving variable (from the set of basic variables).', variable=answer, value=False,command=lambda: Question1Click(answer.get()),font=("Helvetica", 15),background='white')
Test1Answer2.grid(row=17,column=0)

def Question2Click(value):
    if value == True:
        Test2Answer2.config(background="lime green")
        Test2Answer2.config(state=DISABLED)
        Test2Answer1.config(state=DISABLED)
        IntroToQuestion3Correct1.grid(row=18,column=0)
        IntroToQuestion3Correct2.grid(row=19,column=0)
        Question2Frame.grid(row=3,column=10,padx=80,pady=40,rowspan=7)
        Question3Button.grid(row=20,column=0)
        global Score
        Score = Score + 1
        
    else:
        Test2Answer1.config(background="firebrick")
        Test2Answer1.config(state=DISABLED)
        Test2Answer2.config(state=DISABLED)
        IntroToQuestion3Wrong.grid(row=18,column=0)
        ExtraIntro1.grid(row=19,column=0)
        ExtraIntro2.grid(row=20,column=0)
        Question2Frame.grid(row=3,column=10,padx=50,pady=40,rowspan=7)
        Question3Button.grid(row=21,column=0)
        

def click2Correct():
    Question1Frame.grid_remove()
    Question2ButtonCorrect.grid_remove()
    Question2Frame.grid(row=3,column=10,padx=80,pady=5,rowspan=5)
    
def click2Wrong():
    Question1Frame.grid_remove()
    Question2ButtonWrong.grid_remove()
    Question2Frame.grid(row=3,column=10,padx=80,pady=5,rowspan=5)
    


Question2ButtonCorrect = ttk.Button(Question1Frame,text = 'Correct answer, Question 2',command = click2Correct)
Question2ButtonWrong = ttk.Button(Question1Frame,text = 'Wrong answer!, Question 2',command = click2Wrong)

Question2Frame = LabelFrame(root,background='white',padx=5,pady=5)
Question2 = Label(Question2Frame,text = 'Question 2: How do we select the entering variable?',font=("Helvetica", 15, BOLD),background='white').grid(row=15,column=0,columnspan =50)

Test2Answer1 = Radiobutton(Question2Frame, text='We need to use the Minimum Ratio Test.', variable=answer, value=False,command=lambda: Question2Click(answer.get()),font=("Helvetica", 15),background='white')
Test2Answer1.grid(row=16,column=0)

Test2Answer2 = Radiobutton(Question2Frame, text='We need to calculate the Reduced Cost for each of the variables.', variable=answer, value=True,command=lambda: Question2Click(answer.get()),font=("Helvetica", 15),background='white')
Test2Answer2.grid(row=17,column=0) 

IntroToQuestion3Correct1 = Label(Question2Frame,text = 'Correct! In order to calculate the Reduced Costs s,',font=("Helvetica", 15),background='white')
IntroToQuestion3Correct2 = Label(Question2Frame,text = 'we first need to calculate the Dual Prices w.',font=("Helvetica", 15),background='white')
IntroToQuestion3Wrong = Label(Question2Frame,text = 'Wrong! We use the Minimum Ratio Test to determine the leaving variable...',font=("Helvetica", 15),background='white')
ExtraIntro1 = Label(Question2Frame,text = 'In order to calculate the Reduced Costs s,',font=("Helvetica", 15),background='white')
ExtraIntro2 = Label(Question2Frame,text = 'we first need to calculate the Dual Prices w.',font=("Helvetica", 15),background='white')

Question3Frame = LabelFrame(root,background='white',padx=5,pady=5)
img1 = PhotoImage(file=".img\\Right.png")
img2 = PhotoImage(file=".img\\False1.png")
img3 = PhotoImage(file=".img\\False2.png")

def click3():
    Question2Frame.grid_remove()
    Question3Frame.grid(row=1,column=10,rowspan=8,padx=170)
    Question3Button.grid_remove()
    

def Question3Click(value):
    if value == 1:
        Test3Answer1.config(background="lime green")
        Test3Answer1.config(state=DISABLED)
        Test3Answer2.config(state=DISABLED)
        Test3Answer3.config(state=DISABLED)
        ContinueButton1.grid(row=19,column=3,columnspan=50)
        Question3Frame.grid(row=1,column=10,rowspan=9,padx=170,pady=80)
        global Score
        Score = Score + 1
    
    elif value == 2:
        Test3Answer2.config(background="firebrick")
        Test3Answer1.config(background="lime green")
        Test3Answer1.config(state=DISABLED)
        Test3Answer2.config(state=DISABLED)
        Test3Answer3.config(state=DISABLED)
        ContinueButton1.grid(row=19,column=3,columnspan=50)
        Question3Frame.grid(row=1,column=10,rowspan=9,padx=170,pady=80)
        
    elif value == 3:
        Test3Answer3.config(background="firebrick")
        Test3Answer1.config(background="lime green")
        Test3Answer1.config(state=DISABLED)
        Test3Answer2.config(state=DISABLED)
        Test3Answer3.config(state=DISABLED)
        ContinueButton1.grid(row=19,column=3,columnspan=50)
        Question3Frame.grid(row=1,column=10,rowspan=9,padx=170,pady=80)
        
    

    
Question3Button = ttk.Button(Question2Frame,text = 'Question 3',command = click3)
Question3 = Label(Question3Frame,text = 'Question 3: Which one is the right equation?',font=("Helvetica", 15, BOLD),background='white').grid(row=15,column=0,columnspan =50)
Test3Answer1 = Radiobutton(Question3Frame, variable=answerInt, value=1,command=lambda: Question3Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test3Answer1.config(image=img1)
Test3Answer1.grid(row=16,column=3,columnspan=50)

Test3Answer2 = Radiobutton(Question3Frame, variable=answerInt, value=2,command=lambda: Question3Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test3Answer2.config(image=img2)
Test3Answer2.grid(row=17,column=3,columnspan=50)

Test3Answer3 = Radiobutton(Question3Frame, variable=answerInt, value=3,command=lambda: Question3Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test3Answer3.config(image=img3)
Test3Answer3.grid(row=18,column=3,columnspan=50)

imgDual1 = PhotoImage(file=".img\\Dual1.png")
imgDual2 = PhotoImage(file=".img\\Dual2.png")
imgDual3 = PhotoImage(file=".img\\Dual3.png")
imgDual4 = PhotoImage(file=".img\\Dual4.png")

def click4():
    Question3Frame.grid_remove()
    ContinueButton1.grid_remove()
    DualFrame.grid(row=0,column=17,rowspan=100,padx=75,pady=5)
    DualImg1.grid(row=3,column=16,rowspan=2)
    DualImg2.grid(row=10,column=16,rowspan=2)
    DualImg3.grid(row=13,column=16,rowspan=2)
    DualImg4.grid(row=15,column=16,rowspan=2)
    TitleDual.grid(row=0,column=16)
    DualLabel1.grid(row=1,column=16)
    DualLabel2.grid(row=2,column=16)
    DualLabel3.grid(row=8,column=16)
    DualLabel4.grid(row=12,column=16)
    A11.config(fg='red')
    A21.config(fg='red')
    A31.config(fg='red')
    A41.config(fg='red')
    DualPrice2.config(fg='dark orange')
    BaseFunctionCoefficient1.config(fg='blue')
    BaseFunctionCoefficient2.config(fg='blue')
    BaseFunctionCoefficient3.config(fg='blue')
    BaseFunctionCoefficient4.config(fg='blue')
    DualPrice1.grid(row=10,column=3)
    DualPrice1.config(fg='dark orange')
    Question4Button.grid(row=17,column=16)
     


DualFrame = LabelFrame(root,background='white',padx=5,pady=5)       
ContinueButton1 = ttk.Button(Question3Frame,text = 'Continue',command = click4)

TitleDual = Label(DualFrame,text="Dual Price Calculation",font=("Helvetica", 25, BOLD),background='white',pady=5)

DualLabel1 = Label(DualFrame,text="We multiply each column of the tableau",font=("Helvetica", 17),background='white')
DualLabel2 = Label(DualFrame,text="with the objective function coefficients of the base variables.",font=("Helvetica", 17),background='white')
DualImg1 =  Label(DualFrame,font=("Helvetica", 17),background='white')
DualImg1.config(image=imgDual1)


DualLabel3 = Label(DualFrame,text="For example the equation for dual price w1 is: ",font=("Helvetica", 17),background='white')
DualImg2 =  Label(DualFrame,font=("Helvetica", 17),background='white')
DualImg2.config(image=imgDual2) 


DualLabel4 = Label(DualFrame,text="Which is equal to: ",font=("Helvetica", 17),background='white')
DualImg3 = Label(DualFrame,font=("Helvetica", 17),background='white')
DualImg3.config(image=imgDual3)

DualImg4 = Label(DualFrame,font=("Helvetica", 17),background='white')
DualImg4.config(image=imgDual4)

def click5():
    
    A11.config(fg='black')
    A21.config(fg='black')
    A31.config(fg='black')
    A41.config(fg='black')
    A12.config(fg='red')
    A22.config(fg='red')
    A32.config(fg='red')
    A42.config(fg='red')
    Question4Button.grid_remove()
    DualPrice2.grid(row=10,column=4)
    DualPrice1.config(fg='black')
    Question4Label.grid(row=18,column=16)
    Question4Entry.grid(row=19,column=16)
    Question4Answer.grid(row=20,column=16)
    DualFrame.grid(row=0,column=17,rowspan=100,padx=75,pady=30)

Question4Button = ttk.Button(DualFrame,text = 'Question 4',command = click5)
Question4Label = Label(DualFrame,text='Question 4: Dual Price w2 is equal to ',font=("Helvetica", 17, BOLD),background='white')


Question4Entry = Entry(DualFrame, justify = CENTER,width = 10,font=("Helvetica", 17),background='white')
Question4Entry.focus_set()


def callback():
    if Question4Entry.get() == '0':
        Question4Entry.delete(0, END)
        Question4Entry.insert(0, "Correct")
        Question4Entry.configure(state=DISABLED)
        DualPrice2.config(text='0')
        DualPrice2.config(fg='lime green')
        Question4Answer.grid_remove()
        ContinueButton2.grid(row=20,column=16)
        global Score
        Score = Score + 1
    else:
        Question4Entry.delete(0, END)
        Question4Entry.insert(0, "False")
        Question4Entry.configure(state=DISABLED)
        DualPrice2.config(text='0')
        RightAnswer.grid(row=21,column=16)
        Question4Answer.grid_remove()
        ContinueButton2.grid(row=22,column=16)
    

    
Question4Answer = ttk.Button(DualFrame,text = 'Enter',command = lambda : callback())

RightAnswer = Label(DualFrame,text='Correct answer is 0.',font=("Helvetica", 17),background='white')

Question5Frame = LabelFrame(root,background='white',pady=5,padx=5)
Question5Title = Label(Question5Frame,text='Redused Cost Calculation',font=("Helvetica", 25, BOLD),background='white',pady=5)
Question5Intro1 = Label(Question5Frame,text='The rest of the Dual Prices are going to be 0 as well,',font=("Helvetica", 15),background='white')
Question5Intro2 = Label(Question5Frame,text='since the base variables in Iteration 1',font=("Helvetica", 15),background='white')
Question5Intro3 = Label(Question5Frame,text='are the slack variables (x3,x4,x5,x6).',font=("Helvetica", 15),background='white')
Question5Intro4 = Label(Question5Frame,text='This means that the objective coefficients',font=("Helvetica", 15),background='white')
Question5Intro5 = Label(Question5Frame,text='of the base variables and the Dual Prices w are all 0.',font=("Helvetica", 15),background='white')
Question5Intro6 = Label(Question5Frame,text='We can now calculate the Reduced Costs s.',font=("Helvetica", 15),background='white')
Question5Intro7 = Label(Question5Frame,text='For example the equation for Reduced Cost s1 is:',font=("Helvetica", 15),background='white')
Question5Intro8 = Label(Question5Frame,text='Which is equal to: ',font=("Helvetica", 15),background='white')

imgReduced1 = PhotoImage(file=".img\\Reduced1.png")
imgReduced2 = PhotoImage(file=".img\\Reduced2.png")


ReducedImg1 =  Label(Question5Frame,font=("Helvetica", 17),background='white')
ReducedImg1.config(image=imgReduced1)
ReducedImg2 =  Label(Question5Frame,font=("Helvetica", 17),background='white')
ReducedImg2.config(image=imgReduced2)


def click6():
    
    DualFrame.grid_remove()
    Question5Frame.grid(row=0,column=17,rowspan=10,padx=140,pady=5)
    Question5Title.grid(row=0,column=19,columnspan=10)
    Question5Intro1.grid(row=1,column=19,columnspan=10)
    Question5Intro2.grid(row=2,column=19,columnspan=10)
    Question5Intro3.grid(row=3,column=19,columnspan=10)
    Question5Intro4.grid(row=4,column=19,columnspan=10)
    Question5Intro5.grid(row=5,column=19,columnspan=10)
    Question5Intro6.grid(row=6,column=19,columnspan=10)
    Question5Intro7.grid(row=7,column=19,columnspan=10)
    ReducedImg1.grid(row=8,column=19,columnspan=10)
    Question5Intro8.grid(row=9,column=19,columnspan=10)
    ReducedImg2.grid(row=10,column=19,columnspan=10)
    BaseFunctionCoefficient1.config(fg='black')
    BaseFunctionCoefficient2.config(fg='black')
    BaseFunctionCoefficient3.config(fg='black')
    BaseFunctionCoefficient4.config(fg='black')
    A12.config(fg='black')
    A22.config(fg='black')
    A32.config(fg='black')
    A42.config(fg='black')
    DualPrice2.config(fg='black',font=("Helvetica", 20))
    DualPrice3.grid(row=10,column=5)
    DualPrice4.grid(row=10,column=6)
    DualPrice5.grid(row=10,column=7)
    DualPrice6.grid(row=10,column=8)
    ReducedCost1.grid(row=11,column=3)
    ReducedCost1.config(fg='dark orange')
    DualPrice1.config(fg='red')
    FunctionCoefficient1.config(fg='blue')
    Question5Button.grid(row=11,column=19,columnspan=10)
    
def click7():
    
    ReducedCost1.config(fg='black')
    DualPrice1.config(fg='black')
    FunctionCoefficient1.config(fg='black')
    
    SetReducedCostColour('dark orange')
    ReducedCost1.config(fg='black')
    SetReducedCostText('5', '?', '?', '?', '?', '?')
    ReducedCost2.grid(row= 11,column=4)
    ReducedCost3.grid(row= 11,column=5)
    ReducedCost4.grid(row= 11,column=6)
    ReducedCost5.grid(row= 11,column=7)
    ReducedCost6.grid(row= 11,column=8)
    
    SetDualPriceColour('red')
    DualPrice1.config(fg='black')
    
    FunctionCoefficient2.config(fg='blue')
    FunctionCoefficient3.config(fg='blue')
    FunctionCoefficient4.config(fg='blue')
    FunctionCoefficient5.config(fg='blue')
    FunctionCoefficient6.config(fg='blue')
    
    Question5Button.grid_remove()
    Question5Label1.grid(row=12,column=19,columnspan=10)
    Question5Label2.grid(row=13,column=19,columnspan=10)
    Question5Entry.grid(row=14,column=19,columnspan=10)
    Question5Answer.grid(row=15,column=19,columnspan=10)
    
    
ContinueButton2 = ttk.Button(DualFrame,text = 'Continue',command= lambda : click6())
Question5Button = ttk.Button(Question5Frame,text='Question 5',command= lambda : click7())
Question5Label1 = Label(Question5Frame,text='Question 5: Which are the values',font=("Helvetica", 15, BOLD),background='white')
Question5Label2 = Label(Question5Frame,text=' for Reduced Costs s2,s3,s4,s5,s6 ?',font=("Helvetica", 15, BOLD),background='white')
Question5Entry = Entry(Question5Frame, justify = CENTER,width = 35,font=("Helvetica", 12, ITALIC),background='white')
Question5Entry.insert(0, "Format your answer as s2,s3,s4,s5,s6")
Question5Answer = ttk.Button(Question5Frame,text='Enter',command= lambda : callback1())
Question5Entry.focus_set()
ContinueButton3 = ttk.Button(Question5Frame,text = 'Continue',command= lambda : click8())

def callback1():
    if Question5Entry.get() == '4,0,0,0,0':
        Question5Entry.delete(0, END)
        Question5Entry.insert(0, "Correct")
        Question5Entry.configure(state=DISABLED)
        SetReducedCostText('5', '4', '0', '0', '0', '0')
        Question5Answer.grid_remove()
        ContinueButton3.grid(row=16,column=19,columnspan=10)
        global Score
        Score = Score + 1
        
    else:
        Question5Entry.delete(0, END)
        Question5Entry.insert(0, "False")
        Question5Entry.configure(state=DISABLED)
        SetReducedCostText('5', '4', '0', '0', '0', '0')
        Question5Answer.grid_remove()
        ContinueButton3.grid(row=16,column=19,columnspan=10)
    

EnterVarFrame = LabelFrame(root,background='white')
EnterVarTitle = Label(EnterVarFrame,text= 'Step 1: Select the Entering Variable',font=("Helvetica", 25, BOLD),background='white',padx=5,pady=5)
EnterVar1 = Label(EnterVarFrame,text='The Reduced Cost of a variable is the corresponding change',font=("Helvetica", 15),background='white')
EnterVar2 = Label(EnterVarFrame,text='in the objective function per unit increase of the variable.',font=("Helvetica", 15),background='white')
EnterVar3 = Label(EnterVarFrame,text='For example: Increasing x1 by 1 unit would increase',font=("Helvetica", 15),background='white')
EnterVar4 = Label(EnterVarFrame,text='the objective function value by 5, since s1 = 5.',font=("Helvetica", 15),background='white')
EnterVar5 = Label(EnterVarFrame,text='In order to determine the entering variable we need to find the variable',font=("Helvetica", 15),background='white')
EnterVar6 = Label(EnterVarFrame,text='with the maximum (positive) Reduced Cost in a maximazation problem,',font=("Helvetica", 15),background='white')
EnterVar7 = Label(EnterVarFrame,text='or the variable with the minimum (negative) Reduced Cost',font=("Helvetica", 15),background='white')
EnterVar8 = Label(EnterVarFrame,text='in a minimazation problem.',font=("Helvetica", 15),background='white')
EnterVar9 = Label(EnterVarFrame,text='Question 6: We are solving a maximazation problem,',font=("Helvetica", 15, BOLD),background='white')
EnterVar10 = Label(EnterVarFrame,text='which variable is the entering one?',font=("Helvetica", 15, BOLD),background='white')
Question6Entry = Entry(EnterVarFrame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question6Entry.insert(0, "Format your answer as x followed by the index of the variable (e.g. x3)")
Question6Answer = ttk.Button(EnterVarFrame,text='Enter',command= lambda : callback2())
Question6Entry.focus_set()    

def click8():
    SetReducedCostColour('black')
    SetDualPriceColour('black')
    FunctionCoefficient2.config(fg='black')
    FunctionCoefficient3.config(fg='black')
    FunctionCoefficient4.config(fg='black')
    FunctionCoefficient5.config(fg='black')
    FunctionCoefficient6.config(fg='black')
    
    Question5Frame.grid_remove()
    EnterVarFrame.grid(row=0,column=17,rowspan=10,padx=65,pady=5)
    EnterVarTitle.grid(row=0,column=19,columnspan=5)
    EnterVar1.grid(row=1,column=19,columnspan=5)
    EnterVar2.grid(row=2,column=19,columnspan=5)
    EnterVar3.grid(row=3,column=19,columnspan=5)
    EnterVar4.grid(row=4,column=19,columnspan=5)
    EnterVar5.grid(row=5,column=19,columnspan=5)
    EnterVar6.grid(row=6,column=19,columnspan=5)
    EnterVar7.grid(row=7,column=19,columnspan=5)
    EnterVar8.grid(row=8,column=19,columnspan=5)
    EnterVar9.grid(row=9,column=19,columnspan=5)
    EnterVar10.grid(row=10,column=19,columnspan=5)
    Question6Entry.grid(row=11,column=19,columnspan=5)
    Question6Answer.grid(row=12,column=19,columnspan=5)
    
    
def callback2():
    if Question6Entry.get() == 'x1':
        Question6Entry.delete(0, END)
        Question6Entry.insert(0, "Correct")
        Question6Entry.configure(state=DISABLED)
        ReducedCost1.config(fg='dark orange')
        Variable1.config(fg='dark orange')
        Question6Answer.grid_remove()
        Question7Button.grid(row=13,column=19,columnspan=5)
        global Score
        Score = Score + 1
    else:
        Question6Entry.delete(0, END)
        Question6Entry.insert(0, "False, x1 is the entering variable")
        Question6Entry.configure(state=DISABLED)
        ReducedCost1.config(fg='dark orange')
        Variable1.config(fg='dark orange')
        Question6Answer.grid_remove()
        Question7Button.grid(row=13,column=19,columnspan=5)

def click9():
    ReducedCost1.config(fg='black')
    Variable1.config(fg='black')
    Question7Button.grid_remove()
    EnterVar8.grid_remove()
    EnterVar9.grid_remove()
    Question6Entry.grid_remove()
    Question7Label1.grid(row=8,column=19,columnspan=5)
    Question7Label2.grid(row=9,column=19,columnspan=5)
    Question7Label3.grid(row=10,column=19,columnspan=5)
    Question7Label4.grid(row=11,column=19,columnspan=5)
    Test7Answer1.grid(row=12,column=19,columnspan=5)
    Test7Answer2.grid(row=13,column=19,columnspan=5)
    EnterVarFrame.grid(row=0,column=17,rowspan=15,padx=65,pady=25)
    
def Question7Click(value):
    if value == True:
        Test7Answer1.config(background="lime green")
        Test7Answer1.config(state=DISABLED)
        Test7Answer2.config(state=DISABLED)
        Question7Explanation1.grid(row=14,column=19,columnspan=5)
        Question7Explanation2.grid(row=15,column=19,columnspan=5)
        ContinueButton4.grid(row=16,column=21)
        global Score
        Score = Score + 1
        
    else:
        Test7Answer2.config(background="firebrick")
        Test7Answer1.config(state=DISABLED)
        Test7Answer2.config(state=DISABLED)
        Question7Explanation1.grid(row=14,column=19,columnspan=5)
        Question7Explanation2.grid(row=15,column=19,columnspan=5)
        ContinueButton4.grid(row=16,column=21)
        
Question7Button = ttk.Button(EnterVarFrame,text='Question 7',command= lambda : click9())
Question7Label1 = Label(EnterVarFrame,text= 'Question 7:',font=("Helvetica", 15, BOLD),background='white')
Question7Label2 = Label(EnterVarFrame,text= 'If all the reduced costs were less than or equal to zero,',font=("Helvetica", 15, BOLD),background='white')
Question7Label3 = Label(EnterVarFrame,text= 'we cannot select an entering variable',font=("Helvetica", 15, BOLD),background='white')
Question7Label4 = Label(EnterVarFrame,text= 'and the simplex algorith stops (we found the optimal solution).',font=("Helvetica", 15, BOLD),background='white')
Test7Answer1 = Radiobutton(EnterVarFrame, text='True', variable=answer, value=True,command=lambda: Question7Click(answer.get()),font=("Helvetica", 15),background='white')
Test7Answer2 = Radiobutton(EnterVarFrame, text='False', variable=answer, value=False,command=lambda: Question7Click(answer.get()),font=("Helvetica", 15),background='white')
Question7Explanation1 = Label(EnterVarFrame,text = 'The stop condition for the simplex algorithm',font=("Helvetica", 15),background='white')
Question7Explanation2 = Label(EnterVarFrame,text = 'is met when all Reduced Costs are non-positive (max problem).',font=("Helvetica", 15),background='white')



def click10():
    
    ExitVarFrame.grid(row=0,column=17,rowspan=120,padx=75,pady=5)
    ExitVarTitle.grid(row=0,column=19,columnspan=5)
    ExitVar1.grid(row=1,column=19,columnspan=5)
    ExitVar2.grid(row=2,column=19,columnspan=5)
    ExitVar3.grid(row=3,column=19,columnspan=5)
    ExitVar4.grid(row=4,column=19,columnspan=5)
    ExitVar5.grid(row=5,column=19,columnspan=5)
    ExitVar6.grid(row=6,column=19,columnspan=5)
    ExitVar7.grid(row=7,column=19,rowspan=2,columnspan=5)
    ExitVar8.grid(row=9,column=19,columnspan=5)
    ExitVar9.grid(row=10,column=19,columnspan=5)
    ExitVar10.grid(row=11,column=19,columnspan=5)
    ExitVar11.grid(row=12,column=19,columnspan=5)
    ExitVar12.grid(row=13,column=19,columnspan=5)
    ExitVar13.grid(row=14,column=19,columnspan=5)
    Question8Button.grid(row=15,column=21)
    RatioTest1.grid(row=5,column=12,columnspan=2)
    
    EnterVarFrame.grid_remove()
    
    A11.config(fg='red')
    A21.config(fg='red')
    A31.config(fg='red')
    A41.config(fg='red')
    RHS1.config(fg='blue')
    RatioTest1.config(fg='dark orange')
    
def click11():
    Question8Button.grid_remove()
    Question8Label.grid(row=15,column=19,columnspan=5)
    Question8Entry.grid(row=16,column=19,columnspan=5)
    Question8Answer.grid(row=17,column=19,columnspan=5)
    RHS1.config(fg='black')
    RatioTest1.config(fg='black')

def callback3():
    if Question8Entry.get() == 'x5,x6':
        Question8Entry.delete(0, END)
        Question8Entry.insert(0, "Correct")
        Question8Entry.configure(state=DISABLED)
        RatioTest3.grid(row=7,column=12,columnspan=2)
        RatioTest4.grid(row=8,column=12,columnspan=2)
        RatioTest3.config(fg='dark orange')
        RatioTest4.config(fg='dark orange')
        Question8Answer.grid_remove()
        Question9Button.grid(row=17,column=21)
        global Score
        Score = Score + 1
    else:
        Question8Entry.delete(0, END)
        Question8Entry.insert(0, "False, x5,x6 is the right answer")
        Question8Entry.configure(state=DISABLED)
        RatioTest3.grid(row=7,column=12,columnspan=2)
        RatioTest4.grid(row=8,column=12,columnspan=2)
        RatioTest3.config(fg='dark orange')
        RatioTest4.config(fg='dark orange')
        Question8Answer.grid_remove()
        Question9Button.grid(row=17,column=21)
        
    

ContinueButton4 = ttk.Button(EnterVarFrame,text='Continue',command=lambda: click10())
ExitVarFrame = LabelFrame(root,background='white',padx=5)
ExitVarTitle= Label(ExitVarFrame, text= 'Step 2: Select the Leaving Variable',font=("Helvetica", 25, BOLD),background='white')
ExitVar1 = Label(ExitVarFrame,text='The column for the entering basic variable is called the pivot column.',font=("Helvetica", 15),background='white')
ExitVar2 = Label(ExitVarFrame,text='The pivot column is highlighted for ease of reference in red.',font=("Helvetica", 15),background='white')
ExitVar3 = Label(ExitVarFrame,text='The minimum ratio test is used to determine the leaving basic variable.',font=("Helvetica", 15),background='white')
ExitVar4 = Label(ExitVarFrame,text='This test determines which constraint most limits the increase,',font=("Helvetica", 15),background='white')
ExitVar5 = Label(ExitVarFrame,text='in the value of the entering basic variable.',font=("Helvetica", 15),background='white')
ExitVar6 = Label(ExitVarFrame,text='Looking only at the entries in the pivot column for the constraint rows,',font=("Helvetica", 15),background='white')
ExitVar7 = Label(ExitVarFrame,text='we calculate:',font=("Helvetica", 15),background='white')
ExitVar8 = Label(ExitVarFrame,background='white')
ExitVar9 = Label(ExitVarFrame,text='If a coefficient of the entering variable is zero or negative, ',font=("Helvetica", 15),background='white')
ExitVar10 = Label(ExitVarFrame,text='we enter no limit and the basic variable of that row ',font=("Helvetica", 15),background='white')
ExitVar11 = Label(ExitVarFrame,text='is not eligible for a leaving variable.',font=("Helvetica", 15),background='white')
ExitVar12 = Label(ExitVarFrame,text='For example the Ratio Test for x3: .',font=("Helvetica", 15),background='white')
ExitVar13 = Label(ExitVarFrame,background='white')
Question8Button = ttk.Button(ExitVarFrame,text='Question 8',command=lambda: click11())
Question8Label = Label(ExitVarFrame,text='Question 8: For which variables the Ratio Test gives no limit? ',font=("Helvetica", 15, BOLD),background='white')
Question8Entry = Entry(ExitVarFrame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question8Entry.insert(0, "Format your answer as x followed by the index of the variable (e.g. x3,x4).")
Question8Answer = ttk.Button(ExitVarFrame,text='Enter',command= lambda : callback3())
Question8Entry.focus_set() 

def click12():
    Question8Label.grid_remove()
    Question8Entry.grid_remove()
    Question8Answer.grid_remove()
    Question9Button.grid_remove()
    Question9Label.grid(row=15,column=19,columnspan=5)
    Question9Entry.grid(row=16,column=19,columnspan=5)
    Question9Answer.grid(row=17,column=19,columnspan=5)
    RatioTest3.config(fg='black')
    RatioTest4.config(fg='black')
    
def callback4():
    if Question9Entry.get() == '6':
        Question9Entry.delete(0, END)
        Question9Entry.insert(0, "Correct")
        Question9Entry.configure(state=DISABLED)
        RatioTest2.grid(row=6,column=12,columnspan=2)
        RatioTest2.config(fg='dark orange')
        Question9Answer.grid_remove()
        ContinueButton5.grid(row=18,column=21)
        global Score
        Score = Score + 1
    else:
        Question9Entry.delete(0, END)
        Question9Entry.insert(0, "False, 6 is the right answer")
        Question9Entry.configure(state=DISABLED)
        RatioTest2.grid(row=6,column=12,columnspan=2)
        RatioTest2.config(fg='dark orange')
        Question9Answer.grid_remove()
        ContinueButton5.grid(row=18,column=21)
    
Question9Button = ttk.Button(ExitVarFrame,text='Question 9',command=lambda: click12())
Question9Label = Label(ExitVarFrame,text='Question 9: What is the Ratio Test for variable x4? ',font=("Helvetica", 15, BOLD),background='white')
Question9Entry = Entry(ExitVarFrame, justify = CENTER,width = 35,font=("Helvetica", 12, ITALIC))
Question9Entry.insert(0, "Format your answer as an integer (e.g. 2).")
Question9Answer = ttk.Button(ExitVarFrame,text='Enter',command= lambda : callback4())
Question9Entry.focus_set() 


imgExitVar = PhotoImage(file=".img\\ExitVar.png")
ExitVar8.config(image=imgExitVar)
imgExitVar2 = PhotoImage(file=".img\\ExitVar2.png")
ExitVar13.config(image=imgExitVar2)

def click13():
    ContinueButton5.grid_remove()
    Question9Label.grid_remove()
    Question9Entry.grid_remove()
    Question9Answer.grid_remove()
    RatioTest2.config(fg='black')
    ExitVarFrame.grid(row=0,column=17,rowspan=120,padx=20,pady=5)
    MinRatio1.grid(row=16,column=19)
    MinRatio2.grid(row=17,column=19)
    MinRatio3.grid(row=18,column=19)
    MinRatio4.grid(row=19,column=19)
    MinRatio5.grid(row=20,column=19)
    ContinueButton6.grid(row=21,column=19)
    SetRow1Colour('red')
    RHS1.config(fg='red')
    BaseVariable1.config(fg='dark orange')
    RatioTest1.config(fg='dark orange')
    

ContinueButton5 = ttk.Button(ExitVarFrame,text='Continue',command=lambda: click13())
MinRatio1 = Label(ExitVarFrame,text='The variable with the minimum ratio test is selected as the leaving variable,  ',font=("Helvetica", 15),background='white')
MinRatio2 = Label(ExitVarFrame,text='both for maximazation and minimization problems. ',font=("Helvetica", 15),background='white')
MinRatio3 = Label(ExitVarFrame,text='We select variable x3 (minimum ratio test) as leaving variable  ',font=("Helvetica", 15),background='white')
MinRatio4 = Label(ExitVarFrame,text='The row for the leaving variable is called the pivot row (highlighted in red). ',font=("Helvetica", 15),background='white')
MinRatio5 = Label(ExitVarFrame,text='On the next step we update the tableau using the pivot row and the pivot column. ',font=("Helvetica", 15),background='white')

def click14():
    ExitVarFrame.grid_remove()
    UpdateTableFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=8)
    SetRow1Colour('black')
    A11.config(fg='blue')
    BaseVariable1.config(fg='black')
    RatioTest1.config(fg='black')
    RHS1.config(fg='black')
    UpdateTableTitle.grid(row=0,column=16)
    UpdateTable1.grid(row=1,column=16)
    UpdateTable2.grid(row=2,column=16)
    UpdateTable3.grid(row=3,column=16)
    UpdateTable4.grid(row=4,column=16)
    UpdateTable5.grid(row=5,column=16)
    UpdateTable6.grid(row=6,column=16)
    UpdateTable7.grid(row=7,column=16)
    UpdateTable8.grid(row=8,column=16,rowspan=2)
    UpdateTable9.grid(row=10,column=16)
    UpdateTable10.grid(row=11,column=16,rowspan=2)
    ContinueButton7.grid(row=13,column=16)
    
    
    
def click15():
    ContinueButton7.grid_remove()
    UpdateTableTitle.grid_remove()
    UpdateTable1.grid_remove()
    UpdateTable2.grid_remove()
    UpdateTable3.grid_remove()
    UpdateTable4.grid_remove()
    UpdateTable5.grid_remove()
    UpdateTable6.grid_remove()
    UpdateTable7.grid_remove()
    UpdateTable8.grid_remove()
    UpdateTable9.grid_remove()
    UpdateTable10.grid_remove()
    UpdateTableFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=3)
    UpdateTable11.grid(row=0,column=16)
    UpdateTable12.grid(row=1,column=16)
    UpdateTable13.grid(row=2,column=16)
    UpdateTable14.grid(row=3,column=16)
    UpdateTable15.grid(row=4,column=16)
    UpdateTable16.grid(row=5,column=16)
    UpdateTable17.grid(row=6,column=16)
    UpdateTable18.grid(row=7,column=16)
    Question10Button.grid(row=8,column=16)
    SetRow1Colour('red')
    SetRow1Text('1','2/3','1/6','0','0','0')
    RHS1.config(text='4',fg='red')
       
    
ContinueButton6 = ttk.Button(ExitVarFrame,text='Continue',command=lambda: click14())
UpdateTableFrame = LabelFrame(root,background='white',pady=5)
UpdateTableTitle = Label(UpdateTableFrame,text='Step 3: Update the tableau',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5)
UpdateTable1 = Label(UpdateTableFrame,text= 'Now that the entering and leaving basic variables are known,',font=("Helvetica", 17),background='white')
UpdateTable2 = Label(UpdateTableFrame,text= 'we can move to the new and better basic feasible solution.',font=("Helvetica", 17),background='white')
UpdateTable3 = Label(UpdateTableFrame,text= 'Step 3.1: Pivot Element',font=("Helvetica", 20, BOLD),background='white')
UpdateTable4 = Label(UpdateTableFrame,text= 'The tableau element where the pivot row and the pivot column insteresect',font=("Helvetica", 17),background='white')
UpdateTable5 = Label(UpdateTableFrame,text= 'is known as the pivot element (highlighted in blue).',font=("Helvetica", 17),background='white')
UpdateTable6 = Label(UpdateTableFrame,text= 'Step 3.2: Update the pivot row',font=("Helvetica", 20, BOLD),background='white')
UpdateTable7 = Label(UpdateTableFrame,text= 'We update the pivot row using simple Gaussian operations:',font=("Helvetica", 17),background='white')
UpdateTable8 = Label(UpdateTableFrame,background='white')
UpdateTable9 = Label(UpdateTableFrame,text= 'Which is equal to: ',font=("Helvetica", 17),background='white')
UpdateTable10 = Label(UpdateTableFrame,background='white')
UpdateTable11 = Label(UpdateTableFrame,text= 'Step 3.3: Update the remaining rows',font=("Helvetica", 20, BOLD),background='white')
UpdateTable12 = Label(UpdateTableFrame,text= 'We calculate the Updated j row through the Gaussian operation:',font=("Helvetica", 17),background='white')
UpdateTable13 = Label(UpdateTableFrame,background='white')   
UpdateTable14 = Label(UpdateTableFrame,text= 'for each of the j remaining rows.',font=("Helvetica", 17),background='white')
UpdateTable15 = Label(UpdateTableFrame,text= 'Example: Updating Row 2',font=("Helvetica", 17),background='white')               
UpdateTable16 = Label(UpdateTableFrame,background='white')
UpdateTable17 = Label(UpdateTableFrame,text= 'Which is equal to: ',font=("Helvetica", 17),background='white')
UpdateTable18 = Label(UpdateTableFrame,background='white')

ContinueButton7 = ttk.Button(UpdateTableFrame,text='Continue',command=lambda: click15())

imgUpdateTable1 = PhotoImage(file=".img\\UpdateTable1.png")
UpdateTable8.config(image=imgUpdateTable1)
imgUpdateTable2 = PhotoImage(file=".img\\UpdateTable2.png")
UpdateTable10.config(image=imgUpdateTable2)
imgUpdateTable3 = PhotoImage(file=".img\\UpdateTable3.png")
UpdateTable13.config(image=imgUpdateTable3)
imgUpdateTable4 = PhotoImage(file=".img\\UpdateTable4.png")
UpdateTable16.config(image=imgUpdateTable4)
imgUpdateTable5 = PhotoImage(file=".img\\UpdateTable5.png")
UpdateTable18.config(image=imgUpdateTable5)

def click16():
    Question10Button.grid_remove()
    SetRow2Colour('red')
    SetRow2Text('0','4/3','-1/6','1','0','0')
    RHS2.config(text='2',fg='red')
    UpdateTableFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=0)
    Question10Label.grid(row=8,column=16)
    Question10Help.grid(row=9,column=16)
    Test10Answer1.grid(row=10,column=16,columnspan =50)
    Test10Answer2.grid(row=11,column=16,columnspan =50)
    Test10Answer3.grid(row=12,column=16,columnspan =50)
    

def Question10Click(value):
    if value == 1:
        Test10Answer1.config(background="firebrick")
        Test10Answer2.config(background="lime green")
        Test10Answer1.config(state=DISABLED)
        Test10Answer2.config(state=DISABLED)
        Test10Answer3.config(state=DISABLED)
        Question11Button.grid(row=13,column=16,columnspan = 50)
        SetRow3Colour('red')
        SetRow3Text('0','5/3','1/6','0','1','0')
        RHS3.config(text='5',fg='red')
        
        
    elif value == 2:
        Test10Answer2.config(background="lime green")
        Test10Answer1.config(state=DISABLED)
        Test10Answer2.config(state=DISABLED)
        Test10Answer3.config(state=DISABLED)
        Question11Button.grid(row=13,column=16,columnspan = 50)
        SetRow3Colour('red')
        SetRow3Text('0','5/3','1/6','0','1','0')
        RHS3.config(text='5',fg='red')
        global Score
        Score = Score + 1

        
    elif value == 3:
        Test10Answer3.config(background="firebrick")
        Test10Answer2.config(background="lime green")
        Test10Answer1.config(state=DISABLED)
        Test10Answer2.config(state=DISABLED)
        Test10Answer3.config(state=DISABLED)
        Question11Button.grid(row=13,column=16,columnspan = 50)
        SetRow3Colour('red')
        SetRow3Text('0','5/3','1/6','0','1','0')
        RHS3.config(text='5',fg='red')

img1Question10 = PhotoImage(file=".img\\1Question10.png")
img2Question10 = PhotoImage(file=".img\\2Question10.png")
img3Question10 = PhotoImage(file=".img\\3Question10.png")

Question10Button = ttk.Button(UpdateTableFrame,text='Question 10',command=lambda: click16())
Question10Label = Label(UpdateTableFrame,text='Question 10: Which one is the correct updated row 3?',font=("Helvetica", 17, BOLD),background='white')
Question10Help = Label(UpdateTableFrame,text='(3rd tableau element in pivot column = -1)',font=("Helvetica", 17),background='white')
Test10Answer1 = Radiobutton(UpdateTableFrame, variable=answerInt, value=1,command=lambda: Question10Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test10Answer1.config(image=img1Question10)

Test10Answer2 = Radiobutton(UpdateTableFrame, variable=answerInt, value=2,command=lambda: Question10Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test10Answer2.config(image=img2Question10)

Test10Answer3 = Radiobutton(UpdateTableFrame, variable=answerInt, value=3,command=lambda: Question10Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test10Answer3.config(image=img3Question10)

def click17():
    Question11Button.grid_remove()
    Question10Label.grid_remove()
    Test10Answer1.grid_remove()
    Test10Answer2.grid_remove()
    Test10Answer3.grid_remove()
    Question11Label.grid(row=8,column=16)
    Question11Help.grid(row=9,column=16)
    Test11Answer1.grid(row=10,column=16,columnspan =50)
    Test11Answer2.grid(row=11,column=16,columnspan =50)
    Test11Answer3.grid(row=12,column=16,columnspan =50)


def Question11Click(value):
    if value == 1:
        Test11Answer1.config(background="firebrick")
        Test11Answer3.config(background="lime green")
        Test11Answer1.config(state=DISABLED)
        Test11Answer2.config(state=DISABLED)
        Test11Answer3.config(state=DISABLED)
        SetRow4Colour('red')
        SetRow4Text('0','1','0','0','0','1')
        RHS4.config(fg='red')
        ContinueButton8.grid(row=13,column=16)
        
        
    elif value == 2:
        Test11Answer3.config(background="lime green")
        Test11Answer2.config(background="firebrick")
        Test11Answer1.config(state=DISABLED)
        Test11Answer2.config(state=DISABLED)
        Test11Answer3.config(state=DISABLED)
        SetRow4Colour('red')
        SetRow4Text('0','1','0','0','0','1')
        RHS4.config(fg='red')
        ContinueButton8.grid(row=13,column=16)
        
    elif value == 3:
        Test11Answer3.config(background="lime green")
        Test11Answer1.config(state=DISABLED)
        Test11Answer2.config(state=DISABLED)
        Test11Answer3.config(state=DISABLED)
        SetRow4Colour('red')
        SetRow4Text('0','1','0','0','0','1')
        RHS4.config(fg='red')
        ContinueButton8.grid(row=13,column=16)
        global Score
        Score = Score + 1

img1Question11 = PhotoImage(file=".img\\1Question11.png")
img2Question11 = PhotoImage(file=".img\\2Question11.png")
img3Question11 = PhotoImage(file=".img\\3Question11.png")
    
Question11Button = ttk.Button(UpdateTableFrame,text='Question 11',command=lambda: click17())
Question11Label = Label(UpdateTableFrame,text='Question 11: Which one is the correct updated row 4?',font=("Helvetica", 17, BOLD),background='white')
Question11Help = Label(UpdateTableFrame,text='(4th tableau element in pivot column = 0)',font=("Helvetica", 17),background='white')
Test11Answer1 = Radiobutton(UpdateTableFrame, variable=answerInt, value=1,command=lambda: Question11Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test11Answer1.config(image=img1Question11)

Test11Answer2 = Radiobutton(UpdateTableFrame, variable=answerInt, value=2,command=lambda: Question11Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test11Answer2.config(image=img2Question11)

Test11Answer3 = Radiobutton(UpdateTableFrame, variable=answerInt, value=3,command=lambda: Question11Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test11Answer3.config(image=img3Question11)

def click18():
    SetRow1Colour('black')
    SetRow2Colour('black')
    SetRow3Colour('black')
    SetRow4Colour('black')
    SetRHSColour('black')
    ObjectiveFunctionValue.config(text='20')
    ObjectiveFunctionValue.config(fg='red')
    BaseVariable1.config(text= 'x' + '\u2081',font=("Helvetica", 20),fg='red')
    SetDualPriceText('', '', '','', '', '')
    SetReducedCostText('', '', '', '', '', '')
    SetRatioTestText('', '', '', '')
    BaseFunctionCoefficient1.config(text='5',fg='red')
    UpdateTableFrame.grid_remove()
    FinalFormFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=28)
    ContinueButton9.grid(row=9,column=0)
    
    
    

ContinueButton8 = ttk.Button(UpdateTableFrame,text='Continue',command=lambda: click18())

imgFinalForm = PhotoImage(file=".img\\Final Form.png")

FinalFormFrame = LabelFrame(root,background='white',padx=5,pady=5)
FinalForm1 = Label(FinalFormFrame,text='Step 3.4: Final Form of the tableau',font=("Helvetica", 25, BOLD),background='white',pady=5).grid(row=0,column=0)
FinalForm2 = Label(FinalFormFrame,text='We need to update the basic variables with the entering variable',font=("Helvetica", 15),background='white').grid(row=1,column=0)
FinalForm3 = Label(FinalFormFrame,text='as well as the objective function coefficients of the basic variables.',font=("Helvetica", 15),background='white').grid(row=2,column=0)
FinalForm4 = Label(FinalFormFrame,text='Entering variable x1 and its coefficient is highlighted in red.',font=("Helvetica", 15),background='white').grid(row=3,column=0)
FinalForm5 = Label(FinalFormFrame,text='The objective function value in this first iteration of the simplex algorithm',font=("Helvetica", 15),background='white').grid(row=4,column=0)
FinalForm6 = Label(FinalFormFrame,text='is 20, which is calculated using the following equation:',font=("Helvetica", 15),background='white').grid(row=5,column=0)
FinalForm7 = Label(FinalFormFrame,background='white')
FinalForm7.config(image=imgFinalForm)
FinalForm7.grid(row=6,column=0)
FinalForm8 = Label(FinalFormFrame,text='We also delete the Shadow prices, Reduced Costs and the Ratio Test values',font=("Helvetica", 15),background='white').grid(row=7,column=0)
FinalForm9 = Label(FinalFormFrame,text='since we need to calculate them once again in the next step.',font=("Helvetica", 15),background='white').grid(row=8,column=0)

def click19():
    ContinueButton9.grid_remove()
    BaseVariable1.config(fg='black')
    BaseFunctionCoefficient1.config(fg='black')
    ObjectiveFunctionValue.config(fg='black')
    FinalFormFrame.grid_remove()
    StopCondiFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=20)
    Question12Button.grid(row=5,column=0)
    
ContinueButton9 = ttk.Button(FinalFormFrame,text='Continue',command=lambda: click19())

StopCondiFrame = LabelFrame(root,padx=5,pady=5,background='white')
StopCondi1 = Label(StopCondiFrame,text='Step 4: Check the stop condition.',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5).grid(row=0,column=0)
StopCondi2 = Label(StopCondiFrame,text='In this final step for the first iteration,',font=("Helvetica", 15),background='white').grid(row=1,column=0)
StopCondi3 = Label(StopCondiFrame,text='we have to calculate the Dual prices and the Reduced Costs',font=("Helvetica", 15),background='white').grid(row=2,column=0)
StopCondi4 = Label(StopCondiFrame,text='for the now updated tableau and check the stop condition.',font=("Helvetica", 15),background='white').grid(row=3,column=0)
StopCondi5 = Label(StopCondiFrame,text='the stop condition is met when all the Reduced cost values are negative or zero.',font=("Helvetica", 15),background='white').grid(row=4,column=0)

img1StopCondi = PhotoImage(file=".img\\Dual1.png")
img2StopCondi = PhotoImage(file=".img\\Right2.png")

def click20():
    Question12Button.grid_remove()
    StopCondiFrame.grid(row=0,column=17,rowspan=120,pady=25,padx=18)
    Question12Label1.grid(row=5,column=0)
    Question12Label2.grid(row=6,column=0)
    Question12Label3.grid(row=7,column=0)
    Question12Entry.grid(row=8,column=0)
    Question12Answer.grid(row=9,column=0)
    
def callback5():
    if Question12Entry.get() == '5,10/3,5/6,0,0,0':
        Question12Entry.delete(0, END)
        Question12Entry.insert(0, "Correct")
        Question12Entry.configure(state=DISABLED)
        SetDualPriceText('5', '10/3', '5/6','0', '0', '0')
        SetDualPriceFontSize(19)
        DualPrice2.config(font=("Helvetica", 16))
        DualPrice3.config(font=("Helvetica", 16))
        SetDualPriceColour('dark orange')
        Question12Answer.grid_remove()
        Question13Button.grid(row=10,column=0)
        global Score
        Score = Score + 1
    else:
        Question12Entry.delete(0, END)
        Question12Entry.insert(0, "False. Answer highlighted in the tableau.")
        Question12Entry.configure(state=DISABLED)
        SetDualPriceText('5', '10/3', '5/6','0', '0', '0')
        SetDualPriceFontSize(19)
        DualPrice2.config(font=("Helvetica", 16))
        DualPrice3.config(font=("Helvetica", 16))
        SetDualPriceColour('dark orange')
        Question12Answer.grid_remove()
        Question13Button.grid(row=10,column=0)

def click21():
    Question13Button.grid_remove()
    Question12Label1.grid_remove()
    Question12Label2.grid_remove()
    Question12Label3.grid_remove()
    Question12Entry.grid_remove()
    Question13Label1.grid(row=5,column=0)
    Question13Label2.grid(row=6,column=0)
    Question13Label3.grid(row=7,column=0)
    Question13Entry.grid(row=8,column=0)
    Question13Answer.grid(row=9,column=0)
    

Question12Button = ttk.Button(StopCondiFrame,text='Question 12',command=lambda: click20())
Question12Label1 = Label(StopCondiFrame,text='Question 12: We calculate Shadow Price w using the equation:',font=("Helvetica", 15, BOLD),background='white',pady=5)
Question12Label2 = Label(StopCondiFrame,background='white')
Question12Label2.config(image=img1StopCondi)
Question12Label3 = Label(StopCondiFrame,text='Which are the Shadow Price values for the updated tableau?',font=("Helvetica", 15, BOLD),background='white')
Question12Entry = Entry(StopCondiFrame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question12Entry.insert(0, "Format your answer as 6 real numbers separated by commas (e.g. 3,1/3,1,5,2,5).")
Question12Answer = ttk.Button(StopCondiFrame,text='Enter',command= lambda : callback5())
Question12Entry.focus_set() 

Question13Button = ttk.Button(StopCondiFrame,text='Question 13',command=lambda: click21())
Question13Label1 = Label(StopCondiFrame,text='Question 13: We calculate Reduced Cost values using the equation:',font=("Helvetica", 15, BOLD),background='white',pady=5)
Question13Label2 = Label(StopCondiFrame,background='white')
Question13Label2.config(image=img2StopCondi)
Question13Label3 = Label(StopCondiFrame,text='Which are the Reduced Cost values for the updated tableau?',font=("Helvetica", 15, BOLD),background='white')
Question13Entry = Entry(StopCondiFrame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question13Entry.insert(0, "Format your answer as 6 real numbers separated by commas (e.g. 3,1/3,1,5,2,5).")
Question13Answer = ttk.Button(StopCondiFrame,text='Enter',command= lambda : callback6())
Question13Entry.focus_set()

Question14Button = ttk.Button(StopCondiFrame,text='Question 14',command=lambda: click22())

def callback6():
    if Question13Entry.get() == '0,2/3,-5/6,0,0,0':
        Question13Entry.delete(0, END)
        Question13Entry.insert(0, "Correct")
        Question13Entry.configure(state=DISABLED)
        SetReducedCostText('0', '2/3', '-5/6','0', '0', '0')
        SetReducedCostFontSize(19)
        ReducedCost2.config(font=("Helvetica", 16))
        ReducedCost2.config(font=("Helvetica", 16))
        SetReducedCostColour('dark orange')
        SetDualPriceColour('black')
        Question13Answer.grid_remove()
        Question14Button.grid(row=10,column=0)
        global Score
        Score = Score + 1
    else:
        Question13Entry.delete(0, END)
        Question13Entry.insert(0, "False. Answer highlighted in the tableau.")
        Question13Entry.configure(state=DISABLED)
        SetReducedCostText('0', '2/3', '-5/6','0', '0', '0')
        SetReducedCostFontSize(19)
        ReducedCost2.config(font=("Helvetica", 16))
        ReducedCost3.config(font=("Helvetica", 16))
        SetReducedCostColour('dark orange')
        SetDualPriceColour('black')
        Question13Answer.grid_remove()
        Question14Button.grid(row=10,column=0)

def click22():
    StopCondiFrame.grid(row=0,column=17,rowspan=120,pady=90,padx=20)
    Question14Button.grid_remove()
    Question13Label1.grid_remove()
    Question13Label2.grid_remove()
    Question13Label3.grid_remove()
    Question13Entry.grid_remove()
    SetReducedCostColour('black')
    Question14Label.grid(row=5,column=0)
    Test14Answer1.grid(row=6,column=0)
    Test14Answer2.grid(row=7,column=0)
    Test14Answer3.grid(row=8,column=0)
    

def Question14Click(value):
    if value == 1:
        Test14Answer1.config(background="firebrick")
        Test14Answer2.config(background="lime green")
        Test14Answer1.config(state=DISABLED)
        Test14Answer2.config(state=DISABLED)
        Test14Answer3.config(state=DISABLED)
        ReducedCost2.config(fg='dark orange')
        Variable2.config(fg='dark orange')
        Answer1Correction1.grid(row=9,column=0)
        Answer1Correction2.grid(row=10,column=0)
        ContinueButton10.grid(row=11,column=0)
        
        
    elif value == 2:
        Test14Answer2.config(background="lime green")
        Test14Answer1.config(state=DISABLED)
        Test14Answer2.config(state=DISABLED)
        Test14Answer3.config(state=DISABLED)
        ReducedCost2.config(fg='dark orange')
        Variable2.config(fg='dark orange')
        ContinueButton10.grid(row=9,column=0)
        global Score
        Score = Score + 1
        
    elif value == 3:
        Test14Answer3.config(background="firebrick")
        Test14Answer2.config(background="lime green")
        Test14Answer1.config(state=DISABLED)
        Test14Answer2.config(state=DISABLED)
        Test14Answer3.config(state=DISABLED)
        ReducedCost2.config(fg='dark orange')
        Variable2.config(fg='dark orange')
        Answer3Correction1.grid(row=9,column=0)
        Answer3Correction2.grid(row=10,column=0)
        ContinueButton10.grid(row=11,column=0)
        
Question14Label = Label(StopCondiFrame,text='Question 14: Choose the correct sentence',font=("Helvetica", 17, BOLD),background='white')
Test14Answer1 = Radiobutton(StopCondiFrame,text='The stop condition is met and the simplex algorithm stops.', variable=answerInt, value=1,command=lambda: Question14Click(answerInt.get()),font=("Helvetica", 15),background='white')
Answer1Correction1 = Label(StopCondiFrame,text='The stop condition is not met',font=("Helvetica", 15),background='white')
Answer1Correction2 = Label(StopCondiFrame,text='since there is a positive Reduced Cost value.',font=("Helvetica", 15),background='white')

Test14Answer2 = Radiobutton(StopCondiFrame,text='The stop condition is not met and the entering variable is x2.', variable=answerInt, value=2,command=lambda: Question14Click(answerInt.get()),font=("Helvetica", 15),background='white')

Test14Answer3 = Radiobutton(StopCondiFrame,text='The stop condition is not met and the entering variable is x3', variable=answerInt, value=3,command=lambda: Question14Click(answerInt.get()),font=("Helvetica", 15),background='white')
Answer3Correction1 = Label(StopCondiFrame,text='x2 is the entering variable',font=("Helvetica", 15),background='white')
Answer3Correction2 = Label(StopCondiFrame,text='since its the only one with a positive Reduced Cost value.',font=("Helvetica", 15),background='white')

def click23():
    ContinueButton10.grid_remove()
    StopCondiFrame.grid_remove()
    ReducedCost2.config(fg='black')
    Variable2.config(fg='black')
    Iteration2Frame.grid(row=0,column=17,rowspan=120,pady=5,padx=65)
    Question15Button.grid(row=8,column=0)
    
ContinueButton10 = ttk.Button(StopCondiFrame,text='Start Iteration 2',command=lambda: click23())
Iteration2Frame = LabelFrame(root, padx=5,pady=5,background='white')
Iteration2Label1 = Label(Iteration2Frame, text='Iteration 2',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5).grid(row=0,column=0)
Iteration2Label2 = Label(Iteration2Frame,text='Step 1: Select the entering variable.',font=("Helvetica", 17, BOLD),background='white').grid(row=1,column=0)
Iteration2Label3 = Label(Iteration2Frame,text='We already determined x2 as the entering variable',font=("Helvetica", 15),background='white').grid(row=2,column=0)
Iteration2Label3 = Label(Iteration2Frame,text='since its the only one with a positive Reduced Cost value.',font=("Helvetica", 15),background='white').grid(row=3,column=0)
Iteration2Label4 = Label(Iteration2Frame,text='Step 2: Select the leaving variable.',font=("Helvetica", 17, BOLD),background='white').grid(row=4,column=0)
Iteration2Label5 = Label(Iteration2Frame,text='We calculate the Ratio Test values using the equation: ',font=("Helvetica", 15),background='white').grid(row=5,column=0)
Iteration2Label6 = Label(Iteration2Frame,background='white')
Iteration2Label6.config(image=imgExitVar)
Iteration2Label6.grid(row=6,column=0)
Iteration2Label7 = Label(Iteration2Frame,text='looking only at the entries in the pivot column for the constraint rows.',font=("Helvetica", 15),background='white').grid(row=7,column=0)

def click24():
    Question15Button.grid_remove()
    Iteration2Frame.grid(row=0,column=17,rowspan=120,pady=5,padx=35)
    Question15Label.grid(row=8,column=0)
    Question15Entry.grid(row=9,column=0)
    Question15Answer.grid(row=10,column=0)

def callback7():
    if Question15Entry.get() == '6,3/2,3,2':
        Question15Entry.delete(0, END)
        Question15Entry.insert(0, "Correct")
        Question15Entry.configure(state=DISABLED)
        SetRatioTestText('6', '3/2', '3','2')
        RatioTest3.config(font=("Helvetica", 20))
        RatioTest4.config(font=("Helvetica", 20))
        SetReducedCostColour('black')
        SetRatioTestColour('dark orange')
        Question15Answer.grid_remove()
        Question16Button.grid(row=10,column=0) 
        global Score
        Score = Score + 1
        
    else:
        Question15Entry.delete(0, END)
        Question15Entry.insert(0, "False. Answer highlighted in the tableau.")
        Question15Entry.configure(state=DISABLED)
        SetRatioTestText('6', '3/2', '3','2')
        RatioTest3.config(font=("Helvetica", 20))
        RatioTest4.config(font=("Helvetica", 20))
        SetReducedCostColour('black')
        SetRatioTestColour('dark orange')
        Question15Answer.grid_remove()
        Question16Button.grid(row=10,column=0)
        
Question15Button = ttk.Button(Iteration2Frame,text='Question 15',command=lambda: click24())
Question15Label = Label(Iteration2Frame,text='Question 15: Which are the Ratio Test values for the updated tableau?',font=("Helvetica", 15, BOLD),background='white',pady=5)
Question15Entry = Entry(Iteration2Frame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question15Entry.insert(0, "Format your answer as 4 real numbers separated by commas (e.g. 3,1/3,1,5).")
Question15Answer = ttk.Button(Iteration2Frame,text='Enter',command= lambda : callback7())
Question15Entry.focus_set()

def click25():
    Question16Button.grid_remove()
    Question15Label.grid_remove()
    Question15Entry.grid_remove()
    Question15Answer.grid_remove()
    SetRatioTestColour('black')
    Question16Label.grid(row=8,column=0)
    Question16Entry.grid(row=9,column=0)
    Question16Answer.grid(row=10,column=0)
    Iteration2Frame.grid(row=0,column=17,rowspan=120,pady=5,padx=65)
    
def callback8():
    if Question16Entry.get() == 'x4':
        Question16Entry.delete(0, END)
        Question16Entry.insert(0, "Correct")
        Question16Entry.configure(state=DISABLED)
        RatioTest2.config(fg='dark orange')
        BaseVariable2.config(fg='dark orange')
        Question16Answer.grid_remove()
        ContinueButton11.grid(row=10,column=0)
        global Score
        Score = Score + 1
    else:
        Question16Entry.delete(0, END)
        Question16Entry.insert(0, "False, x4 has the Minimum Ratio Test.")
        Question8Entry.configure(state=DISABLED)
        RatioTest2.config(fg='dark orange')
        BaseVariable2.config(fg='dark orange')
        Question16Answer.grid_remove()
        ContinueButton11.grid(row=10,column=0)
        
def click26():
    Iteration2Frame.grid_remove()
    SetRatioTestColour('black')
    BaseVariable2.config(fg='black')
    No2UpdateTableFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=5)
    SetRow2Colour('red')
    A12.config(fg='red')
    A22.config(fg='blue')
    A32.config(fg='red')
    A42.config(fg='red')
        
Question16Button = ttk.Button(Iteration2Frame,text='Question 16',command=lambda: click25())
Question16Label = Label(Iteration2Frame,text='Question 16: Which variable is the leaving variable? ',font=("Helvetica", 15, BOLD),background='white')
Question16Entry = Entry(Iteration2Frame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question16Entry.insert(0, "Format your answer as x followed by the index of the variable (e.g. x3).")
Question16Answer = ttk.Button(Iteration2Frame,text='Enter',command= lambda : callback8())
Question16Entry.focus_set()
    

ContinueButton11 = ttk.Button(Iteration2Frame,text='Continue',command=lambda: click26()) 
No2UpdateTableFrame = LabelFrame(root,background='white',pady=5)
No2UpdateTableTitle = Label(No2UpdateTableFrame,text='Step 3: Update the tableau',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5)
No2UpdateTableTitle.grid(row=0,column=0)
No2UpdateTable1 = Label(No2UpdateTableFrame,text= 'Now that the entering and leaving basic variables are known,',font=("Helvetica", 17),background='white')
No2UpdateTable1.grid(row=1,column=0)
No2UpdateTable2 = Label(No2UpdateTableFrame,text= 'we can move to the new and better basic feasible solution.',font=("Helvetica", 17),background='white')
No2UpdateTable2.grid(row=2,column=0)
No2UpdateTable3 = Label(No2UpdateTableFrame,text= 'Step 3.1: Pivot Element',font=("Helvetica", 20, BOLD),background='white')
No2UpdateTable3.grid(row=3,column=0)
No2UpdateTable4 = Label(No2UpdateTableFrame,text= 'The tableau element where the pivot row and the pivot column insteresect',font=("Helvetica", 17),background='white')
No2UpdateTable4.grid(row=4,column=0)
No2UpdateTable5 = Label(No2UpdateTableFrame,text= 'is known as the pivot element (highlighted in blue).',font=("Helvetica", 17),background='white')
No2UpdateTable5.grid(row=5,column=0)
No2UpdateTable6 = Label(No2UpdateTableFrame,text= 'Step 3.2: Update the pivot row',font=("Helvetica", 20, BOLD),background='white')
No2UpdateTable6.grid(row=6,column=0)
No2UpdateTable7 = Label(No2UpdateTableFrame,text= 'We update the pivot row using simple Gaussian operations:',font=("Helvetica", 17),background='white')
No2UpdateTable7.grid(row=7,column=0)
No2UpdateTable8 = Label(No2UpdateTableFrame,background='white')
No2UpdateTable8.config(image=imgUpdateTable1)
No2UpdateTable8.grid(row=8,column=0,columnspan=2)

def click27():
    Question17Button.grid_remove()
    Question17Label.grid(row=11,column=0)
    Test17Answer1.grid(row=12,column=0)
    Test17Answer2.grid(row=13,column=0)
    Test17Answer3.grid(row=14,column=0)
    
    
def Question15Click(value):
    if value == 1:
        Test17Answer1.config(background="firebrick")
        Test17Answer2.config(background="lime green")
        Test17Answer1.config(state=DISABLED)
        Test17Answer2.config(state=DISABLED)
        Test17Answer3.config(state=DISABLED)
        SetRow2Text('0','1','-1/8','3/4','0','0')
        SetRow2Colour('dark orange')
        RHS2.config(text='3/2',fg='dark orange')
        ContinueButton12.grid(row=15,column=0)
        
        
    elif value == 2:
        Test17Answer2.config(background="lime green")
        Test17Answer1.config(state=DISABLED)
        Test17Answer2.config(state=DISABLED)
        Test17Answer3.config(state=DISABLED)
        SetRow2Text('0','1','-1/8','3/4','0','0')
        SetRow2Colour('dark orange')
        RHS2.config(text='3/2',fg='dark orange')
        ContinueButton12.grid(row=15,column=0)
        global Score
        Score = Score + 1
       
        
    elif value == 3:
        Test17Answer3.config(background="firebrick")
        Test17Answer2.config(background="lime green")
        Test17Answer1.config(state=DISABLED)
        Test17Answer2.config(state=DISABLED)
        Test17Answer3.config(state=DISABLED)
        SetRow2Text('0','1','-1/8','3/4','0','0')
        SetRow2Colour('dark orange')
        RHS2.config(text='3/2',fg='dark orange')
        ContinueButton12.grid(row=15,column=0)
        

img1Question17 = PhotoImage(file=".img\\Question17Answer1.png")
img2Question17 = PhotoImage(file=".img\\Question17Answer2C.png")
img3Question17 = PhotoImage(file=".img\\Question17Answer3.png")
    
Question17Button = ttk.Button(No2UpdateTableFrame,text='Question 17',command=lambda: click27())
Question17Button.grid(row=10,column=0)
Question17Label = Label(No2UpdateTableFrame,text='Question 17: Which is the correct updated pivot row? ',font=("Helvetica", 17, BOLD),background='white')

Test17Answer1 = Radiobutton(No2UpdateTableFrame, variable=answerInt, value=1,command=lambda: Question15Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test17Answer1.config(image=img1Question17)

Test17Answer2 = Radiobutton(No2UpdateTableFrame, variable=answerInt, value=2,command=lambda: Question15Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test17Answer2.config(image=img2Question17)

Test17Answer3 = Radiobutton(No2UpdateTableFrame, variable=answerInt, value=3,command=lambda: Question15Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test17Answer3.config(image=img3Question17)

def click28():
    No2UpdateTableFrame.grid_remove()
    No2UpdateTable11.grid(row=3,column=0)
    Question18Button.grid(row=5,column=0)
    No2UpdateTableFrame2.grid(row=0,column=17,rowspan=120,pady=5,padx=20)
    
ContinueButton12 = ttk.Button(No2UpdateTableFrame,text='Continue',command=lambda: click28())
No2UpdateTableFrame2 = LabelFrame(root,background='white',pady=5)
No2UpdateTableTitle2 = Label(No2UpdateTableFrame2,text='Step 3: Update the tableau',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5).grid(row=0,column=0)  
No2UpdateTable9 = Label(No2UpdateTableFrame2,text= 'Step 3.3: Update the remaining rows',font=("Helvetica", 20, BOLD),background='white').grid(row=1,column=0)
No2UpdateTable10 = Label(No2UpdateTableFrame2,text= 'We calculate the Updated j row through the Gaussian operation:',font=("Helvetica", 17),background='white').grid(row=2,column=0)
No2UpdateTable11 = Label(No2UpdateTableFrame2,background='white')   
No2UpdateTable11.config(image=imgUpdateTable3)
No2UpdateTable12 = Label(No2UpdateTableFrame2,text= 'for each of the j remaining rows.',font=("Helvetica", 17),background='white').grid(row=4,column=0)

def click29():
    Question18Button.grid_remove()
    Question18Label.grid(row=5,column=0)
    Question18Help.grid(row=6,column=0)
    Test18Answer1.grid(row=7,column=0)
    Test18Answer2.grid(row=8,column=0)
    Test18Answer3.grid(row=9,column=0)

def Question16Click(value):
    if value == 1:
        Test18Answer1.config(background="lime green")
        Test18Answer1.config(state=DISABLED)
        Test18Answer2.config(state=DISABLED)
        Test18Answer3.config(state=DISABLED)
        SetRow3Text('0','0','3/8','-9/8','1','0')
        SetRow3Colour('dark orange')
        RHS3.config(text='5/2',fg='dark orange')
        ContinueButton13.grid(row=10,column=0)
        No2UpdateTableFrame2.grid(row=0,column=17,rowspan=120,pady=35,padx=10)
        global Score
        Score = Score + 1
        
    elif value == 2:
        Test18Answer2.config(background="firebrick")
        Test18Answer1.config(background="lime green")
        Test18Answer1.config(state=DISABLED)
        Test18Answer2.config(state=DISABLED)
        Test18Answer3.config(state=DISABLED)
        SetRow3Text('0','0','3/8','-9/8','1','0')
        SetRow3Colour('dark orange')
        RHS3.config(text='5/2',fg='dark orange')
        ContinueButton13.grid(row=10,column=0)
        No2UpdateTableFrame2.grid(row=0,column=17,rowspan=120,pady=35,padx=10)
        
    elif value == 3:
        Test18Answer3.config(background="firebrick")
        Test18Answer1.config(background="lime green")
        Test18Answer1.config(state=DISABLED)
        Test18Answer2.config(state=DISABLED)
        Test18Answer3.config(state=DISABLED)
        SetRow3Text('0','0','3/8','-9/8','1','0')
        SetRow3Colour('dark orange')
        RHS3.config(text='5/2',fg='dark orange')
        ContinueButton13.grid(row=10,column=0)
        No2UpdateTableFrame2.grid(row=0,column=17,rowspan=120,pady=35,padx=10)
        
def click30():
    No2UpdateTableFrame2.grid_remove()
    SetRow1Colour('black')
    SetRow2Colour('black')
    SetRow3Colour('black')
    SetRow4Colour('black')
    RHS2.config(fg='black')
    RHS3.config(fg='black')
    SetRow1Text('1', '0', '1/4', '-1/2', '0', '0')
    SetRow4Text('0', '0', '1/8', '-3/4', '0', '1')
    RHS1.config(text='3')
    RHS4.config(text='1/2')
    BaseVariable2.config(text= 'x' + '\u2082',font=("Helvetica", 20),fg='red')
    BaseFunctionCoefficient2.config(text='4',fg='red')
    SetDualPriceText('', '', '', '', '', '')
    SetReducedCostText('', '', '', '', '', '')
    SetRatioTestText('', '', '', '')
    ObjectiveFunctionValue.config(text='')
    No2FinalFormFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=20)
    Question19Button.grid(row=9,column=0)
    
img1Question18 = PhotoImage(file=".img\\Question18Answer1C.png")
img2Question18 = PhotoImage(file=".img\\Question18Answer2.png")
img3Question18 = PhotoImage(file=".img\\Question18Answer3.png")


   
Question18Button = ttk.Button(No2UpdateTableFrame2,text='Question 18',command=lambda: click29())
Question18Label = Label(No2UpdateTableFrame2,text='Question 18: Which is the correct updated pivot row? ',font=("Helvetica", 17, BOLD),background='white')
Question18Help = Label(No2UpdateTableFrame2,text='(pivot element = 4/3) ',font=("Helvetica", 17, BOLD),background='white')
Test18Answer1 = Radiobutton(No2UpdateTableFrame2, variable=answerInt, value=1,command=lambda: Question16Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test18Answer1.config(image=img1Question18)

Test18Answer2 = Radiobutton(No2UpdateTableFrame2, variable=answerInt, value=2,command=lambda: Question16Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test18Answer2.config(image=img2Question18)

Test18Answer3 = Radiobutton(No2UpdateTableFrame2, variable=answerInt, value=3,command=lambda: Question16Click(answerInt.get()),font=("Helvetica", 15),background='white')
Test18Answer3.config(image=img3Question18)

imgFinalForm2 = PhotoImage(file=".img\\Final Form 2.png")

ContinueButton13 = ttk.Button(No2UpdateTableFrame2,text='Continue',command=lambda: click30())
No2FinalFormFrame = LabelFrame(root,background='white',padx=5,pady=5)
No2FinalForm1 = Label(No2FinalFormFrame,text='Step 3.4: Final Form of the tableau',font=("Helvetica", 25, BOLD),background='white',pady=5).grid(row=0,column=0)
No2FinalForm2 = Label(No2FinalFormFrame,text='We need to update the basic variables with the entering variable',font=("Helvetica", 15),background='white').grid(row=1,column=0)
No2FinalForm3 = Label(No2FinalFormFrame,text='as well as the objective function coefficients of the basic variables.',font=("Helvetica", 15),background='white').grid(row=2,column=0)
No2FinalForm4 = Label(No2FinalFormFrame,text='Entering variable x2 and its coefficient is highlighted in red.',font=("Helvetica", 15),background='white').grid(row=3,column=0)
No2FinalForm5 = Label(No2FinalFormFrame,text='The objective function value in the second iteration of the simplex algorithm',font=("Helvetica", 15),background='white').grid(row=4,column=0)
No2FinalForm6 = Label(No2FinalFormFrame,text='is calculated using the following equation:',font=("Helvetica", 15),background='white').grid(row=5,column=0)
No2FinalForm7 = Label(No2FinalFormFrame,background='white')
No2FinalForm7.config(image=imgFinalForm2)
No2FinalForm7.grid(row=6,column=0)
No2FinalForm8 = Label(No2FinalFormFrame,text='We also delete the Shadow prices, Reduced Costs and the Ratio Test values',font=("Helvetica", 15),background='white').grid(row=7,column=0)
No2FinalForm9 = Label(No2FinalFormFrame,text='since we need to calculate them once again in the next step.',font=("Helvetica", 15),background='white').grid(row=8,column=0)

def click31():
    Question19Button.grid_remove()
    Question19Label.grid(row=9,column=0)
    Question19Entry.grid(row=10,column=0)
    Question19Answer.grid(row=11,column=0)

def callback9():
    if Question19Entry.get() == '21':
        Question19Entry.delete(0, END)
        Question19Entry.insert(0, "Correct")
        Question19Entry.configure(state=DISABLED)
        ObjectiveFunctionValue.config(text='21',fg='dark orange')
        Question19Answer.grid_remove()
        ContinueButton14.grid(row=11,column=0)
        global Score 
        Score = Score + 1
    else:
        Question19Entry.delete(0, END)
        Question19Entry.insert(0, "False. Answer highlighted in the tableau.")
        Question19Entry.configure(state=DISABLED)
        ObjectiveFunctionValue.config(text='21',fg='dark orange')
        Question19Answer.grid_remove()
        ContinueButton14.grid(row=11,column=0)

def click32():
    ContinueButton14.grid_remove()
    No2FinalFormFrame.grid_remove()
    ObjectiveFunctionValue.config(fg='black')
    BaseVariable2.config(fg='black')
    BaseFunctionCoefficient2.config(fg='black')
    No2StopCondiFrame.grid(row=0,column=17,rowspan=120,pady=5,padx=15)
    Question20Button.grid(row=5,column=0)
    SetDualPriceColour('dark orange')
    SetDualPriceText('5', '4', '3/4', '1/2', '0', '0')
    SetDualPriceFontSize(20)
    SetReducedCostColour('dark orange')
    SetReducedCostText('0', '0', '-3/4', '-1/2', '0', '0')
    SetReducedCostFontSize(20)    
        
Question19Button = ttk.Button(No2FinalFormFrame,text='Question 19',command=lambda: click31())
Question19Label = Label(No2FinalFormFrame,text='Question 19: Which is the objective function value at this point? ',font=("Helvetica", 15, BOLD),background='white',pady=5)
Question19Entry = Entry(No2FinalFormFrame, justify = CENTER,width = 55,font=("Helvetica", 12, ITALIC),background='white')
Question19Entry.insert(0, "Format your answer as an integer (e.g. 30).")
Question19Answer = ttk.Button(No2FinalFormFrame,text='Enter',command= lambda : callback9())
Question19Entry.focus_set()
ContinueButton14 = ttk.Button(No2FinalFormFrame,text='Continue',command=lambda: click32())

No2StopCondiFrame = LabelFrame(root,padx=5,pady=5,background='white')
No2StopCondi1 = Label(No2StopCondiFrame,text='Step 4: Check the stop condition.',font=("Helvetica", 25, BOLD),background='white',pady=5,padx=5).grid(row=0,column=0)
No2StopCondi2 = Label(No2StopCondiFrame,text='In this final step for the first iteration,',font=("Helvetica", 15),background='white').grid(row=1,column=0)
No2StopCondi3 = Label(No2StopCondiFrame,text='we have to calculate the Dual prices and the Reduced Costs',font=("Helvetica", 15),background='white').grid(row=2,column=0)
No2StopCondi4 = Label(No2StopCondiFrame,text='for the now updated tableau and check the stop condition.',font=("Helvetica", 15),background='white').grid(row=3,column=0)
No2StopCondi5 = Label(No2StopCondiFrame,text='the stop condition is met when all the Reduced cost values are negative or zero.',font=("Helvetica", 15),background='white').grid(row=4,column=0)

def click33():
    Question20Button.grid_remove()
    Question20Label1.grid(row=5,column=0)
    Question20Label2.grid(row=6,column=0)
    Test20Answer1.grid(row=7,column=0)
    Test20Answer2.grid(row=8,column=0)
    
def Question20Click(value):
    global Score
    if value == True:
        Test20Answer1.config(background="lime green")
        Test20Answer1.config(state=DISABLED)
        Test20Answer2.config(state=DISABLED)
        Question20Explanation1.grid(row=9,column=0)
        Question20Explanation2.grid(row=10,column=0)
        Score = Score + 1
        ScoreLabel1 = Label(No2StopCondiFrame,text= 'Your Score: ' + str(Score) + '/20',font=("Helvetica", 15, BOLD),background='white')
        ScoreLabel2 = Label(No2StopCondiFrame,text= 'You can watch a geometrical presentation for the Primal Simplex Algorithm.',font=("Helvetica", 15, BOLD),background='white')
        ScoreLabel1.grid(row=11,column=0)
        ScoreLabel2.grid(row=12,column=0)
        ContinueButton16.grid(row=13,column=0)
        
    else:
        Test20Answer2.config(background="firebrick")
        Test20Answer1.config(state=DISABLED)
        Test20Answer2.config(state=DISABLED)
        Question20Explanation1.grid(row=9,column=0)
        Question20Explanation2.grid(row=10,column=0)
        ScoreLabel1 = Label(No2StopCondiFrame,text= 'Your Score: ' + str(Score) + '/20',font=("Helvetica", 15, BOLD),background='white')
        ScoreLabel2 = Label(No2StopCondiFrame,text= 'You can watch a geometrical presentation for the Primal Simplex Algorithm.',font=("Helvetica", 15, BOLD),background='white')
        ScoreLabel3 = Label(No2StopCondiFrame,text= 'Pressing the "Youtube" Button will open the video in your default browser and close the application.' ,font=("Helvetica", 11, BOLD),background='white')
        ScoreLabel1.grid(row=11,column=0)
        ScoreLabel2.grid(row=12,column=0)
        ScoreLabel3.grid(row=13,column=0)
        ContinueButton16.grid(row=14,column=0)


    
def click35():
    TableauFrame.grid_remove()
    No2StopCondiFrame.grid_remove()
    url = "https://youtu.be/mHgv6kKOl6g"
    webbrowser.open(url,new=1)
    root.destroy()
        
Question20Button = ttk.Button(No2StopCondiFrame,text='Question 20',command= lambda : click33())
Question20Label1 = Label(No2StopCondiFrame,text= 'Question 20:',font=("Helvetica", 15, BOLD),background='white')
Question20Label2 = Label(No2StopCondiFrame,text= 'The stop condition of the simplex algorithm is met.',font=("Helvetica", 15, BOLD),background='white')
Test20Answer1 = Radiobutton(No2StopCondiFrame, text='True', variable=answer, value=True,command=lambda: Question20Click(answer.get()),font=("Helvetica", 15),background='white')
Test20Answer2 = Radiobutton(No2StopCondiFrame, text='False', variable=answer, value=False,command=lambda: Question20Click(answer.get()),font=("Helvetica", 15),background='white')
Question20Explanation1 = Label(No2StopCondiFrame,text = 'The stop condition for the simplex algorithm',font=("Helvetica", 15),background='white')
Question20Explanation2 = Label(No2StopCondiFrame,text = 'is met when all Reduced Costs are non-positive (max problem).',font=("Helvetica", 15),background='white')
ContinueButton16 = ttk.Button(No2StopCondiFrame,text='Youtube',command=lambda: click35())



    
root.mainloop()

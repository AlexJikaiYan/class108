import random 
import plotly.figure_factory as pff
import plotly_express as px
count=[]
diceresult=[]
for i in range(0,100):
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
figure=px.bar(x=diceresult,y=count)
figure=pff.create_distplot([diceresult],["result"],show_hist= False)
figure.show()


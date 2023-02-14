import pandas as pd 
from matplotlib import pyplot as plt 
import numpy as np 
import calendar 

def generate(file):
    df = pd.read_excel(file, index_col=0) 
    df.groupby(by=["Department"]).count()['Name'].plot.bar(xlabel='Department',ylabel='Number of students', title='Branchwise Offers made in 2021')
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('Branchwise Offers made in 2021', dpi=100, format='png')
    plt.close()

    df.groupby(by=["Company Name"]).count()['Name'].sort_values(ascending=False).head(7).plot.bar(xlabel='Company',ylabel='Number of students', title='Branchwise Company')
    fig = plt.gcf()
    fig.set_size_inches(20, 13)
    fig.savefig('Branchwise Company', dpi=100)
    plt.close()

    df.groupby(by=['Category']).count()['Name'].plot.pie(autopct='%1.1f%%',title="Dream vs Open Dream") 
    fig = plt.gcf()
    fig.set_size_inches(9.5, 6.5)
    fig.savefig('Dream vs Open Dream', dpi=100)
    plt.close()

    df.groupby(by=["Job Profile"]).count()['Name'].sort_values(ascending=False).head(7).plot.pie(autopct='%1.1f%%',title='Job Profile Distribution') 
    fig = plt.gcf()
    fig.set_size_inches(9.5, 6.5)
    fig.savefig('Job Profile Distribution', dpi=100)
    plt.close()

    df.groupby(by=pd.cut(df["CTC"], np.arange(0, 40, 5))).count()['Name'].plot.bar(xlabel='CTC',ylabel='Number of students', title='CTC vs No of Students')
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig('CTC vs No of Students', dpi=100)
    plt.close()

    df.groupby(by=['Gender']).count()['Name'].plot.pie(autopct='%1.1f%%',title='Male Female Distribution') 
    fig = plt.gcf()
    fig.set_size_inches(9.5, 6.5)
    fig.savefig('Male Female Distribution', dpi=100)
    plt.close()

    df.groupby(by=['Type']).count()['Name'].plot.pie(autopct='%1.1f%%',title='Intership and Full time distribution') 
    fig = plt.gcf()
    fig.set_size_inches(9.5, 6.5)
    fig.savefig('Intership and Full time distribution', dpi=100)
    plt.close()






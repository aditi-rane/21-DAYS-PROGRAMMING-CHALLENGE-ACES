from matplotlib import pyplot as plt
from matplotlib import style

x=[1,2,3]
y=[4,5,1]
plt.plot(x,y)
plt.title("Information")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
#--------------------------------------------------------

x=[5,8,10]
y=[12,16,6]
x1=[6,9,11]
y1=[6,15,7]
style.use('ggplot')
plt.plot(x,y,color='g',label='line one',linewidth=4)
plt.plot(x1,y1,color='r',label='line two',linewidth=4)
plt.title('Epic Information')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
#--------------------------------------------------------

#Bar Graph
x1=[0.25,1.25,2.25,3.25,4.25]
y1=[50,40,70,80,20]
x2=[0.75,1.75,2.75,3.75,4.75]
y2=[80,20,20,50,60]
plt.bar(x1,y1,label="BMW",color='c',width=0.5)
plt.bar(x2,y2,label="Audi",color='r',width=0.5)
plt.xlabel('Days')
plt.ylabel('Distance (kms)')
plt.title('Information')
plt.legend()
plt.show()
#------------------------------------------------------

#Pie chart
days=[1, 2, 3, 4, 5]
sleeping=[7, 8, 6, 11, 7]
eating=[2, 3, 4, 3, 2]
working=[7, 8, 7, 2, 2]
playing=[8, 5, 7, 8, 13]
slices=[7, 2, 2, 13]
activities=['sleeping', 'eating', 'working', 'playing']
cols=['b', 'r', 'm', 'c']
plt.pie(slices,labels=activities,colors=cols,startangle=90,shadow=True,explode=(0, 0.1, 0, 0),
        autopct='%1.1f%%')
plt.title('Pie Plot')
plt.legend()
plt.show()

#------------------------------------------------------

#Histogram
age=[22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(age,bins,histtype='bar',rwidth=0.8,color='c')
plt.xlabel('Age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()

#--------------------------------------------------------

#Scatter plot
x1=[1, 1.5, 2, 2.5, 3, 3.5, 3.6]
y1=[7.5, 8, 8.5, 9, 9.5, 10, 10.5]
x2=[8, 8.5, 9, 9.5, 10, 10.5, 11]
y2=[3, 3.5, 3.7, 4, 4.5, 5, 5.2]
plt.scatter(x1,y1,label='High income low saving', color='r')
plt.scatter(x2,y2,label='Low income high savings', color='b')
plt.xlabel('saving*100')
plt.ylabel('income*1000')
plt.title('Scatter Plot')
plt.legend()
plt.show()

#---------------------------------------------------------

#Area plot
days=[1, 2, 3, 4, 5]
sleeping=[7, 8, 6, 11, 7]
eating=[2, 3, 4, 3, 2]
working=[7, 8, 7, 2, 2]
playing=[8, 5, 7, 8, 13]
plt.plot([], [], color='m', label='Sleeping', linewidth=5)
plt.plot([], [], color='c', label='Eating', linewidth=5)
plt.plot([], [], color='r', label='Working', linewidth=5)
plt.plot([], [], color='k', label='Playing', linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=['k', 'r', 'c', 'm'])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Stack Plot')
plt.legend()
plt.show()
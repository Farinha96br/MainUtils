import matplotlib.pyplot as plt

plt.rcParams.update({
    'font.size': 12,
    'axes.grid': False,
    'font.family': 'serif',
    'mathtext.fontset': 'cm'
})

# sample on ploting a pie chart
labels = ['A', 'B', 'C', 'D']
values = [35, 25, 22, 18]
explode = (0.05, 0, 0, 0)  # pull the first slice out

fig, ax = plt.subplots()
ax.pie(values, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90,
       colors=['steelblue', 'indianred', 'darkseagreen', 'goldenrod'])
# for a donut instead, drop explode and add: wedgeprops=dict(width=0.4)

ax.axis('equal')  # keeps it circular
ax.set_title('Pie chart')
plt.show()
plt.close()

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('/Users/Myra/Documents/School/physics1lab/archimedesdata.csv')
data.set_index("measurement", inplace=True)

volume = (((data.loc['cylinder','length']/2)**2*np.pi)*data.iloc[1:5, 0])

u_volume = volume*np.sqrt(
    (2*data.loc['cylinder','u_length']/data.loc['cylinder','length'])**2 +
    (data.iloc[1:5,1]/data.iloc[1:5,0])**2
)

y= data.iloc[1:5,2]
x= volume
dy = data.iloc[1:5,3]
dx = u_volume

regression = np.polyfit(x, y, deg=1)

m = regression[0]
b = regression[1]

#function for error in regression
def Delta(x, dy):
    D = (sum(1/dy**2))*(sum(x**2/dy**2))-(sum(x/dy**2))**2
    return D

D=Delta(x, dy)

#error in slope and intercept
dm = np.sqrt(1/D*sum(1/dy**2))
db = np.sqrt(1/D*sum(x**2/dy**2))

fig, ax = plt.subplots()
ax.scatter(x,y)
ax.plot(x, (m*x+b))
ax.set_title("Fig 1: The apparent mass of an object decreases\n as it is increasingly submerged in a fluid ")
ax.set_xlabel("Volume of Object Submerged [m^3]")
ax.set_ylabel("Apparent Mass[kg]")
ax.annotate("Slope: {:.2f} \nIntercept: {:.2f} \nUncertainty in Slope: {:.2f} \nUncertainty in Intercept: {:.4f}".format(m, b, dm, db), (1.0e-5,0.085))
ax.errorbar(x,y, yerr=None, xerr=dx, ls='none')
plt.show()
breakpoint()
#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#load data
data = pd.read_csv('/Users/Myra/Documents/School/physics1lab/uniformMotionData.csv', delimiter=',')
data.set_index('variable', inplace=True)

#constants and important independent variables
g = 9.81
radiusLength = data.loc['radius1':'radius5','length']

#centripetal force == hex weight == tension force in string
#no error in g
centripetalForce = (data.loc['hex','mass']*g)
u_centripetalForce = centripetalForce*np.sqrt(
    (data.loc['hex','u_mass']/data.loc['hex','mass'])**2
)

#periods, theoretical
periodTheoretical = 2*np.pi*np.sqrt(
    data.loc['cylinder','mass']*data.loc['radius1':'radius5', 'length']/centripetalForce #massCylinder*radius/cForce
)
u_periodTheoretical = periodTheoretical*np.sqrt(
    (0.5*data.loc['cylinder','u_mass']/data.loc['cylinder','mass'])**2 + #u_massCyl/massCyl
    (0.5*data.loc['radius1':'radius5', 'u_length']/data.loc['radius1':'radius5', 'length'])**2 +  #u_radius/radius
    (-0.5*u_centripetalForce/centripetalForce)**2 #uncertainty/centripetal force
)

#periods, experimental (deltaQ=cdeltaA)
meanPeriod = (data.loc['radius1':'radius5','trial1':'trial5'].mean(axis=1)*0.2)
u_meanPeriod = (0.2)*(data.loc['radius1':'radius5', 'trial1':'trial5'].std(axis=1)/np.sqrt(5))

#regression
c, errorReg = np.polyfit(np.sqrt(radiusLength), meanPeriod, 1, cov=True)
errorReg = np.sqrt(np.diag(errorReg))
b = c[1]
u_b = errorReg[1]
m = c[0]
u_m = errorReg[0]
exp_centForce = (4*np.pi**2*data.loc['cylinder','mass'])/m**2
u_exp_centForce = exp_centForce*np.sqrt((data.loc['cylinder','u_mass']/data.loc['cylinder','mass'])**2 + float(-2*u_m/m)**2)

c1, errorReg1 = np.polyfit(radiusLength, meanPeriod**2, 1, cov=True)
errorReg1 = np.sqrt(np.diag(errorReg1))
b1 = c1[1]
u_b1 = errorReg1[1]
m1 = c1[0]
u_m1 = errorReg1[0]
exp_centForce1 = (4*np.pi**2*data.loc['cylinder','mass'])/m1
u_exp_centForce1 = exp_centForce1*np.sqrt(((data.loc['cylinder','u_mass']/data.loc['cylinder','mass'])**2 + (-1*u_m1/m1)**2))


#plotting
fig, (ax1, ax2) = plt.subplots(1,2)
ax1.plot(np.linspace(0.05,0.3,100), np.sqrt(np.linspace(0.05,0.3,100))*m + b)
ax1.scatter(radiusLength, meanPeriod)
ax1.set_title("Fig 1: The period of a rotating mass at constant centrifical \nacceleration is sub-linearly proportional to the \nradius at which "
             "it is rotated")
ax1.set_xlabel("Radius[m]")
ax1.set_ylabel("Period[s]")
#by the way i'm sure there's a better way to express the error of the slope in terms of sqrt(x) but oh well
ax1.annotate("Slope: {:.2f}/\u221Ax +/- {:.2f}/\u221Ax [s/m] \nIntercept: {:.2f} +/- {:.2f} m [s]".format(
    m/2, 0.5*u_m, b, u_b), (0.04,1.5))
ax1.errorbar(radiusLength, meanPeriod, yerr=u_meanPeriod, xerr=None, ls='none')
ax2.scatter(radiusLength, meanPeriod**2)
ax2.plot(radiusLength, m1*radiusLength + b1)
ax2.set_title("Fig 2: The squared period of a rotating mass at constant centrifical acceleration is\n "
              "linearly proportional to the radius at which it is rotated")
ax2.set_xlabel("Radius[m]")
ax2.set_ylabel("Period Squared[s^2]")
ax2.annotate("Slope: {:.2f} +/- {:.2f} [s^2/m] \nIntercept: {:.2f} +/- {:.2f} m [s^2]".format(
    m1, u_m1, b1, u_b1), (0.1,2.2))
plt.show()
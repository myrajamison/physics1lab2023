#import packages
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import data from local directories
data = pd.read_csv('/home/myra/Documents/schoolf2023/physics1lab/data/spinnyboidata.csv')
data.set_index("measurement", inplace=True)

#theoretical value for the moment of inertia
diskMass = data.loc["diskMass", "mass[kg]"]
diskRadius = data.loc["diskDiameter", "length[m]"]*0.5
theo_momentOfInertia = 0.5*diskMass*(diskRadius**2)
u_theo_momentOfInertia = theo_momentOfInertia*np.sqrt(
    (data.loc["diskMass", "u_mass[kg]"]/data.loc["diskMass", "mass[kg]"])**2 +
    (2*(data.loc["diskDiameter", "u_length[m]"]/data.loc["diskDiameter", "length[m]"]))**2
)

#calculating mean linear acceleration measured values
meanAcceleration = data.loc["20g":"120g", "trial1[a]":"trial6[a]"].mean(axis=1)
u_meanAcceleration = data.loc["20g":"120g", "trial1[a]":"trial6[a]"].std(axis=1)/np.sqrt(6)

#calculating torque
g = 9.81
acceleratingMass = data.loc["20g":"120g", "massOnString[kg]"]-data.loc["paperclipsMass", "mass[kg]"]
u_acceleratingMass = np.sqrt((data.loc["paperclipsMass", "u_mass[kg]"]/data.loc["paperclipsMass", "mass[kg]"])**2 +
                             (data.loc["20g":"120g", "u_massOnString[kg]"]/data.loc["20g":"120g", "massOnString[kg]"])**2)
meanStringTension = acceleratingMass*(g-meanAcceleration)
u_meanStringTension = np.sqrt(
    (meanStringTension-((acceleratingMass+u_acceleratingMass)*(g-meanAcceleration)))**2
    + (meanStringTension-(acceleratingMass*(g-(meanAcceleration+u_meanAcceleration))))**2
)
meanTorque = (data.loc["cylinderDiameter", "length[m]"]*0.5)*meanStringTension*np.sin(np.pi/2)
u_meanTorque = meanTorque*np.sqrt(
    (data.loc["cylinderDiameter", "u_length[m]"]/data.loc["cylinderDiameter", "length[m]"])**2 +
    (u_meanStringTension/meanStringTension)**2
)


#alternative method of calculating uncertainty in torque
# gminusa = (g-data.loc["20g":"120g", "trial1[a]":"trial6[a]"]).mean(axis=1)
# u_gminusa = ((g-data.loc["20g":"120g", "trial1[a]":"trial6[a]"]).std(axis=1))/np.sqrt(6)
#
# u2_meanTorque = meanTorque * np.sqrt((data.loc["cylinderDiameter", "u_length[m]"]/data.loc["cylinderDiameter", "length[m]"])**2 + (u_gminusa/gminusa)**2 + (u_acceleratingMass/acceleratingMass)**2
#                                      )

#calculating angular acceleration
meanAngularAcceleration = meanAcceleration/(data.loc["cylinderDiameter", "length[m]"]*0.5)
u_meanAngularAcceleration = meanAngularAcceleration*np.sqrt(
    (u_meanAcceleration/meanAcceleration)**2 +
    (-1*data.loc["cylinderDiameter", "u_length[m]"]/data.loc["cylinderDiameter", "length[m]"])**2
)

#calculating regression and slope
m , b = np.polyfit(meanAngularAcceleration, meanTorque, 1)
u_m = np.sqrt(1/(sum(1/(u_meanTorque**2))*(sum(meanAngularAcceleration**2/u_meanTorque**2))-(sum(meanAngularAcceleration/u_meanTorque**2))**2)
             *sum(1/u_meanTorque**2))
u_b = np.sqrt(1/(sum(1/(u_meanTorque**2))*(sum(meanAngularAcceleration**2/u_meanTorque**2))-(sum(meanAngularAcceleration/u_meanTorque**2))**2)
             *sum(meanAngularAcceleration**2/u_meanTorque**2))

#plotting
fig, ax = plt.subplots()
ax.scatter(meanAngularAcceleration, meanTorque)
ax.plot(meanAngularAcceleration, meanAngularAcceleration*m + b, color="black", linestyle="--", label="Modeled Linear Regression of the \n"
                                                                                                     "Relationship"
                                                                                                     " between Torque and \nAngular Acceleration,"
                                                                                                     "with Error Bars")
ax.legend(loc='center left', bbox_to_anchor=(0.8, 0.5))
ax.set_ylabel("Torque[N*m]")
ax.set_xlabel("Angular Acceleration [m/s^2]")
ax.annotate("Slope = {}+/-{} [kg*m]".format(("%.4f" % m), ("%.4f" % u_m)), (0.3, 0.0175))
ax.set_title("As the angular acceleration of the cylinder holding the disk increases,\n "
             "so does the torque applied to the cylinder. The ratio (slope) of these two\n "
             "items provide us with the moment of inertia of the disk")
ax.errorbar(meanAngularAcceleration, meanTorque, yerr=u_meanTorque, xerr=u_meanAngularAcceleration, ls='none')
plt.show()

breakpoint()
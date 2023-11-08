# For each collision, you will need to calculate the following:
# 1. Total initial momentum
# 2. Final momentum for cart 𝑚1, with uncertainty
# 3. Final momentum for cart 𝑚2, with uncertainty
# 4. Total final momentum, with uncertainty
# 5. Total initial KE
# 6. Final KE for cart 𝑚1, with uncertainty
# 7. Final KE for cart 𝑚2, with uncertainty
# 8. Total final KE, with uncertainty

#things to still do on Wednesday
# 1. calculate uncertainty
# 2. figure out significant figures

#'remember, KE is only conserved in *Elastic* collisions

#'[Load Data and Set Directories]

setwd('/Users/Myra/Documents/School/physics1lab')
cardataraw <- data.frame(read.csv('linearcollisionsdata.csv'))

#'[Uncertainty]
fractionaluncertaintyvelocity <- sum(c((abs(cardataraw$initialvelocity1.m.s.[5:13]-cardataraw$finalvelocity1.m.s.[5:13]))/cardataraw$initialvelocity1.m.s.[5:13]))/9
finalmomentum1uncertainty <- abs(finalmomentum1[1:4])*sqrt(((fractionaluncertaintyvelocity*cardataraw$finalvelocity1.m.s.[1:4])
                                                        /cardataraw$finalvelocity1.m.s.[1:4])^2+((0.1)/cardataraw$mass1.g.[1:4])^2)
finalmomentum2uncertainty <- abs(finalmomentum2[1:4])*sqrt(((fractionaluncertaintyvelocity*cardataraw$finalvelocity2.m.s.[1:4])
                                                             /cardataraw$finalvelocity2.m.s.[1:4])^2+((0.1)/cardataraw$mass2.g.[1:4])^2)
totalmomentumfinaluncertainty <- sqrt(finalmomentum1uncertainty^2 + finalmomentum2uncertainty^2)
finalKE1uncertainty <- abs(finalKE1)*sqrt((0.1/cardataraw$mass1.g.[1:4])^2 + (2*(fractionaluncertaintyvelocity*cardataraw$finalvelocity1.m.s.[1:4])
                                                                              /cardataraw$finalvelocity1.m.s.[1:4])^2)   
finalKE2uncertainty <- abs(finalKE2)*sqrt((0.1/cardataraw$mass2.g.[1:4])^2 + (2*(fractionaluncertaintyvelocity*cardataraw$finalvelocity2.m.s.[1:4])
                                                                              /cardataraw$finalvelocity2.m.s.[1:4])^2)
totalfinalKEuncertainty <- sqrt(finalKE1uncertainty^2 + finalKE2uncertainty^2)

#'[Initial Momentum]
initialmomentum1 <- (cardataraw$mass1.g.[1:4]/1000)*cardataraw$initialvelocity1.m.s.[1:4]
initialmomentum2 <- (cardataraw$mass2.g.[1:4]/1000)*cardataraw$initialvelocity2.m.s[1:4]
totalmomentuminitial <- c(initialmomentum1+initialmomentum2)

#'[Final Momentum]
finalmomentum1 <- (cardataraw$mass1.g.[1:4]/1000)*cardataraw$finalvelocity1.m.s.[1:4]
finalmomentum2 <- (cardataraw$mass2.g.[1:4]/1000)*cardataraw$finalvelocity2.m.s[1:4]
totalmomentumfinal <- c(finalmomentum1+finalmomentum2)

#'[Initial Kinetic Energy]
totalinitialKE <- c((0.5*(cardataraw$mass1.g.[1:4]/1000)*(cardataraw$initialvelocity1.m.s.[1:4]^2))+(0.5*(cardataraw$mass2.g.[1:4]/1000)
  *(cardataraw$initialvelocity2.m.s.[1:4]^2)))

#'[Final Kinetic Energy]
finalKE1 <- c(0.5*(cardataraw$mass1.g.[1:4]/1000)*(cardataraw$finalvelocity1.m.s.[1:4]^2))
finalKE2 <- c(0.5*(cardataraw$mass2.g.[1:4]/1000)*(cardataraw$finalvelocity2.m.s.[1:4]^2))
totalfinalKE <- c((0.5*(cardataraw$mass1.g.[1:4]/1000)*(cardataraw$finalvelocity1.m.s.[1:4]^2))+(0.5*(cardataraw$mass2.g.[1:4]/1000)
  *(cardataraw$finalvelocity2.m.s.[1:4]^2)))

#'[Description of Trial]
descriptionoftrial <- c("Elastic collision with stationary target where masses are equal", 
                        "Elastic collision with stationary target where mass 2 > mass 1",
                        "Elastic collision with moving target where masses are equal",
                        "Inelastic collision with stationary target where masses are equal")

#'[Creating Matrix]
matrix1 <- matrix(c(initialmomentum1,initialmomentum2,totalmomentuminitial,finalmomentum1,finalmomentum2,totalmomentumfinal,
                    totalinitialKE,finalKE1,finalKE2,totalfinalKE,descriptionoftrial), ncol=11)
rownames(matrix1) <- c("Trial 1", "Trial 2", "Trial 3", "Trial 4")
colnames(matrix1) <- c("Initial Momentum (car 1, red) [kg*m/s]", "Initial Momentum (car 2, blue) [kg*m/s]", 
                       "Total Initial Momentum [kmg*m/s]", "Final Momentum (car 1, red) [kg*m/s]", 
                       "Final Momentum (car 2, blue)[kg*m/s]", "Total Final Momentum [kg*m/s]", "Total Initial KE",
                       "Final KE (car 1, red) [kg*m^2/s^2, or J]", "Final KE (car 2, blue) [kg*m^2/s^2, or J]", 
                       "Total Final KE [kg*m^2/s^2, or J]", "Description of Trial")
matrixu <- matrix(c(finalmomentum1uncertainty,finalmomentum2uncertainty,totalmomentumfinaluncertainty,finalKE1uncertainty,
                    finalKE2uncertainty,totalfinalKEuncertainty), ncol=6)
rownames(matrixu) <- c("Trial 1", "Trial 2", "Trial 3", "Trial 4")
colnames(matrixu) <- c( "Uncertainty in Final Momentum (car 1, red)","Uncertainty in Final Momentum (car 2, blue)",
                       "Uncertainty in Final Total Momentum", "Uncertainty in Final KE (car 1, red)", "Uncertainty in Final KE (car 2, blue)",
                       "Uncertainty in Total Final KE")





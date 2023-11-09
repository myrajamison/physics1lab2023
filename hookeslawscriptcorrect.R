#'[Set Directories and Load Packages]
library(ggplot2)
setwd('/Users/Myra/Documents/School/physics1lab')
hookesdata <- data.frame(read.csv('hookeslawlabcorrected.csv'))

#'[Calculating K using linear regression]
brassregenforce <- c(hookesdata$totalmass.kg.[4:12]*9.8)
brassposition <- c(hookesdata$position.m.[4:12]-0.493)
brassregression <- lm(brassregenforce ~ brassposition)
brassk1 <- summary(brassregression)$coefficients[2,1]

steelregenforce <- c(hookesdata$totalmass.kg.[13:21]*9.8)
steelposition <- c(hookesdata$position.m.[13:21]-0.464)
steelregression <- lm(steelregenforce ~ steelposition)
steelk1 <- summary(steelregression)$coefficients[2,1]

#'[Calculating K using oscillation equation]
meanbrasstime <- mean(hookesdata$time.s.[22:31])
periodbrass <- meanbrasstime/10
totalmassbrass <- hookesdata$totalmass.kg.[1]*(1/3) + hookesdata$totalmass.kg.[3]
brassk2 <- totalmassbrass/((periodbrass/(2*pi))^2)

meansteeltime <- mean(hookesdata$time.s.[32:41])
periodsteel <- meansteeltime/10
totalmasssteel <- hookesdata$totalmass.kg.[2]*(1/3) + hookesdata$totalmass.kg.[3] + 1
steelk2 <- totalmasssteel/((periodsteel/(2*pi))^2)

#'[Uncertainties]
#additive error propogation, from error measurement final - error measurement initial
uncertainty_brassposition <- c(sqrt(0.001^2 + 0.001^2))
#additive error propogation, from kg of hangar measured error + kg error of weights
uncertainty_brassregenforce <-c(sqrt(0.0001^2 + 0.0001^2))
uncertainty_brassk1 <- summary(brassregression)$coefficients[2,2]
uncertainty_stdevmeanbrasstime <- sd(hookesdata$time.[22:31])/sqrt(10)
#power product rule, but with only one object since n=10 is an exact counted number
uncertainty_periodbrass <- periodbrass*sqrt((uncertainty_stdevmeanbrasstime/meanbrasstime)^2)
#additive error prop from mass of spring and hanger
uncertainty_totalmassbrass <- sqrt(0.0001^2 + 0.0001^2)
uncertainty_brassk2 <- brassk2*sqrt((uncertainty_totalmassbrass/totalmassbrass)^2
                                    +(-1*(uncertainty_periodbrass/periodbrass))^2)

#additive error propogation, from error measurement final - error measurement initial
uncertainty_steelposition <- c(sqrt(0.001^2 + 0.001^2))
#additive error propogation, from kg of hangar measured error + kg error of weights
uncertainty_steelregenforce <-c(sqrt(0.0001^2 + 0.0001^2))
uncertainty_steelk1 <- summary(steelregression)$coefficients[2,2]
uncertainty_stdevmeansteeltime <- sd(hookesdata$time.[22:31])/sqrt(10)
#power product rule, but with only one object since n=10 is an exact counted number
uncertainty_periodsteel <- periodsteel*sqrt((uncertainty_stdevmeansteeltime/meansteeltime)^2)
#additive error prop from mass of spring and hanger (or spring and hangar and kg weight in steel)
uncertainty_totalmasssteel <- sqrt(0.0001^2 + 0.0001^2 + 0.0001^2)
uncertainty_steelk2 <- steelk2*sqrt((uncertainty_totalmasssteel/totalmasssteel)^2
                                    +(-1*(uncertainty_periodsteel/periodsteel))^2)

#'[Graphing Results]
hookesdataframe <- data.frame(brassposition,brassregenforce, steelposition, steelregenforce)

p <- ggplot(hookesdataframe)+
        geom_point(aes(x=brassposition,y=brassregenforce, color="blue"))+
        geom_point(aes(x=steelposition, y=steelregenforce, color="red"))+
        geom_smooth(method="lm", aes(x=brassposition,y=brassregenforce,color="blue"))+
        geom_smooth(method="lm", aes(x=steelposition, y=steelregenforce, color="red"))+
        labs(title="Spring Regenerative Force by Distance from Equilibrium, with Linear Regressions", 
             x="Distance from Equilibrium Position[m]", 
             y="Regenerative Force from Spring[N]", color="Spring Type")+
        scale_color_hue(labels=c("Brass","Steel"))
print(p)





      

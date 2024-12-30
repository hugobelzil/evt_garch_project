# Getting the data and necessary libraries

if (!require(rugarch)){
  install.packages("rugarch")
}

if (!require(qrmtools)){
  install.packages("qrmtools")
}

if (!require(ismev)){
  install.packages("ismev")
}

library(rugarch) #model fitting
library(qrmtools) 
library(ismev) #dow jones data

#extracting the data (from ismev package)
data(dowjones)
log_returns_DJ <- 100*returns(dowjones$Index,method="logarithmic")


# EDA on Dow Jones data

# plotting the (scaled) log-returns 
plot(as.Date(dowjones$Date[-1]),log_returns_DJ,type='l', main="Scaled Log Returns of Dow Jones",col='blue',lwd=1.3,xlab="Time",ylab="Scaled log-returns",cex.main=1.5,cex.lab=1.2,cex.axis=1.1)
grid(col='gray',lty='dotted')

#histograms of the (log-returns)
hist(log_returns_DJ, main = "Distribution of the scaled log-returns of the Dow Jones",breaks=40,col='skyblue',border='white',xlab="Log returns",cex.main=1.5,cex.lab=1.2,cex.axis=1.1,freq=FALSE)
length(log_returns_DJ)
rug(log_returns_DJ,col='red') #highlights the extremes (in red, on top of x-axis)
box()

# Fitting the GARCH(1,1) model with Gaussian innovations


#the rugarch packages requires the initialization of a class rugarch object that speficifes the parameters of the model to be fitted.
#The chunk below initializes this object for a GARCH(1,1) model

model_specs_g <- ugarchspec(
  variance.model = list(model="sGARCH",garchOrder=c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean=TRUE), #including mean (assumed 0)
  distribution.model = "norm" #assuming gaussian innovations here
)


model_g <- ugarchfit(spec = model_specs_g, data = log_returns_DJ) #fits the model

model_g #outputs the estimatd parameters

plot(model_g,which =9) #9 corresponds to QQplot of residuals


# Fitting the GARCH(1,1) model with $t$-distributed innovations

model_specs_t <- ugarchspec(
  variance.model = list(model="sGARCH",garchOrder=c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean=TRUE), #excluding mean (assumed 0)
  distribution.model = "std" #assuming gaussian innovations here
)


model_t <- ugarchfit(spec = model_specs_t, data = log_returns_DJ)

model_t

plot(model_t, which =9) 


# Fitting the GARCH(1,1) model with Generalized Hyperbolic innovations

model_specs_ghyp <- ugarchspec(
  variance.model = list(model="sGARCH",garchOrder=c(1,1)),
  mean.model = list(armaOrder = c(0,0), include.mean=TRUE), #excluding mean (assumed 0)
  distribution.model = "ghyp" #assuming gaussian innovations here
)


model_ghyp <- ugarchfit(spec = model_specs_ghyp, data = log_returns_DJ)

model_ghyp

plot(model_ghyp,which=9)




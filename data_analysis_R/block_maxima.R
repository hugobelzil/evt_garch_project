if (!require(fExtremes)){
  install.packages("fExtremes") #package which contains block maxima methods
}
library(fExtremes)

if (!require(extRemes)){
  install.packages("extRemes") #package which contains block maxima methods
}
library(extRemes)

if (!require(ismev)){
  install.packages("ismev") #package containing the dow jones data
}
library(ismev)

if (!require(qrmtools)){
  install.packages("qrmtools") #package containing functions for dj data
}
library(qrmtools)






#getting the data
data(dowjones)
log_returns_DJ <- 100*returns(dowjones$Index,method="logarithmic")


## Block maxima

### 30-day blocks
bm_30 <- blockMaxima(log_returns_DJ,block=30)
output_bm_30 <- fevd(bm_30,type="GEV",method="MLE")
output_bm_30

#diagnostic plots
plot(output_bm_30,type=c("qq"),main="QQ-Plot for 30-day Block Maxima model")


### 50-day blocks
bm_50 <- blockMaxima(log_returns_DJ,block=50)
output_bm_50 <- fevd(bm_50,type="GEV",method="MLE")
output_bm_50

#diagnostic plots
plot(output_bm_50,type=c("qq"),main="QQ-Plot for 50-day Block Maxima model")


### 75-day blocks
bm_75 <- blockMaxima(log_returns_DJ,block=75)
output_bm_75 <- fevd(bm_75,type="GEV",method="MLE")
output_bm_75

#diagnostic plots
plot(output_bm_75,type=c("qq"),main="QQ-Plot for 75-day Block Maxima model")


### 100-day blocks
bm_100 <- blockMaxima(log_returns_DJ,block=100)
output_bm_100 <- fevd(bm_100,type="GEV",method="MLE")
output_bm_100

#diagnostic plots
plot(output_bm_100,type=c("qq"),main="QQ-Plot for 100-day Block Maxima model")




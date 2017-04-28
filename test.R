library(nnet)
library(ggplot2)
taxi=read.csv("taxi.csv",header=T)
index = sample(nrow(taxi),100000)
taxi.subset=taxi[index,]
write.csv(taxi.subset,file="subset1.csv")
write.csv(taxi.subset,file="subset2.csv")
write.csv(taxi.subset,file="subset3.csv")
write.csv(taxi.subset,file="subset4.csv")
write.csv(taxi.subset,file="subset5.csv")
write.csv(taxi.subset,file="subset6.csv")
write.csv(taxi.subset,file="subset7.csv")
write.csv(taxi.subset,file="subset8.csv")
write.csv(taxi.subset,file="subset9.csv")
write.csv(taxi.subset,file="subset10.csv")
taxi.subset=read.csv("subset3.csv",header=T)
index3= sample(2,nrow(taxi.subset),replace=TRUE,prob=c(.2,.8))
taxi.training=taxi.subset[index3==1,]
taxi.testing=taxi.subset[index3==2,]

hi=nnet(fare_amount~pickup_longitude+pickup_latitude+trip_distance+dropoff_longitude+dropoff_latitude
	,data=taxi.training,size=200,MaxNWts=10000,maxit=10000,linout=TRUE)
np = predict(hi,taxi.testing)
plot(np,taxi.testing$fare_amount)

np = predict(hi,taxi.subset)
plot(np,taxi.subset$fare_amount)

np = predict(hi,taxi.training)
plot(np,taxi.training$fare_amount)
mean(taxi.testing$fare_amount==np)
summary(np)
qplot(hi)

modela = lm(fare_amount~pickup_longitude+pickup_latitude+trip_distance+dropoff_longitude+dropoff_latitude
	,data=taxi.training)
summary(modela)
asdf=predict(modela,taxi.testing,interval="prediction")
plot(modela$fit,taxi.training$fare_amount)
plot(asdf[,"fit"],taxi.testing$fare_amount)

checkAccuracy <- function(fit,upperbound,lowerbound){
	if (fit <= upperbound && fit >= lowerbound) {
		return(1)
	} else {
		return(0)
	}
}
taxi.training$fare_amount[1]-modela$fit[1]
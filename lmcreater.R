days = c("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
daysIndex = c(1,2,3,4,5,6,7)
names(days) <- daysIndex
theFile=c()
for (i in 1:7) {
	for (j in 0:23) {
		taxi=read.csv(sprintf("%s%i.csv",days[i],j),header=T)
		theModel = lm(Fare~.,data=taxi)
		theFile=rbind(theFile,theModel$coefficients)
	}
}
write.csv(theFile,file="LM.csv")
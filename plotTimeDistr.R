setwd("/Users/Xing/documents/IdentificationProject/Data_V3")

data = read.csv("LIWC_bucketByMonth.csv", header = TRUE, sep = ',')
month=unique(data$Segment)
m=matrix(0,length(month),93)
for (i in 1:length(month)){
  m[i,]=colMeans(data[which(data$Segment==month[i]),3:95])
}

amputeeNames = read.csv("AmputeeNames.csv", header = F, sep = ',')
nonAmputeeNames = read.csv("NonAmputeeNames.csv", header = F, sep = ',')
label=matrix('N',dim(data)[1],1)
for (i in 1:dim(amputeeNames)[1]){
    label[grep(amputeeNames[i,1],data$Filename)]='A'
}
amputee=data[label=='A',]
nonamputee=data[label=='N',]

a_month=unique(amputee$Segment)
a_month=a_month[a_month<=80]
a_mean=matrix(0,length(a_month),93)
for (i in 1:length(a_month)){
  a_mean[i,]=colMeans(amputee[which(amputee$Segment==a_month[i]),3:95])
}


n_month=unique(nonamputee$Segment)
n_month=n_month[n_month<=80]
n_mean=matrix(0,length(n_month),93)
for (i in 1:length(n_month)){
  n_mean[i,]=colMeans(nonamputee[which(nonamputee$Segment==n_month[i]),3:95])
}







#setwd('/Users/Xing/documents/IdentificationProject/resultsv3/plots')
setwd('/Users/Xing/documents/IdentificationProject/resultsv3/plotlim')
#setwd('/Users/Xing/documents/IdentificationProject/ResultsV3/plotlimPoints')
colname=colnames(data)


par(mfrow=c(2,2))

for (i in 1:93){
  jpeg(paste(colname[i+2], '.jpg', sep = ""), width = 800, height = 600)
  
  plot(a_month, a_mean[,i],pch=20,cex=0.5,xlim=c(0,80),col='Red',type='l',main=colname[i+2])
  lines (n_month, n_mean[,i],pch=20,cex=0.5,col='Black')
  #points (n_month, n_mean[,i],pch=20,cex=0.5,col='Black')
  legend ('topright',legend=c('amputee','nonamputee'),col=c('Red','Black'),lty=2:2,box.lty=0,cex=0.7)
  
  dev.off()
}







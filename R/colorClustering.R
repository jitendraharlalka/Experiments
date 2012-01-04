library("scatterplot3d")

#Read relevant columns from colors.csv
colorDataset=read.csv("colors.csv", sep="\t", header=TRUE)
colHexs<-colorDataset[,-c(2,3,4,8)]

#Create a k means clustering with 5 clusters over r,g,b values
myMeans=kmeans(colHexs[,c(2,3,4)],centers=5)

#Plot each color as a point in 3-dimension using r,g,b values of colors. Points are plotted using the colors represented by (r,g,b) values.
s3d<-scatterplot3d(colHexs[,2],colHexs[,3],colHexs[,4],color=rgb(colHexs[,2],colHexs[,3],colHexs[,4],maxColorValue=255),pch=myMeans$cluster)

#Plot the center in the representative (r,g,b) value of the center
points(s3d$xyz.convert(myMeans$centers[,1],myMeans$centers[,2],myMeans$centers[,3]),col=rgb(myMeans$centers[,1],myMeans$centers[,2],myMeans$centers[,3],maxColorValue=255),pch=19,cex=2)

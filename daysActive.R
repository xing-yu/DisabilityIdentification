# plot active days of online users

data = read.csv(file.choose(), sep = ',', header = FALSE)

hist(data$V1, main = "Distribution of active days of online users(total)",
     xlab = "Days", ylab = "Number of users")

summary(data$V1)

sum(data$V1>3000)/length(data$V1)


sum(data$V1>2700)
/length(data$V1)

#EXERCICI 1
#apartat a)
Valors <- c(0,1,2,3,4,5)
Frequencies <- c(40,52,83,24,12,4)

taula = data.frame(cbind(Valors,Frequencies))
taula
transform(taula,Frequencia_Acumulada= cumsum(Frequencies), Relativa= round(
  prop.table(Frequencies),3), Relativa_Acumulada = round(cumsum(prop.table(Frequencies)),3))


#apartat b)
     #mitjana
mean(Frequencies)
     #mediana
median(Frequencies)
     #variància corregida
var(Frequencies)
     #variància
varp <- function(Frequencies)
n <- length(Frequencies)
variancia <- var(Frequencies)*(n-1)/n
variancia

    #desviació tipica corregida
sd(Frequencies)
     #desviació tipica 
varp <- function(Frequencies)
n <- length(Frequencies)
variancia <- var(Frequencies)*(n-1)/n
desviacio <- variancia**0.5
desviacio

#apartat c)
quantile(Frequencies)
boxplot(Frequencies, main = "Diagrama de caixa de les freqüències")



#EXERCICI 2

head(iris)
table(iris$Species)


#apartat a)
boxplot(Petal.Width~Species,ylab="Petal Width")

#apartat b)

ab_fit <- lm(Petal.Width~Petal.Length, data = iris)
plot(Petal.Width~Petal.Length, data = iris,col=Species, xlab="Petal Length",ylab="Petal Width")
abline(ab_fit, col = "skyblue", lwd = 3)
legend(x = "topleft", legend = c(levels(Species)), fill = c("black","red","green"), 
       title = "Species")


regresion <- lm(Petal.Width~Petal.Length, data = iris)
summary(regresion)

#apartat c)
skewness(iris$Petal.Width[iris$Species=="setosa"])
Petal.Width <- iris$Petal.Width[iris$Species=="setosa"]
hist(Petal.Width, freq = FALSE)
curve(dnorm(x, mean(Petal.Width), sd(Petal.Width)), col = 4, lty = 2, lwd = 2, add=T)

#EXERCICI 3
print(motos)
head(motos)
names(motos)

grupos <- group_by(motos, motos$MARXES)
summarise(grupos,
          num = n()
)
#apartat a)


install.packages('dplyr')
library(dplyr)

#CANVI MANUAL

    #Mitjana
manu<- select(filter(motos, MARXES=='M'), PREU)
manu
preum <-x$PREU
preum
mean(preum)


    #Mediana
median(preum)

    #variància 

varp <- function(Frequencies)
  n <- length(Frequencies)
variancia <- var(Frequencies)*(n-1)/n
variancia


    #variància corregida
var(preum)
    #desviació 
desv <- varian**0.5
desv
    #desviació tipica corregida
sd(preum)

    #minim

min(preus)

    #maxim
max(preus)

#CANVI AUTOMÀTIC

#Mitjana
aut<- select(filter(motos, MARXES=='A'), PREU)
aut
preusa <-aut$PREU
preusa
mean(preusa)


#Mediana
median(preusa)

#variància 

varianauto <- function(preum)
  n <- length(preusa)
varianautomatica <- varianauto(preusa)*(n-1)/n
varianautomatica

#variància corregida
var(preusa)
#desviació 
desv <- varianautomatica**0.5
desv
#desviació tipica corregida
sd(preusa)

#minim

min(preusa)

#maxim
max(preusa)

#apartat b)

varA <- max(preusa) - min(preusa)
varA
varM <-max(preus) - min(preus)
varM

#apartat c)

preu <- motos$PREU
cilindrada <- motos$CC

ab_fit <- lm(cilindrada~preu)
plot(cilindrada~preu, data = motos, xlab="Cilindrada",ylab="Preu")
abline(ab_fit, col = "skyblue", lwd = 3)

regresion <- lm(cilindrada~preu, data = motos)
summary(regresion)


#apartat d)

filtracio <- motos[1:5,]
filtracio
preufilt <- filtracio$PREU
preufilt
cilindradafilt <- filtracio$CC
cilindradafilt
     #Valors ajustats
recta <- lm(cilindrada~preu, data = motos)
valorsajustats <- fitted(recta)
valaj <- valorsajustats[0:5]
valaj

      #Residus

recta <- lm(cilindrada~preu, data = motos)
residus <- residuals(recta)
r<-residus[0:5]
r

#apartat d)

#e
preu <- motos$PREU
cilindrada <- motos$CC
recta <- lm(cilindrada~preu, data = motos)
anova(recta)
#SQT, SQE i SQR els hem extret de la taula obtinguda fent anova()
#SQT
SQT <- sum(anova(recta)[,2])
SQT
      
      #SQE

SQE <- 3524185
SQE
      #SQR

SQR<- 15503754
SQR
#Es compleix SQT = SQR+SQE
SQT
(SQR+SQE)

#Es compleix R**2 = 1- SQE/SQT
R <- summary(recta)$r.squared
Comp <- 1- (SQE/SQT)
R
Comp

#EXERCICI 4
#apartat a)
     #Mitjanes x
taula <- Practica1[c(2:12),]
x1 <- strtoi(taula$I)
x2 <- strtoi(taula$II)
x3 <- strtoi(taula$III)
x4 <- strtoi(taula$IV)
mit1 <- mean(x1)
mit2 <- mean(x2)
mit3 <- mean(x3)
mit4 <- mean(x4)
mit1 
mit2 
mit3 
mit4
     #Variància x

varp <- function(x1)
  n <- lenght(x1)
var1 <- var(x1)*(n-1)/n
var1x

varp <- function(x2)
  n <- lenght(x2)
var2 <- var(x2)*(n-1)/n
var2x

varp <- function(x3)
  n <- lenght(x3)
var3 <- var(x3)*(n-1)/n
var3x

varp <- function(x4)
  n <- lenght(x4)
var4 <- var(x4)*(n-1)/n
var4x
     #Mitjanes y

y1 <- as.double(taula$...2)
y2 <- as.double(taula$...4)
y3 <- as.double(taula$...6)
y4 <- as.double(taula$...8)
mit1y <- mean(y1)
mit2y <- mean(y2)
mit3y <- mean(y3)
mit4y <- mean(y4)
mit1y 
mit2y 
mit3y 
mit4y

     #Variància y

varp <- function(y1)
  n <- lenght(y1)
var1 <- var(y1)*(n-1)/n
var1y

varp <- function(y2)
  n <- lenght(y2)
var2 <- var(y2)*(n-1)/n
var2y

varp <- function(y3)
  n <- lenght(y3)
var3 <- var(y3)*(n-1)/n
var3y

varp <- function(y4)
  n <- lenght(y4)
var4 <- var(y4)*(n-1)/n
var4y


#apartat b)
  #coeficient de correlació
     #xy1
install.packages("ggpubr")
library("ggpubr")

cor1 <- cor(x1, y1,  method = "pearson", use = "complete.obs")
cor1
     #xy2
cor2 <- cor(x2, y2,  method = "pearson", use = "complete.obs")
cor2
     #xy3
cor3 <- cor(x3, y3,  method = "pearson", use = "complete.obs")
cor3
     #xy4
cor4 <- cor(x4, y4,  method = "pearson", use = "complete.obs")
cor4
  #Coeficient de determinació

det1 <- cor1*cor1
det2 <- cor2*cor2
det3 <- cor3*cor3
det4 <- cor4*cor4
det1 
det2 
det3 
det4 


  #Recta de regressió
 #X1- Y1
regresion1 <- lm(y1 ~ x1, data = taula)
summary(regresion1)

  #X2- Y2
regresion2 <- lm(y2 ~ x2, data = taula)
summary(regresion2)

  #X3- Y3
regresion3 <- lm(y3 ~ x3, data = taula)
summary(regresion3)

  #X4- Y4
regresion4 <- lm(y4 ~ x4, data = taula)
summary(regresion4)

  #Representció diagrama + recta de regressió
     #xy1
ab_fit1 <- lm(y1~x1)
plot(y1~x1, data = taula, xlab="X1",ylab="Y1")
abline(ab_fit1, col = "skyblue", lwd = 3)

     #xy2
ab_fit2 <- lm(y2~x2)
plot(y2~x2, data = taula, xlab="X2",ylab="Y2")
abline(ab_fit2, col = "skyblue", lwd = 3)

     #xy3
ab_fit3 <- lm(y3~x3)
plot(y3~x3, data = taula, xlab="X3",ylab="Y3")
abline(ab_fit3, col = "skyblue", lwd = 3)

     #xy4
ab_fit4 <- lm(y4~x4)
plot(y4~x4, data = taula, xlab="X4",ylab="Y4")
abline(ab_fit4, col = "skyblue", lwd = 3)


#EXERCICI 5
#apartat a)
fil <- filter(sao.paulo.properties.april.2019, Negotiation.Type == 'rent')
fil
x <- select(filter(sao.paulo.properties.april.2019, Negotiation.Type == 'rent'),'Price','Condo','Size','Rooms','Elevator')
x
apartata<- select(sao.paulo.properties.april.2019,'Price','Condo','Size','Rooms','Elevator')
apartata

#apartat b)
mit <- mean(apartata$Condo)
apartata$Condo[apartata$Condo == "0"] <- mit
apartata
mean(apartata$Condo)

#apartat c)
preu <- apartata$Price
condo <- apartata$Condo
size <- apartata$Size
room <- apartata$Rooms
ascensor <- apartata$Elevator

#mitjana
mean(preu)
mean(condo)
mean(size)
mean(room)
mean(ascensor)

#mediana
median(preu)
median(condo)
median(size)
median(room)
median(ascensor)

#variancia

preu1 <- as.double(preu)

varp <- function(preu1)
  n <- lenght(preu1)
var1 <- var(preu1)*(n-1)/n
var1

varp <- function(condo)
  n <- lenght(condo)
var2 <- var(condo)*(n-1)/n
var2

varp <- function(size)
  n <- lenght(size)
var3 <- var(size)*(n-1)/n
var3

varp <- function(room)
  n <- lenght(room)
var4 <- var(room)*(n-1)/n
var4

varp <- function(ascensor)
  n <- lenght(ascensor)
var5 <- var(ascensor)*(n-1)/n
var5


#desviació tipica
des1 <- var1**0.5
des1

des2 <- var2**0.5
des2

des3 <- var3**0.5
des3

des4 <- var4**0.5
des4

des5 <- var5**0.5
des5

#apartat d)
covc <- cov(preu,condo)
covc
covs <- cov(preu,size)
covs
covr <- cov(preu,room)
covr
cova <- cov(preu,ascensor)
cova

cor1 <- cor(preu,condo,  method = "pearson", use = "complete.obs")
cor1
cor2 <- cor(preu,size,  method = "pearson", use = "complete.obs")
cor2
cor3 <- cor(preu,room,  method = "pearson", use = "complete.obs")
cor3
cor4 <- cor(preu,ascensor,  method = "pearson", use = "complete.obs")
cor4

ab_fit1 <- lm(preu~size)
plot(preu~size, data = apartata, xlab="Preu",ylab="Mida")
abline(ab_fit1, col = "skyblue", lwd = 3)

regresion1 <- lm(preu~size, data = apartata)
summary(regresion1)

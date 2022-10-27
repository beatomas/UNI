#EXERCICI 1
#  a)
f <- function(k){
  if (k == 2){
    1/16
  } 
  else if (k == 4 || k == 5 || k == 10 || k == 12 ||k == 15 || k == 20){
    (k-3)/(4*k)
  }
  else{
    "No compleix cap condició" 
  }
}

#  b)

valors <- c(2,4,5,10,12,15,20)
probs <-c(f(2),f(4),f(5),f(10),f(12),f(15),f(20))

plot(valors,probs,type="h",col="red",main = "Funció de massa")

probcum <- cumsum(probs)

s <- stepfun(valors,c(0,probcum))
plot(s, verticals=FALSE, col="red",main = "Funció de distribució")

#  c) 
P = (f(5)+f(10)+f(12))/(f(5)+f(10)+f(12)+f(15)+f(20))
P*100

# d)

E <- sum(valors*probs)
Var <- sum((valors**2)*probs) - (E**2)

E
Var

# e)

n <- 300
mostra <- sample(valors,n,prob=probs,replace=TRUE)

varp <- function(x){
  n <- length(x)
  varx <- var(x)*(n-1)/n
  varx
}
mean(mostra)
varp(mostra)

#EXERCICI 2

#c
sequencia <- seq(0,10, by=1)
prob = 0.3

dgeom1 <- dgeom(sequencia,prob)
plot(dgeom1,type="h",col="red",xlab = "Valors", ylab ="Probabilitats",main = "Funció de massa")


probcum <- cumsum(dgeom1)
probcum
s <- stepfun(sequencia,c(0,probcum))
plot(s, verticals=FALSE, col="red",main = "Funció de distribució")


#d
x <- c(1,2,3,4,5,6)

llen = sample(x,200,replace=TRUE)
llen
hist(llen, breaks=65, xlab="Valors", ylab="Total de cops que ha sortit el valor",main = "Historiagrama 200 simulacions del llençament d'un dau")


llen1 <- c(llen)
llen1

valor_1=0
valor_2=0
valor_3=0
valor_4=0
valor_6=0
Exitos=0 
contador=1

for(i in 1:200){ #Inicia el bucle, cada iteracion es un experimento
  {if(llen1[i]==5) Exitos=Exitos+1} 
  {if(llen1[i]==1) valor_1=valor_1+1}
  {if(llen1[i]==2) valor_2=valor_2+1}
  {if(llen1[i]==3) valor_3=valor_3+1}
  {if(llen1[i]==4) valor_4=valor_4+1}
  {if(llen1[i]==6) valor_6=valor_6+1}}
#Si el elemento j-esimo en M es igual a 5, incrementa

for (u in llen){
  if (u != 5){
    contador <- contador +1
  }else{
    break
  }
}
valors <- c(valor_1,valor_2,valor_3,valor_4,Exitos,valor_6)
valors
contador
#e

p <- 1/6
pgeom(10,p) - pgeom(3,p)


#EXERCICI 3
#a)
x <- seq(0,2, by = 0.05)
funcio <- function(x){
  (5*x^4)/32
}
plot(x, funcio(x), xlab = 'x', ylab = 'F(x)', type = "l", col = "red", main = "Funció de densitat")


integral <- function(x){
  (x^5)/32
}
plot(x, integral(x), xlab = 'x', ylab = 'F(x)', type = "l", col = "red", main = "Funció de distribució")


#b)
x <- seq(0,2, by = 0.05)
u <- runif(500)
y <- 2*(u^0.2) #Inversa de la dunció de distribució
hist(y, freq = FALSE, xlab = "Valors", ylab = "Probabilitat", main = "Histograma amb la funció de densitat")
z <- seq(0, 2, by = 0.05)
t <- (5*x^4)/32
lines (z, t, col = "red", lwd = 2)

#c)
#Calculem l'esperança i la variància teòricament

int1 <- integrate(function(x) (5/32*(x^5)),lower= 0, upper= 2)$value
int2 <- integrate(function(x) (5/32*(x^6)),lower= 0, upper= 2)$value
int1
Var <- int2 - int1^2
Var

#Calculem la mitjana i la variància per a la llista de num aleatoris
funcio <- function(x){
  (5*x^4)/32
}  
x <- seq(0,2, by = 0.05)
varp <- function(x){
  n <- length(x)
  varx <- var(x)*(n-1)/n
}
valors <- c(x)
probs <- c(funcio(valors))
mostra <- sample(valors,n,prob=probs,replace=TRUE)

mean(mostra)
var <- varp(mostra)
var

#d)
#(x1^5)/32 <- 0.85  Aïllem la x1 i obtenim la línia següent
x1 <- (0.85*32)^0.2
x1
funcio(x) < x1 #Comprovem quantes de les simulacions tenen un valor inferior a x1



#EXERCICI 4

#a


a <- pnorm(295,298,3)
a
#b

b <-       qnorm(0.1,298,3)
b

#c
primera <- 1-(pbinom(1,6,0.1586553))
primera

c <- 1-(pbinom(29,100,primera))
c


#d

n <-100
p <- primera
q <- 1-p
p

variancia <- n*p*q
esperanza <- n*p
dt <- sqrt(variancia)

dt
variancia
esperanza

#e

1-pnorm(30,esperanza,dt)



#EXERCICI 5

#lamba = 4

l <- 4


#a)

N <- 100
B<-400
A <- matrix(rpois(B, l), nrow = N, ncol=B)

A

freq_rel <- apply(A,1,mean)


freq_rel


mitjana <- l
variancia <- l

vec <- (freq_rel-mitjana)/((variancia**(1/2))/(B**(1/2)))

minim = min(vec)
maxim = max(vec)

hist(vec, freq =FALSE, xlab="Valors", ylab="Probabilitat",main = "Historiagrama amb la funció de densitat")
curve(dnorm(x,mean(vec),sd(vec)), from=minim,to=maxim, add=TRUE, lwd=2,col="red")


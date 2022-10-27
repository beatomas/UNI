
#EXERCICI 1

#  a)

neperiano <- log(5,10)
elevado <- 3**5
arrel<-sqrt(3*pi)
sinus <- sin(2*pi/3)
exponencial <- (exp(1))**1/3
ex1a <- (neperiano + elevado - (arrel*sinus) - exponencial)
ex1_alternativa <- (log(5,10)+3**5-(sqrt(3*pi)*sin(2*pi/3))-(exp(1))**1/3)
paste(ex1a)
paste(ex1_alternativa)

#  b) -----------

ex1b <- ((sqrt(3))+(5*pi))/(7-((2)**(1/5)))
paste(ex1b)

#  c)

ex1c <- (2**(-7/13))*((11/9)**(-8/7))
paste(ex1c)

#  d)

Ex1d <- function(){
  k <- 763:825
  sum(1/k)
}
Ex1d()


#  e)

Ex1e <- function(){
  k <- 4:9
  sum(((3**k)*factorial(k))/(k**k))
}
Ex1e()


#EXERCICI 2

A <- matrix(c(7,8,10,5), nrow=2)
B <- matrix(c(1,4,5,0,0,11), nrow=2)
C <- matrix(c(7,0,3,12,9,3), nrow=3)
D <- matrix(c(13,7,2,3), nrow=2)

#  a)
ex2a <- A+D
paste(ex2a)


#  b)
ex2b1 <-  A %*% B
paste(ex2b1)
ex2b2 <- C %*% A
paste(ex2b2)
ex2b3 <- A %*% D
paste(ex2b3)

# EXERCICI 3

# a)
f <- function(n){
  k <- 1:n
  sum(exp(-k))
}
f(10)
f(100)

# b)
g <- function(j,n){
  k <- j:n
  sum(1/factorial(k))
}
g(4,10)
g(6,23)


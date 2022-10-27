install.packages('EnvStats')
library(EnvStats)
install.packages('dplyr')
library(dplyr)

#EXERCICI 1
#a)
   PH = Nadons$pH
   int_ph <- t.test(PH, conf.level = 0.90)$conf.int
   int_ph

#b)
   mares_fumadores<- select(filter(Nadons, Madre=='F'),pH)
   mares_no_fumadores<- select(filter(Nadons, Madre=='NF'),pH)
   int_mares_fumadores <- t.test(mares_fumadores, conf.level = 0.90)$conf.int
   int_mares_fumadores
   int_mares_no_fumadores <- t.test(mares_no_fumadores, conf.level = 0.90)$conf.int
   int_mares_no_fumadores

#c)
   int_df <- t.test(mares_no_fumadores,mares_fumadores, var.equal = FALSE, level.conf = 0.95)$conf.int
   int_df 

#d)
   test <- t.test(mares_fumadores, mares_no_fumadores, alternative="two.sided", mu=0, paired=FALSE, var.equal=FALSE, conf.level=0.95)
   test

      
#EXERCICI 2
#a)
   parc1_<- select(filter(notes, V1!='parcial1'),V1)
   parc2_<- select(filter(notes, V2!='parcial2'),V2)
   
   parc1 <- c()
   for (v in parc1_){
     b <- as.numeric(v)
     parc1 <- c(parc1,b)
   }
   
   parc2 <- c()
   for (nota in parc2_){
     c <- as.numeric(nota)
     parc2 <- c(parc2,c)
   }
 
   con1 <- t.test(parc1, conf.level = 0.90)$conf.int
   con2 <- t.test(parc2, conf.level = 0.90)$conf.int
   
   con1
   con2

#b)
   int_dif <- t.test(parc1, parc2, paired = TRUE, conf.level = 0.92)$conf.int
   int_dif   

#c)
   #  parc1
       # Introduim la mostra i definim les variables
       alpha <- 0.07
       n <- length(parc1)
       a <- qchisq(alpha/2, n-1)
       b <- qchisq(1-alpha/2, n-1)
       
       # Calculem l'interval
       linf <- (n-1) / b * var(parc1)
       lsup <- (n-1) / a * var(parc1)
       linf; lsup 
    
    #  parc2
       # Introduim la mostra i definim les variables
       alpha <- 0.07
       n <- length(parc2)
       a <- qchisq(alpha/2, n-1)
       b <- qchisq(1-alpha/2, n-1)
       
       # Calculem l'interval
       linf <- (n-1) / b * var(parc2)
       lsup <- (n-1) / a * var(parc2)
       linf; lsup 
       
#d)
       parc1_1 <- (parc1*0.4) 
       parc2_2 <-(parc2*0.6)
       suma <- parc1_1+  parc2_2
       int_dif <- t.test(suma, conf.level = 0.95)$conf.int
       int_dif 
       
#e)
       b= 0
       for (nota in suma){
          if (nota>5){
          b <- b+1
          }
       }
       
       per <- (b*100)/80

       prop <- prop.test(b, 80, conf.level = 0.95)$conf.int
       prop
       
       
#EXERCICI 3
       n <- nrow(kidsfeet)
#a)
       lefties <- select(filter(kidsfeet, Lateralitat != 'R'), Lateralitat)
       x <-nrow(lefties)
       prop.test(x, n, p = 0.3, alternative = 'less', correct = FALSE)
       #Resultat: 5%: 0.09803 > 0.05. 
       
       prop.test(x, n, p = 0.3, alternative = 'less', conf.level = .90, correct = FALSE)
       #Resultat: 10%: 0.09803 < 0.1 
       
#b) 
       amplada <- kidsfeet$Amplada
       varTest(amplada, alternative = 'less', sigma.squared = 0.56**2)
       #5%: 0.2359 > 0.05 
       
       varTest(amplada, alternative = 'less', conf.level = 0.97, sigma.squared = 0.56**2)
       #3%: 0.2359 > 0.03 
       
#c) 
       left_longitud <- select(filter(kidsfeet, Lateralitat != 'R'), Longitud)
       left <- c()
       for (l in left_longitud){
          b <- as.numeric(l)
          left <- c(left,b)
       }
       
       right_longitud <- select(filter(kidsfeet, Lateralitat == 'R'), Longitud)
       right <- c()
       for (r in right_longitud){
          b <- as.numeric(r)
          right <- c(right,b)
       }
       
       t.test(left, right)
       #0.4179 > 0.05 
       
#d) 
       t.test(left, right, var.equal = TRUE)
       #0.444 > 0.05 
       
#e) 
       var.test(left,right)
       #0.7597 > 0.05
       

#EXERCICI 4
#a)
       velocitats <- select(filter(tterreny),Velocitat)
       vel <- c()
       for (v in velocitats){
          b <- as.numeric(v)
          vel <- c(vel,b)
       }
       t.test(vel, mu = 155, alternative = "two.sided")
       #Resultat 0.1664 > 0.05
       
#b)
       consum <- select(filter(tterreny),Consum.Urba)
       con <- c()
       for (c in consum){
          b <- as.numeric(c)
          con <- c(con,b)
       }
       t.test(con, mu = 13.2, alternative = "less")
       #Resultat 0.06069 > 0.05
       
#c)
       consum90 <- select(filter(tterreny),Consum90)
       con90 <- c()
       for (co in consum90){
          b <- as.numeric(co)
          con90 <- c(con90,b)
       }
       var.test(con90, con)
       #Resultat p-valor < 0.05
       
#d)
       t.test(con, con90, mu = 3, paired = TRUE)
       #p-valor < 0.05
       
#e)
       consum120 <- select(filter(tterreny),Consum120)
       con120 <- c()
       for (con in consum120){
          b <- as.numeric(con)
          con120 <- c(con120,b)
       }
       var.test(con120, con90, ratio = 2)
       #Resultat 0.4818 > 0.05

       
#EXERCICI 5
       n <- nrow(anime)
#a)
       emisio <- select(filter(anime, ESTAT != 0),ESTAT)
       xe <- nrow(emisio)
       prop.test(xe, n)$conf.int
       #Resultat: [ 0.003881908 , 0.046759727]
       
#b)
       mang <- select(filter(anime, FONT == 'Manga'),FONT)
       nm <-nrow(mang)
       prop.test(nm, n)$conf.int
       #Resultat: [ 0.3947572 , 0.5366092]
       
#c)
       nnm <- n-nm
       xy <- c(nm,nnm)
       nn <- c(200,200)
       prop.test(xy, nn, alternative = 'less', correct = FALSE)
       #Resultat 0.08076 > 0.05
       
#d)
       m2000 <- select(filter(anime, ANY>=2000, FONT == 'Manga'),PUNTS)
       l <- select(filter(anime, ANY>=2000, FONT == 'Llibre'),PUNTS)
       
       t.test(m2000, l , alternative = "greater", var.equal = FALSE)
       #0.04294 < 0.05
       
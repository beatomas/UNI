#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

int lectura(int fd1, char llista[]){
int i=0;
char j;

if( read(fd1,&j,1) == 0){
    return 0;
}
while(j!='\n'){
    llista[i]=j;
    i++;
    read(fd1,&j,1);
    }
    llista[i] = '\0';
return 1;
}


unsigned long getField( int fn, char line[] ){
 int i;
 char *p, aux[256];
 strcpy( aux, line );
 p = strtok( aux, "," );
 for ( i = 0; i < fn; i++ ) p = strtok( NULL, "," );
return strtoul( p, NULL, 10 );
}


int contabilitzacio(int likesreci, int likesreal, int numamigos, int numdies, int contador, float *mitreci, float *mitreal, float *mitamigos, float *mitdies){

*mitreci=(likesreci*1.0)/contador;
*mitreal=(likesreal*1.0)/contador;
*mitamigos=(numamigos*1.0)/contador;
*mitdies=(numdies*1.0)/contador;
}


int main(){
char llista[180];
int fd1;
int doc;
int max1=0, max2=0, max3=0;
int likesreci=0;
int likesreal=0;
int numamigos=0;
int numdies=0;
int contador=0;
char maxlikes[180], maxreal[180], maxdies[180];
char x;
int i;
int k;
char num1[180], num2[180], num3[180], num4[180];
float mitreci=0;
float mitreal=0;
float mitamigos=0;
float mitdies=0;
char cap[180];


fd1=open("pseudo_facebook.csv",O_RDWR);
lectura(fd1, cap);
while(1){
k=lectura(fd1,llista);
if(k==0){
break;}
else{
likesreci=likesreci+getField( 11, llista);
likesreal=likesreal+getField(10, llista);
numamigos=numamigos+getField( 8,llista);
numdies=numdies+getField(7, llista);
contador++;
if ((getField(11, llista))>max1);{
    max1=getField(11, llista);
    strcpy(maxlikes, llista);
    }

if ((getField(10, llista))>max2);{
    max2=getField(10, llista);
    strcpy(maxreal, llista);
    }    

if ((getField(7, llista))>max3);{
    max3=getField(7, llista);
    strcpy(maxdies, llista);
    }

}
}
contabilitzacio(likesreci, likesreal, numamigos, numdies, contador, &mitreci, &mitreal, &mitamigos, &mitdies);

doc = open("GlobalOutput.txt", O_CREAT | O_RDWR,0644);

sprintf(num1,"%f",mitreal);
sprintf(num2,"%f",mitdies);
sprintf(num3,"%f",mitamigos);
sprintf(num4,"%f",mitreci);



write(doc," Average likes recived = ",strlen(" Average likes recived = ")-1);
write(doc, num1, strlen(num1));
write(doc,"\n Average likes given = ",strlen("\n Average likes given = ")-1);
write(doc, num4, strlen(num4));
write(doc,"\n Average tenure at FB = ",strlen("\n Average tenure at FB = ")-1);
write(doc, num3, strlen(num3));
write(doc,"\n Average number of friends = ",strlen("\n Average number of friends = ")-1);
write(doc, num2, strlen(num2));
write(doc,"\n",strlen("\n"));
write(doc, cap, strlen(cap));
write(doc,"\n Greatest number of received likes: ",strlen("\n Greatest number of received likes: ")-1);
write(doc, maxlikes, strlen(maxlikes)-1);
write(doc,"\n Greatest number of given likes: ",strlen("\n Greatest number of given likes: ")-1);
write(doc, maxreal, strlen(maxreal)-1);
write(doc,"\n Member for the longest time: ",strlen("\n Member for the longest time: ")-1);
write(doc, maxdies, strlen(maxdies)-1);



}



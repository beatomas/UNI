#include <stdio.h>
#include <stdlib.h>

# define N 512
int Mat1[N][N];
int Mat2[N][N];
int Vec1[N];
int Vec2[N];

void initMats(){
	int i, j;
	srand(8824553);
	for( i=0; i < N; i++ )
		for( j = 0; j < N; j++ ){
			Mat1[i][j] = rand()%100;
			Mat2[i][j] = rand()%100;
	}
	for( i=0; i < N; i++ ){
		Vec1[i] = rand()%100;
		Vec2[i] = rand()%100;
	}
} 



void mulMats(int Mat1[N][N],int Mat2[N][N],int Mat3[N][N]){
	int i,j,k;
	int resultat=0;
	for (i=0; i<N; i++){
		for (j=0; j<N; j++){
			resultat = 0;
			for (k=0; k<N; k++){
				resultat += Mat1[i][k]*Mat2[k][j];
				Mat3[i][j] = resultat;
				}
			}
	}

}

void Saxpy(int Vec1[N], int Vec2[N],int Vec3[N]){
	int k=4, i ;
	for (i=0; i<N; i++){
		Vec3[i]= (k*Vec1[i]) + (Vec2[i]);
	}
	
}

void transMat(int Mat1[N][N],int Mat4[N][N]){
	int i,j;
	for (i=0; i<N; i++){
			for (j=0; j<N; j++){
				Mat4[i][j]=Mat1[j][i];
				}
		}	
}

int SumDiagonal(int Mat1[N][N]){
	int i,j;
	int suma=0;
	for (i=0; i<N; i++){
		for (j=0; j<N; j++){
			if (i==j){
				suma= suma + Mat1[i][j];
			}
		}
	}
	return suma;
}


void sumElement(int Mat1[N][N], int Vec4[N]){
	int i,j;
	int suma = 0;
	for (i=0; i<N; i++){
		suma=0;
		for (j=0; j<N; j++){
			suma=suma+Mat1[j][i];
			Vec4[i] = suma;
		}
		
	}	
	
}



int main(void){

int Mat3[N][N];
int Vec3[N];
int Vec4[N];
int suma;
int Mat4[N][N];
int i,j;

initMats();

mulMats(Mat1, Mat2, Mat3);
	for (j=10; j<20; j++){
		printf("%d ", Mat3[10][j]);
}

printf("\n");
printf("\n");

Saxpy(Vec1,Vec2,Vec3);
	for (i=100; i<120; i++){
		printf("%d ", Vec3[i]);
}

printf("\n");
printf("\n");

transMat (Mat3, Mat4);
	for (i=10;i<20;i++){
		printf("%d ", Mat4[i][10]);
}

printf("\n");
printf("\n");

suma =SumDiagonal(Mat4);
	printf("%d ", suma);

printf("\n");
printf("\n");

sumElement(Mat3,Vec4);
	for (i=400;i<420;i++){
		printf("%d ",Vec4[i]);
}
}



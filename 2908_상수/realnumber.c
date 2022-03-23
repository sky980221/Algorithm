#include<stdio.h>

/* 734  -> 437  
893  -> 398
bigger num = 437 
*/
int main(){
int A,B,C,D,E; 
scanf("%d%d",&A,&B);
C = A/100 + (A%100 - A%10) +(A%10)*100;
D = B/100 + (B%100 - B%10) +(B%10)*100;

if(C>D){
    E = C;
}
else
    E = D;

printf("%d",E);
return 0;
}

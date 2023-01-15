#include<stdio.h>
#include<string.h>
void f_gets(char string[],int n){
    int i=0;
    while(i<n){
        scanf("%c",&string[i]);
        if(string[i]=='\n'){
            break;
        }
        i++;
    }
    string[i]='\0';
}
void encryption(char message[]){
    char temp;
    int c=(strlen(message)-1)/2;
    {
    if(strlen(message)%2==1)
    {
        for(int i=0; i<c; i++){
            temp=message[i];
            message[i]=message[c+i+1];
            message[c+i+1]=temp;
        }
    }
     if(strlen(message)%2==0)
    {
        for(int i=0; i<=c; i++){
            temp=message[i];
            message[i]=message[c+i+1];
            message[c+1+i]=temp;
            
        }
    }
    }
    for(int i=0; i<strlen(message);i++){
        temp=message[i];
        message[i]=message[strlen(message)-1-i];
        message[strlen(message)-1-i]=temp;
    }
    int i=0;
    while(message[i]!='\0')
    {
        message[i]=message[i]-2;
        i++;
    }
}
int main()
{
    char message[500];
    printf("Enter encrypted message: ");
    f_gets(&message[0],500);
    encryption(&message[0]);
    printf("Decrypted message: %s\n",message);
    return 0;
}







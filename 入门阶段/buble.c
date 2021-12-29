#include<stdio.h>
int main(void)
{
    int n;
    int tmp;
    int sum=0;
    int arry[10001];
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arry[i]);
    }
    for(int i=0;i<n;i++)
    for(int j=0;j<n-i-1;j++)
    {
        if (arry[j]>arry[j+1])
        {
            sum++;
            tmp=arry[j];
            arry[j]=arry[j+1];
            arry[j+1]=tmp;
        }
    }
    printf("%d",sum);
    return 0;

}
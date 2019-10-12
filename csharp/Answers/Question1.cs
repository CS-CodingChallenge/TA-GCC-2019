#include <iostream.h>
#include <math.h>
#include <stdio.h>
#include <conio.h>
void main()
{
clrscr();
float total, rem, deb, iper, rper, rep, dep, xyz;
long int abc, i;
cout<<"Enter Debt: ";
cin>>deb;
cout<<"Enter intrest percentage: ";
cin>>iper;
cout<<"Enter repayment percentage: ";
cin>>rper;
dep=deb/10;
rep=deb*(rper/100);
if (rep>50)
{
for(i=0; deb>50; i++)
{
deb=deb+deb*(iper/100);
deb=deb-rep;
}
}
else
{
for(i=0; deb>50; i++)
{
rep=50;
deb=deb+deb*(iper/100);
deb=deb-rep;
}
}
rem=deb;
total=(i*rep)+dep+rem;
abc=total;
xyz=total-abc;
if (xyz<0.5)
{
total=abc;
}
else
{
total=abc+1;
}
cout<<"Total repayment amount is: "<<total;
}

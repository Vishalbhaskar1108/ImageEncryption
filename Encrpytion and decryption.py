from PIL import Image
import math
imagename=input('enter the image name: ')
im1=Image.open(imagename)
im=im1
size1=list(im.size)
pix=list(im.getdata())
pixf = [x for sets in pix for x in sets]
#im2 = Image.new(im.mode, im.size)
#im2.putdata(pix)
#im2.show()
def mod1(b,e,m):
	if(m==1):
		y=0;
	else:
		c=1
		for i in range(1,e+1):
			c=(c*b)%m
		y=c
	return(y)
def encrypt(m,p,r,a,k):
	s=mod1(r,a,p)
	y=((m%p)*(mod1(s,k,p)))%p
	return(y)
def encrypt1(r,k,p):
	x=mod1(r,k,p)
	return(x)
def mulinv(b,n):
	r1=n
	r2=b
	t1=0
	t2=1
	while(r2>0):
		q=math.floor(r1/r2)
		r=r1-(q*r2)
		r1=r2
		r2=r
		t=t1-(q*t2)
		t1=t2
		t2=t
	if(r1==1):
		if(t1<0):
			t1=t1+n
			y=t1
		else:
			y=t1
	else:
		y=-1
	return(y)
def decrypt(y,x,a,p):
	m=((y%p)*(mulinv((x**a),p)))%p
	return(m)
p=int(input("prime number p:"))
r=int(input("primitive root r:"))
a=int(input("any a less than p-2:"))
k=int(input("any k less than p-2:"))
x=encrypt1(r,k,p)
print("\nx is: ", x)
print(" pix first 3 element:" ,pix[0])
print(" pixf first 3 element:",pixf[0],pixf[1],pixf[2])

for i in range(0,len(pixf)):
		pixf[i]=encrypt(pixf[i],p,r,a,k)

print("\nencrypted pixf first 3 element:",pixf[0],pixf[1],pixf[2])
pixg=[]
i=0
while(i<(size1[0]*size1[1]*3)-2):
	tup=(pixf[i],pixf[i+1],pixf[i+2])
	pixg.append(tup)
	i=i+3
print(" pixg first 3 elements:",pixg[0])
im2=Image.new(im.mode, im.size)
im2.putdata(pixg)
im2.show()
dc=int(input("\n enter 1 to decrypt:"))
if(dc==1):
	x=int(input("x calculted :"))
	a=int(input("any private key 'a' less than p-2:"))
	p=int(input("prime number p:"))
	for i in range(0,len(pixf)):
			pixf[i]=decrypt(pixf[i],x,a,p)
	print("decrypted pixf first 3 element:",pixf[0],pixf[1],pixf[2])
	pixg1=[]
	i=0
	while(i<(size1[0]*size1[1]*3)-2):
		tup=(pixf[i],pixf[i+1],pixf[i+2])
		pixg1.append(tup)
		i=i+3
	print(" pixg1 first 3 elements:",pixg1[0])
	im3=Image.new(im.mode, im.size)
	im3.putdata(pixg1)
	im3.show()


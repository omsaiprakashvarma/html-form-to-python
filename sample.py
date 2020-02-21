import csv
import time
with open("G:\galla\data.csv") as f:
    reader = csv.reader(f)
    your_list = list(reader)
# a=int(input("enter no of floors"))
# b=int(input("enter no of rooms"))
count=0  #Initialised Count heref
def loop1(i,our_list,s,m,l,smax,mmax,lmax,roomcapacity,lroom,mroom,a,b):
    if(your_list[i][6]=='small'):
        s=s+1
        smax=smax-1
    elif(your_list[i][6]=='large'):
        l=l+1
        lmax=lmax-1
    elif(your_list[i][6]=='medium'):
        m=m+1
        mmax=mmax-1
        count=s+m+l
        if(count<=roomcapacity):
            print(your_list[i][3]+"  "+your_list[i][2]+' allocatted at room'+str(lroom))
        else:
            lroom=b
            count=0
            if(your_list[i][6]=='small'):
                s=s+1
                smax=smax-1
            elif(your_list[i][6]=='large'):
                l=l+1
                lmax=lmax-1
            elif(your_list[i][6]=='medium'):
                m=m+1
                mmax=mmax-1
            count=s+l+m  
            if(count<=roomcapacity):
                print(your_list[i][3]+"  "+your_list[i][2]+' allocatted at room'+str(mroom))


def loop2(i,your_list,s,m,l,smax,mmax,lmax,roomcapacity,lroom,mroom,a,b):
    if(your_list[i][6]=='small'):
        s=s+1
        smax=smax-1
    elif(your_list[i][6]=='large'):
        l=l+1
        lmax=lmax-1
    elif(your_list[i][6]=='medium'):
        m=m+1
        mmax=mmax-1
    count=s+m+l 
    if(count<=roomcapacity):
        print(your_list[i][3]+"  "+your_list[i][2]+' allocatted at room'+str(mroom))
    else:
        if(mroom+1!=b):
            mroom=mroom+1
        else:
            mroom=mroom+2
            count=0
            if(your_list[i][6]=='small'):
                s=s+1
                smax=smax-1
            elif(your_list[i][6]=='large'):
                l=l+1
                lmax=lmax-1
            elif(your_list[i][6]=='medium'):
                m=m+1
                mmax=mmax-1
            count=s+l+m
            if(count<=roomcapacity):
                print(your_list[i][3]+"  "+your_list[i][2]+' allocation in room'+str(mroom))


def loop3(i,your_list,s,m,l,smax,mmax,lmax,roomcapacity,sroom,a,b):
        if(your_list[i][6]=='small'):
            s=s+1
            smax=smax-1
        elif(your_list[i][6]=='large'):
                l=l+1
                lmax=lmax-1
        elif(your_list[i][6]=='medium'):
                m=m+1
                mmax=mmax-1
        count=s+m+l 
        if(count<=roomcapacity):
                print(your_list[i][3]+"  "+your_list[i][2]+' allocatted at room'+str(sroom))
                        
        else:
                sroom=sroom+1
                count=0
                if(your_list[i][6]=='small'):
                        s=s+1
                        smax=smax-1
                elif(your_list[i][6]=='large'):
                        l=l+1
                        lmax=lmax-1
                elif(your_list[i][6]=='medium'):
                        m=m+1
                        mmax=mmax-1
                count=s+l+m
                if(count<=roomcapacity):
                        print(your_list[i][3]+"  "+your_list[i][2]+' allocatted at room'+str(sroom))   

def allot(n1,n2):
    a=n1
    b=n2
    lroom=1
    mroom=2
    sroom=b+1
    roomcapacity=200
    lmax=50
    mmax=100
    smax=200
    s=0
    l=0
    m=0
    for floor in range(0,a):
        for room in range(0,floor):
            for i in range(1,len(your_list)):
                if(your_list[i][8]=='TRUE'):
                    if(your_list[i][3]=='electronic' or your_list[i][2]=='rice'):
                        loop1(i,your_list,s,m,l,smax,mmax,lmax,roomcapacity,lroom,mroom,a,b)
                    if(your_list[i][7]=='Daily Needs' or your_list[i][7]=='Kitchen Needs' and your_list[i][3]!='electronic'):
                        loop2(i,your_list,s,m,l,smax,mmax,lmax,roomcapacity,lroom,mroom,a,b)
                    if(your_list[i][7]=='Food|Baking|Baking Mixes' or your_list[i][7]=='Household Essentials' and your_list[i][3]!='electronic'):
                        loop3(i,your_list,s,m,l,smax,mmax,lmax,roomcapacity,sroom,a,b)
def number_density_distribution(TimeStep,NOAtoms,XX,YY,ZZ):
    try:
        with open(str(TimeStep)+'.dat','w') as out:
            print('ZONE I=70, J=60, F=POINT',file=out)
            dj=1/60
            dk=1/70
            for j in range(1,61):
                for k in range(1,71):
                    count=0;
                    for n in range(NOAtoms):
                        if ((j-1)*dj<=YY[n]<=j*dj and (k-1)*dk<=ZZ[n]<=k*dk):
                            count=count+1
                    print((k-0.5)*dj,(j-0.5)*dj,count,file=out)
    except IOError as err:
        print('File Error:'+str(err))

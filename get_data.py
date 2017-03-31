def get_data(file):
    global TimeStep
    global NOAtoms
    global XX
    global YY
    global ZZ
    AID=[]
    ATYPE=[]
    XX=[]
    YY=[]
    ZZ=[]
    try:
        with open(file) as data:
            AllLine=data.readlines()
            TimeStep=int(AllLine[1])
            NOAtoms=int(AllLine[3])
            XLH=AllLine[5]
            (xl,xh)=XLH.split()
            YLH=AllLine[6]
            (yl,yh)=YLH.split()
            ZLH=AllLine[7]
            (zl,zh)=ZLH.split()
            ATOMSdata=AllLine[9:]
            for each_line in ATOMSdata:
                try:
                 (atomid,atomtype,x,y,z)=each_line.split(' ',4)
                 AID.append(int(atomid))
                 ATYPE.append(int(atomtype))
                 XX.append(float(x))
                 YY.append(float(y))
                 ZZ.append(float(z))
                except ValueError:
                    pass
    except IOError as err:
        print('File Error:'+str(err))

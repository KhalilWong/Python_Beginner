def get_data(file):                                                         #读取dump出的单个时间步的数据
    global TimeStep                                                         #定义全部局变量，等同于函数Return值
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
            TimeStep=int(AllLine[1])                                        #时间步
            NOAtoms=int(AllLine[3])                                         #原子总数
            XLH=AllLine[5]
            (xl,xh)=XLH.split()                                             #X方向边界
            YLH=AllLine[6]
            (yl,yh)=YLH.split()                                             #Y方向边界
            ZLH=AllLine[7]
            (zl,zh)=ZLH.split()                                             #Z方向边界
            ATOMSdata=AllLine[9:]                                           #具体原子数据
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

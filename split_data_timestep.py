def split_data_timestep(file):
    line=''
    try:
        with open(file) as bdata:
            for each_line in bdata:
                line+=each_line                                                #所有行数据串成一个字符串
            sdata=line.split('ITEM: TIMESTEP')                                 #按时间步分割字符串
            del sdata[0]
            l=len(sdata)
    except IOError as err:
        print('File Error:'+str(err))

    for i in range(l):
        try:
            with open(str(i)+'.split','w') as out:
                print(sdata[i],file=out)                                       #按时间步生成多个数据文件
        except IOError as err:
            print('File Error:'+str(err))

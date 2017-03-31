line=''
try:
    with open('bigdata.test') as bdata:
        for each_line in bdata:
            line+=each_line
        sdata=line.split('ITEM: TIMESTEP')
        del sdata[0]
        l=len(sdata)
except IOError as err:
    print('File Error:'+str(err))

for i in range(l):
    try:
        with open(str(i)+'.test','w') as out:
            print(sdata[i],file=out)
        get_data(str(i)+'.test')
        shumidu(TimeStep,NOAtoms,XX,YY,ZZ)
    except IOError as err:
        print('File Error:'+str(err))

import exrex

names = ['LIXING','LiXing','lixing','Lixing','LX','lx','Lix','Lx','Lxing','lxing','lXing']
birthday = ['19981201','1998121','981201','98121','121','1201']

f_dic = open('namedic.txt','w')
f_dic.close()
for name in names:
    for birth in birthday:
        dics = list(exrex.generate('(|{name})(|[!@#$&*])(|[!@#$&*])(|{birth})'.format(name=name,birth= birth)))
        for dic in dics:
            if len(dic)>=6:
                f_dic = open('namedic.txt','a')
                f_dic.write(dic+'\n')
            f_dic.close()
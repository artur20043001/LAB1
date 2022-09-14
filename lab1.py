import csv
count=-1
count1=0
flag =0
janrs=[]
janrs1=''
dic={}
search = input("автор ")
f = open('result.txt', "w")
with open('books.csv', "r") as csvfile:
    table = csv.reader(csvfile, delimiter = ";")
    for row in list(table):
        if count>=0:
            dic[row[1]]=dic.setdefault(row[1],0)+int(row[8])
        fl1=False
        janre=''
        for i in row[12]:
            if i=='#':
                if janre!='' and janre not in janrs and fl1==True:
                    janrs.append(janre)
                    janrs1+=janre+'\n'
                janre=''
                fl1=True
            else:
                janre+=i
        if janre!='' and janre not in janrs and fl1==True:
            janrs.append(janre)
            janrs1+=janre+'\n'
            janre=''
        count+=1
        lower_case = row[3].lower()
        index = lower_case.find(search.lower())
        if len(row[1])>30:
            count1+=1
        if 1<=count<=20:
            f.write(row[4]+'. '+row[1]+' - '+row[6][:4]+'\n')
        if index != -1 and int(row[6][:4])<2016:
            flag = 1
            f.write(row[1]+'\n')
    if flag == 0:
        f.write('Ничего не найдено'+'\n')
    f.write(str(count)+'\n')
    f.write(str(count1)+'\n')
    f.write(janrs1)
    co=0
    sorted_books = dict(sorted(dic.items(), key=lambda item: item[1],reverse=True))
    for key in sorted_books:
        if co<20:
            f.write(key+'\n')
        co+=1

    f.close()

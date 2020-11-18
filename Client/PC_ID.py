def file_read() :
    fr = open('PC_ID.txt','r')
    ID = fr.read()
    if ID == 'temp':
        ID = 'unknown'

    elif ID=='0':
        print('파일에 내용이 없습니다')

    fr.close()

    return ID

def file_modify(text) :
    fw = open('PC_ID.txt','w')
    fw.write(text)

    fw.close()

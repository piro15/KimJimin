try:
    file =open('maria.txt','r')
except FileNotFOundError:
    print('파일이 없습니다.')
else:
    s=file.read()
    file.close()

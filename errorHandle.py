file = open('trywriting.txt','w')
file.write('Try writing to this file in read mode')
file.close()

try: 
    file = open('trywriting.txt','r')
    file.write('Add this content to this file')
    file.close()
except Exception as e:
    print(e)
finally:
    print('I will write into this file')

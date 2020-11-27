import sys

# try:
#     with open('myfile.txt') as file:
#         data = file.read()   
#     print(data)
# except FileNotFoundError:
#     print('The file is not found.')
# except PermissionError:
#     print('This is not allowed.')
# except:
#     print('some other error occured.')
    
class MyException(Exception):
    pass

try:
    1/0
except:
    err = sys.exc_info()
    for e in err:
        print(e)


from datetime import datetime

def say_hi():
    '''
    to say hi only
    '''
    msg ='Hello World ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(msg)
    return msg

if __name__ == '__main__':
    say_hi()
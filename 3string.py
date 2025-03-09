def length(user):
    lengths=len(user)
    print('the length of your string is',lengths)
    return lengths

def letterbyletter(var):
    
    index = 0
    
    while index < len(var):
        letter=var[index]
        print(letter)
        index = index + 1
    return index 

def main():
    user=input('enter a string: ')
    lengthss=length(user)
    letterbyletter(user)
    print(lengthss)
    return
if __name__ == '__main__':
    main()
    
def code():
    import random 
    import string
    # name = input("Enter the message to code:")
    # if name.lower() == 'code':
        # key = int(input("Enter your key :"))
        # code = int(input("Enter the coding number:"))
    a= input("Enter the message to code:")
    def random_char(y):
        return ''.join(random.choice(string.ascii_letters) for x in range(y))
    rev = ''
    for i in a.split():
        if len(i)<=3:
            rev= rev + " " + (i[::-1])
        else:
            rev= rev + " " + (random_char(3)+i[1::]+i[0]+random_char(3))

    print("Encoded message is:",rev)
    

def decode():
    decode = input("Enter the message to decode")
    # key2 = int(input("Enter the key for decrypting:"))
    # if key ==key2:
    sol = ''
    for word in decode.split():
        if len(word)<=3:
            sol = sol + " " + word[::-1]
        else:
             sol = sol + " " + (word[-4]+word[3:-4])

    print('Your decoded message is:', sol)
        # else:
        #     print("Sorry key for decrypting is wrong")
        # name = input("Hi welcome, do you want to code or decode:")


i = int(input("Enter 0 for code, 1 for decode and 2 for quit:"))
if i ==0:
    code()
elif i == 1:
    decode()
    
while i!=2:
    i = int(input("Enter 0 for code, 1 for decode and 2 for quit:"))
    if i ==0:
                  code()
    elif i == 1:
                  decode()
    
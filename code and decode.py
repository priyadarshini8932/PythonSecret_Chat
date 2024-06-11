def code():
    import random 
    import string
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
    sol = ''
    for word in decode.split():
        if len(word)<=3:
            sol = sol + " " + word[::-1]
        else:
             sol = sol + " " + (word[-4]+word[3:-4])

    print('Your decoded message is:', sol)

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
    

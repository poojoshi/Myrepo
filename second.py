
'''
def custom():
    print("this is a custom function")



def convert_currency(param):
    amount=527*param
    print(amount, "this is the converted value")

custom()
convert_currency(1)


for k in range(10):
    if k%2 is 0 :
        print("it is even number",k)
    else:
        print(" the number is odd" , k)




def custom_func(age):
    my_age= age/2+7
    return my_age

buckys_age=custom_func(22)
print("buckys age is : ", buckys_age)


def get_validation(value='unknown'):
    if value is 'm' :
        print("male")
    elif value is 'f' :
        print("female")
    else:
        print("unknown")

get_validation('m')
get_validation('f')
get_validation()


def fun_A():
    a=2548
    print(a)

def fun_B():
    print(a)

fun_A()
fun_B()




def F1(name='pooja', action='is' , item='awesome'):
    print(name,action,item)


F1('all','are','awesome')
F1(name='tuna')
'''
'''

def Fun_A(*args):
    total=0
    for n in args:
        total=total + n
    print(total)

Fun_A(10)
Fun_A(10,20)
    
'''

'''
#classmates={'mango', 'apple','watermelon','mango'}
#print(classmates)

classmates={'Tony':' is cool', 'sammy':' bites','lauren':' is nice'}


#print(classmates['Tony'])


for k,v in classmates.items():
    print(k + v)

    '''
def display():
    print("i am fine")

display()



































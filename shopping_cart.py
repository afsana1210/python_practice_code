from IPython.display import clear_output


cart=[]

def addItem(item):
    clear_output()
    cart.append(item)
    print('{} has been added'.format(item))

def removeItem(item):
    clear_output()
    try:
        cart.remove(item)
        print('{} has been remove'.format(item))
    except:
        print('sorry we could not remove that item')

def showcart():
    clear_output()
    if cart:
        print('here is your cart')
        for item in cart:
            print('-{}'.format(item))
    else:
        print('your cart is empty')

def clearCart():
    clear_output()
    cart.clear()
    print('your cart is empty')

def main():
    done=False

    while not done:
        ans=input('quit/add/remove/show/clear : ').lower()
        if ans=='quit':
            print('thanks for using our program')
            showcart()
            done=True
        elif ans=='add':
            item= input('what would you like to add').title()
            addItem(item)
        elif ans=='remove':
            showcart()
            item= input('what would you like to remove').title()
            removeItem(item)
        elif ans=='show':
            showcart()
        elif ans=='clear':
            clearCart()
        else:
            print('sorry this is  not an option')

main()
          
           
          
          




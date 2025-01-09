from .models import Cart, CartItem



def cart_item_detail(id):
    return CartItem.objects.get(id=id)

def get_cart(user):
    Cart.objects.get(user=user)
    

def cart_item_list(cart):
    return CartItem.objects.filter(cart=cart)
    


    
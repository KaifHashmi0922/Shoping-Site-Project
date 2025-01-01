from django import template
register=template.Library()


@register.filter
def Currency(value):
    return "₹"+str(int(value))

@register.filter
def cart_status(product,cart):
    ks=cart.keys()
    for k in ks:
        if int(k)==product.id:
            return True
    return False 

@register.filter
def cart_quantity(product,cart):
    ks=cart.keys()
    for k in ks:
        if int(k)==product.id:
            return cart.get(k)
    return 0

@register.filter
def total_price(product,cart):
    return product.price*cart_quantity(product,cart)    

@register.filter
def grand_total(prods,cart):
    s=0
    for p in prods:
        s=s+total_price(p,cart)
    return s    



from django.shortcuts import render, redirect
from .models import CartItem
from shop.models import Products


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Products.objects.get(pk=product_id)
        user = request.user
        quantity = int(request.POST.get('quantity', 1))
        cart_item, created = CartItem.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart/cart_detail.html', {'cart_items': cart_items,'total_price': total_price})


        



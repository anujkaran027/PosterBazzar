from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

from .models import Cart, CartItem
from shop.models import products


def get_or_create_cart(request):
    """Get or create cart for user or session"""
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart


def add_to_cart(request, product_id):
    """Add product to cart"""
    if request.method == 'POST':
        try:
            product = get_object_or_404(products, id=product_id)
            cart = get_or_create_cart(request)
            
            # Get quantity from POST data
            quantity = int(request.POST.get('quantity', 1))
            
            # Check if item already exists in cart
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )
            
            if not created:
                # Update quantity if item already exists
                cart_item.quantity += quantity
                cart_item.save()
            
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Content-Type', ''):
                return JsonResponse({
                    'success': True,
                    'message': f'{product.name} added to cart',
                    'cart_total': cart.total_items,
                    'cart_price': cart.total_price
                })
            else:
                messages.success(request, f'{product.name} added to cart')
                return redirect('cart:cart_detail')
                
        except Exception as e:
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Content-Type', ''):
                return JsonResponse({
                    'success': False,
                    'message': 'Error adding item to cart'
                })
            else:
                messages.error(request, 'Error adding item to cart')
                return redirect('shop:product_detail', product_id=product_id)
    
    return redirect('shop:product_detail', product_id=product_id)


def remove_from_cart(request, item_id):
    """Remove item from cart"""
    if request.method == 'POST':
        try:
            cart_item = get_object_or_404(CartItem, id=item_id)
            cart = cart_item.cart
            
            # Check if user owns this cart
            if request.user.is_authenticated:
                if cart.user != request.user:
                    messages.error(request, 'You do not have permission to modify this cart')
                    return redirect('cart:cart_detail')
            else:
                if cart.session_key != request.session.session_key:
                    messages.error(request, 'You do not have permission to modify this cart')
                    return redirect('cart:cart_detail')
            
            product_name = cart_item.product.name
            cart_item.delete()
            
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Content-Type', ''):
                return JsonResponse({
                    'success': True,
                    'message': f'{product_name} removed from cart',
                    'cart_total': cart.total_items,
                    'cart_price': cart.total_price
                })
            else:
                messages.success(request, f'{product_name} removed from cart')
                return redirect('cart:cart_detail')
                
        except Exception as e:
            # Check if this is an AJAX request
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest' or 'application/json' in request.headers.get('Content-Type', ''):
                return JsonResponse({
                    'success': False,
                    'message': 'Error removing item from cart'
                })
            else:
                messages.error(request, 'Error removing item from cart')
                return redirect('cart:cart_detail')
    
    return redirect('cart:cart_detail')


def update_cart_item(request, item_id):
    """Update cart item quantity"""
    if request.method == 'POST':
        try:
            cart_item = get_object_or_404(CartItem, id=item_id)
            cart = cart_item.cart
            
            # Check if user owns this cart
            if request.user.is_authenticated:
                if cart.user != request.user:
                    return JsonResponse({
                        'success': False,
                        'message': 'You do not have permission to modify this cart'
                    })
            else:
                if cart.session_key != request.session.session_key:
                    return JsonResponse({
                        'success': False,
                        'message': 'You do not have permission to modify this cart'
                    })
            
            quantity = int(request.POST.get('quantity', 1))
            
            if quantity <= 0:
                cart_item.delete()
                return JsonResponse({
                    'success': True,
                    'message': 'Item removed from cart',
                    'cart_total': cart.total_items,
                    'cart_price': cart.total_price,
                    'item_removed': True
                })
            else:
                cart_item.quantity = quantity
                cart_item.save()
                
                return JsonResponse({
                    'success': True,
                    'message': 'Cart updated',
                    'cart_total': cart.total_items,
                    'cart_price': cart.total_price,
                    'item_total': cart_item.total_price,
                    'item_removed': False
                })
                
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Error updating cart'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })


def cart_detail(request):
    """Display cart contents"""
    cart = get_or_create_cart(request)
    cart_items = cart.cartitem_set.all()
    
    context = {
        'cart': cart,
        'cart_items': cart_items,
        'total_items': cart.total_items,
        'total_price': cart.total_price,
        'total_discount': cart.total_discount,
    }
    
    return render(request, 'cart/cart_detail.html', context)


def cart_count(request):
    """Get cart item count for AJAX requests"""
    cart = get_or_create_cart(request)
    return JsonResponse({
        'count': cart.total_items
    })


@csrf_exempt
def ajax_add_to_cart(request, product_id):
    """AJAX endpoint for adding items to cart"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product = get_object_or_404(products, id=product_id)
            cart = get_or_create_cart(request)
            
            quantity = int(data.get('quantity', 1))
            
            cart_item, created = CartItem.objects.get_or_create(
                cart=cart,
                product=product,
                defaults={'quantity': quantity}
            )
            
            if not created:
                cart_item.quantity += quantity
                cart_item.save()
            
            return JsonResponse({
                'success': True,
                'message': f'{product.name} added to cart',
                'cart_total': cart.total_items,
                'cart_price': cart.total_price,
                'product_name': product.name
            })
            
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': 'Error adding item to cart'
            })
    
    return JsonResponse({
        'success': False,
        'message': 'Invalid request method'
    })
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ReviewRating, ProductGallery
from category.models import Category
from cart.models import CartItem
from cart.views import _cart_id
from django.core.paginator import *
from.forms import Reviewform
from orders.models import OrderProduct
from accounts.models import UserProfile
from django.views.generic.edit import UpdateView,DeleteView
from . forms import ProductForm

def seller_profile(request,id):
    seller = User.objects.get(id=id,)
    context ={
        'seller':seller,
    }
    return render(request, 'store/seller_profile.html',context)

def storeview(request, cat_slug=None):
    category = None
    products =None
    product_count = 0
    categories = None
    if cat_slug != None:
        categories = get_object_or_404(Category, cat_slug=cat_slug)
        products = Product.objects.filter(category=categories).order_by('-created_date')
        product_count = products.count()
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    else:
        products = Product.objects.all().filter(is_available=True).order_by('-created_date')
        product_count = products.count()
        paginator = Paginator(products, 6)
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)
    context = {
        'products': paged_products,
        'product_count': product_count,
        'category': categories,
        
        
    }
    return render(request, 'store/store.html', context)


def productDetail(request, slug, cat_slug):
    try:
        product = Product.objects.get(category__cat_slug=cat_slug, slug=slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=product)
    except Exception as e:
        raise e

    if request.user.is_authenticated:
        try:
            orderproduct = OrderProduct.objects.filter(user=request.user, product_id=product.id).exists()

        except OrderProduct.DoesNotExist:
            orderproduct = None
    else:
        orderproduct = None
    # get reviews

    reviews = ReviewRating.objects.filter(product__id=product.id, status=True)
    # get product gallery

    product_gallery = ProductGallery.objects.filter(product_id=product.id)
    context = {
        'product': product,
        'in_cart': in_cart,
        'orderproduct': orderproduct,
        'reviews': reviews,
        'product_gallery': product_gallery
    }
    return render(request, 'store/product-detail.html', context)


def searchview(request):
    products = None
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            products = Product.objects.order_by('created_date').filter(Q(product_name__icontains=query) | Q(description__icontains=query))
            product_count = products.count()
            if products.count() == 0:
                messages.warning(request, f'No search results with \'{query}\' found.')
            else:
                messages.success(request, f'{product_count} items found.')
    context = {
        'products': products,
    }
    return render(request, 'store/store.html', context)


def reviewview(request, product_id):
    url = request.META.get('HTTP_REFERER')
    user = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user=user, product__id=product_id)
            form = Reviewform(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = Reviewform(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you, review has been submitted.')
                return redirect(url)



def addproducts(request):
    form = ProductForm()

    if request.method =='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect('store')
    else:
        form = ProductForm()

    context = {
        "form":form
    }
    return render(request, 'store/addproducts.html', context)

def delete_product(request,id):
    product = Product.objects.get(id=id)
    context={
        'product':product,
    }
    if request.method =='POST':
        product.delete()
        return redirect('store')
    return render (request,'store/delete.html',context)


def my_listings(request):
        products = Product.objects.filter(seller_name=request.user)
        context ={
            'products':products,
        }
        return render(request,'store/mylistings.html',context)


class ProductUpdateView(UpdateView):
    model = Product
    fields = ['category','product_name','slug','description','product_specifications','price','old_price','is_available','image']
    template_name = 'store/product_update.html'



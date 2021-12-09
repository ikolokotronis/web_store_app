from django.shortcuts import render, redirect
from django.views import View
from .models import Category, SubCategory, CategorySubCategory, ShoppingCart, Order
from products.models import Product
from datetime import date, timedelta
from users.models import WebsiteUser
# Create your views here.


class HomePageView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True)[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today())[0:3]
        return render(request, 'main/base.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories}
                      )

    def post(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        all_categories = SubCategory.objects.all()
        bestsellers = Product.objects.filter(is_bestseller=True)[0:3]
        added_recently = Product.objects.filter(date_added__gte=date.today() - timedelta(days=3),
                                                date_added__lte=date.today())[0:3]
        key_word = request.POST.get('key_word')
        product_results = Product.objects.filter(name__icontains=key_word)
        category_results = Category.objects.filter(name__icontains=key_word)
        subcategory_results = SubCategory.objects.filter(name__icontains=key_word)
        return render(request, 'main/search_results.html', {'stringed_instruments': stringed_instruments,
                                                  'keyboard_instruments': keyboard_instruments,
                                                  'drums': drums,
                                                  'sound_system': sound_system,
                                                  'bestsellers': bestsellers,
                                                  'added_recently': added_recently,
                                                  'all_categories': all_categories,
                                                  'product_results': product_results,
                                                  'category_results': category_results,
                                                  'subcategory_results': subcategory_results}
                      )


class CategoryDetailsView(View):
    def get(self, request, category_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        subcategories = SubCategory.objects.filter(category_id=category_id)
        parent_category = CategorySubCategory.objects.filter(category_id=category_id)[0]
        return render(request, 'main/category_details.html', {'stringed_instruments': stringed_instruments,
                                                                'keyboard_instruments': keyboard_instruments,
                                                                'drums': drums,
                                                                'sound_system': sound_system,
                                                                'subcategories': subcategories,
                                                                'parent_category': parent_category}
                      )


class SubCategoryView(View):
    def get(self, request, subcategory_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        products = Product.objects.filter(subcategory_id=subcategory_id)
        parent_category = CategorySubCategory.objects.filter(subcategory_id=subcategory_id)[0]
        return render(request, 'main/subcategory_details.html', {'stringed_instruments': stringed_instruments,
                                                              'keyboard_instruments': keyboard_instruments,
                                                              'drums': drums,
                                                              'sound_system': sound_system,
                                                              'products': products,
                                                              'parent_category': parent_category})


class ContactView(View):
    def get(self, request):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        return render(request, 'main/contact.html', {'stringed_instruments': stringed_instruments,
                                                                 'keyboard_instruments': keyboard_instruments,
                                                                 'drums': drums,
                                                                 'sound_system': sound_system})


class ShoppingCartView(View):
    def get(self, request, user_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
        products_summary = sum(product.product.price * product.quantity for product in shopping_cart_list)
        return render(request, 'main/shoppingCart.html', {'stringed_instruments': stringed_instruments,
                                                     'keyboard_instruments': keyboard_instruments,
                                                     'drums': drums,
                                                     'sound_system': sound_system,
                                                     'shopping_cart_list': shopping_cart_list,
                                                     'products_summary': products_summary})
    def post(self, request, user_id):
        ShoppingCart.objects.all().delete()
        return redirect(f'/shopping_cart/{user_id}/')


class ShoppingCartCheckoutView(View):
    def get(self, request, user_id):
        stringed_instruments = Category.objects.get(id=1)
        keyboard_instruments = Category.objects.get(id=2)
        drums = Category.objects.get(id=3)
        sound_system = Category.objects.get(id=4)
        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)
        products_summary = sum(product.product.price*product.quantity for product in shopping_cart_list)
        return render(request, 'main/shoppingCart_checkout.html', {'stringed_instruments': stringed_instruments,
                                                          'keyboard_instruments': keyboard_instruments,
                                                          'drums': drums,
                                                          'sound_system': sound_system,
                                                          'shopping_cart_list': shopping_cart_list,
                                                          'products_summary': products_summary})
    def post(self, request, user_id):
        post_shipping_type = request.POST.get('shipping_type')
        shipping_type = 0
        if post_shipping_type == 'pickup_in_person':
            shipping_type = 1
        elif post_shipping_type == 'home_shipping':
            shipping_type = 2

        shopping_cart_list = ShoppingCart.objects.filter(user_id=user_id)

        products = [product.product for product in shopping_cart_list]
        quantity = [product.quantity for product in shopping_cart_list]
        product = Product.objects.get(id=products.id)
        user = WebsiteUser.objects.get(id=user_id)
        Order.objects.create(quantity=quantity, shipping_type=shipping_type,
                             product=product, user=user)
        return redirect('/')


class ShoppingCartRemoveProductView(View):
    def get(self, request, user_id, product_id):
        cart_item = ShoppingCart.objects.get(user_id=user_id, product_id=product_id)
        cart_item.delete()
        return redirect(f'/shopping_cart/{user_id}/')

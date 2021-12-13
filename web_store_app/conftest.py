from main.models import Category, SubCategory, CategorySubCategory, ShoppingCart, Order
from products.models import Product, SubCategoryProduct
from users.models import WebsiteUser

import pytest


@pytest.fixture
def example_product():
    return Product.objects.create(
            name='Product 1',
            description='Product description 1',
            price=100,
            is_bestseller=True,
            rating='3')


@pytest.fixture
def example_category():
    return Category.objects.create(
            name='Category 1',
            description='Category description 1')


@pytest.fixture
def example_subcategory():
    return SubCategory.objects.create(
            name='Subcategory 1',
            description='Subcategory description 1')


@pytest.fixture
def example_product_subcategory_relation():
    return SubCategoryProduct.objects.create(
            product=Product.objects.first(),
            subcategory=SubCategory.objects.first())


@pytest.fixture
def example_category_subcategory_relation():
    return CategorySubCategory.objects.create(
            category=Category.objects.first(),
            subcategory=SubCategory.objects.first())


@pytest.fixture
def example_website_user():
    return WebsiteUser.objects.create_user(
        username='test_user',
        password='test_password',
        first_name='User first name',
        last_name='User last name',
        email='test_email@test.com',
        address='test address',
        wallet=500,
        phone_number=123456789
    )


@pytest.fixture
def example_shopping_cart():
    return ShoppingCart.objects.create(
        product=Product.objects.first(),
        user=WebsiteUser.objects.first()
    )


@pytest.fixture
def example_order():
    return Order.objects.create(
        user=WebsiteUser.objects.first(),
        amount_paid=100,
        status=1,
        shipping_type=1,
        payment_type=1,
        address='test_address',
        phone_number=123456789
    )


@pytest.fixture
def create_products():
    return [
        Product.objects.create(
            name='Product 1',
            description='Product description 1',
            rating='3'),

        Product.objects.create(
            name='Product 2',
            description='Product description 2',
            rating='4'),
        Product.objects.create(
            name='Product 3',
            description='Product description 3',
            rating='5'),
    ]


@pytest.fixture
def create_categories():
    return [
        Category.objects.create(
            name='First category',
            description='First description'),

        Category.objects.create(
            name='Second category',
            description='Second description',
        ),
    ]
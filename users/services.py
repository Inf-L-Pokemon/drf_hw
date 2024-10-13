import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(obj):
    """Создаёт продукт в Stripe"""

    product_object = obj.paid_course if obj.paid_course else obj.paid_lesson
    product = stripe.Product.create(name=product_object.title, description=product_object.description)
    return product.id


def create_stripe_price(amount, product_id):
    """Создаёт цену продукта в Stripe"""

    price = stripe.Price.create(
        currency="rub",
        unit_amount=int(amount) * 100,
        product=product_id,
    )
    return price.id


def create_stripe_session(price_id):
    """Создаёт сессию на оплату в Stripe"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/course/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session.id, session.url

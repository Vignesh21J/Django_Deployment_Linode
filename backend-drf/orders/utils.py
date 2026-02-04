from django.conf import settings
from django.core.mail import send_mail

def send_order_notification(order):
    send_mail(
        subject=f'Order Confirmation - #{order.id}',
        message=f""" 
            Hi {order.user.username},

            Your Order #{order.id} has been placed successfully.

            Order ID: {order.id}
            Subtotal: {order.subtotal}
            Tax: {order.tax_amount}
            Grand Total: {order.grand_total}

            We will notify you once your order is shipped.

            Thank you for shopping with us,
            Team ClickMart
        """,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[order.user.email],
        fail_silently=False
    )
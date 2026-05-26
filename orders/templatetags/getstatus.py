from django import template
register = template.Library()
@register.filter(name='getstatus')
def getstatus(order):
    try:
        status_code = int(order.order_status) 
        index = status_code - 1
        status_array = ['Order Confirmed', 'Order Processed', 'Delivered', 'Rejected']
        return status_array[index]
    except (AttributeError, ValueError, IndexError, TypeError):
        return "Unknown Status"

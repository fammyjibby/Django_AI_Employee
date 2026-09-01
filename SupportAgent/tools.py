from orders.models import Order,RefundRequest
from django.utils import timezone
from .tracking_data import DELIVERY_DATA

def get_order_by_id(order_id):
    try:
        order =Order.objects.get(id=order_id)
        return {
            "id": order.id,
            "prduct_name": order.product_name,
            "status": order.status,
            "amount": order.amount,
            "carrier": order.carrier,
            "tracking_number": order.tracking_number,
            "delivery_address": order.delivery,
            "order_date": order.created_at.strftime("%d-%m-%Y %H:%M:%S"),
            "days_since_order": (timezone.now() - order.created_at).days 

        }

    except Order.DoesNotExist:
        return { "error": f"Order with id {order_id} does not exist or not found."}

def get_refund_history(user_id):
        refund = RefundRequest.objects.filter(user_id=user_id).order_by('-created_at')
        history = []
        for refund in refund:
            history.append({
                "order_id": refund.order.id,
                "product_name": refund.order.product_name,
                "reason": refund.reason,
                "status": refund.status,
                "request_date": refund.created_at.strftime("%d-%m-%Y %H:%M:%S"),
            })
            return {
                "total_refund_requests": len(history),
                "refund_history": history
            }

def check_delivery_status(tracking_number,carrier):
     default_response = {
         "status": "Tracking number not found",
         "last_location": None,
         "last_update": None,
         "estimated_delivery": "contact carrier for more information",
         "delay_reason": "No information available",
     }
     result = DELIVERY_DATA.get(tracking_number,default_response)
     result["tracking_number"] = tracking_number
     result["carrier"] = carrier
     return result
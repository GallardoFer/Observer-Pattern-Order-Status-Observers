from .customer_notifier import CustomerNotifier
from .audit_observer import AuditObserver
class OrderStatus:
    def __init__(self,order_id,customer_notifier: CustomerNotifier,audit_observer: AuditObserver):
        self.order_id=order_id; self.status="NEW"
        self.customer_notifier=customer_notifier; self.audit_observer=audit_observer
    def set_status(self,status):
        self.status=status
        self.customer_notifier.notify_customer(self.order_id,status)
        self.audit_observer.record(self.order_id,status)

from order_status.customer_notifier import CustomerNotifier
from order_status.audit_observer import AuditObserver
from order_status.order_status import OrderStatus
def test_direct_calls():
    c=CustomerNotifier(); a=AuditObserver(); o=OrderStatus("A-100",c,a)
    o.set_status("SHIPPED")
    assert c.messages==["A-100:SHIPPED"]
    assert a.entries==[("A-100","SHIPPED")]

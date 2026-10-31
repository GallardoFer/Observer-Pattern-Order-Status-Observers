from order_status.analytics_observer import AnalyticsObserver
from order_status.audit_observer import AuditObserver
from order_status.customer_notifier import CustomerNotifier
from order_status.order_status import OrderStatus


def test_subscribed_observers_are_notified_and_unsubscribed_ones_are_not():
    customer, audit, analytics = CustomerNotifier(), AuditObserver(), AnalyticsObserver()
    order = OrderStatus("A-100")
    for observer in (customer, audit, analytics):
        order.subscribe(observer)

    order.set_status("SHIPPED")
    order.unsubscribe(customer)
    order.set_status("DELIVERED")

    assert customer.messages == ["A-100:SHIPPED"]
    assert audit.entries == [("A-100", "SHIPPED"), ("A-100", "DELIVERED")]
    assert analytics.status_counts == {"SHIPPED": 1, "DELIVERED": 1}

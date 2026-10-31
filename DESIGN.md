# Observer Pattern — Order Status Observers

**Modified by:** Fernando Gallardo Romero

## Subject / Observer structure

- **Observer (contract):** `Observer` (`src/order_status/observer.py`) — abstract class with one method: `update(order_id, status)`.
- **Subject:** `OrderStatus` — keeps its own state and a list of subscribers. It exposes `subscribe(observer)`, `unsubscribe(observer)`, and calls `update()` on every subscriber inside `_notify()` whenever `set_status()` changes the state. It no longer knows any concrete receiver; it depends only on the `Observer` abstraction.
- **Concrete Observers:**
  - `CustomerNotifier` — stores customer messages like `"A-100:SHIPPED"`.
  - `AuditObserver` — stores audit entries like `("A-100", "SHIPPED")`.
  - `AnalyticsObserver` — counts how many times each status happened.

Before, `OrderStatus` received `CustomerNotifier` and `AuditObserver` in its constructor and called `notify_customer()` and `record()` directly. Now both classes implement `Observer.update()` and are attached at runtime with `subscribe()`.

## `AnalyticsObserver` added without changing Subject notification logic

`AnalyticsObserver` is a new file that only implements `Observer`. To use it, the client just calls `order.subscribe(AnalyticsObserver())`. Nothing in `OrderStatus` (`set_status`, `_notify`) had to change to support it, so the Subject is open for extension and closed for modification.

Subscription and unsubscription are supported: `subscribe()` ignores duplicates, `unsubscribe()` ignores observers that are not subscribed, and `_notify()` iterates over a copy of the list so an observer can safely unsubscribe during a notification.

## Focused test

`tests/test_order_status_observers.py` subscribes the three observers to order `A-100`, changes the status to `SHIPPED`, unsubscribes `CustomerNotifier`, and changes the status to `DELIVERED`. It checks that:

- `CustomerNotifier` only received `SHIPPED` (it was unsubscribed before `DELIVERED`),
- `AuditObserver` received both changes,
- `AnalyticsObserver` counted `{"SHIPPED": 1, "DELIVERED": 1}`.

The old `tests/test_baseline.py` was removed because it tested the direct-call constructor that no longer exists. Run with `pytest -q`.

## Design explanation / lifecycle or coupling cost

Observer removes the compile-time coupling between `OrderStatus` and its receivers: the Subject only knows the `Observer` interface, and new reactions (like analytics) are added by subscribing a new class. The cost moves to the **lifecycle**: someone outside the Subject now has to remember to subscribe each observer and, just as important, to unsubscribe it when it is no longer needed. If that is forgotten, the Subject keeps a reference to the observer, so it keeps receiving updates and cannot be garbage-collected (the "lapsed listener" problem). There is also hidden, implicit coupling: from `OrderStatus` alone you cannot see who will react to a status change or in what order, so the full behavior only exists at runtime. That makes debugging harder, and if one observer raises an exception, the observers after it in the list are not notified.

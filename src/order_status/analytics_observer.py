from .observer import Observer


class AnalyticsObserver(Observer):
    """New observer added without touching OrderStatus: counts each status."""

    def __init__(self):
        self.status_counts: dict[str, int] = {}

    def update(self, order_id: str, status: str) -> None:
        self.status_counts[status] = self.status_counts.get(status, 0) + 1

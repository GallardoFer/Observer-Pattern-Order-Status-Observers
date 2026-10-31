from abc import ABC, abstractmethod


class Observer(ABC):
    """Contract every OrderStatus subscriber must follow."""

    @abstractmethod
    def update(self, order_id: str, status: str) -> None:
        raise NotImplementedError

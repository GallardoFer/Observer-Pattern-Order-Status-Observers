class CustomerNotifier:
    def __init__(self): self.messages=[]
    def notify_customer(self,order_id,status): self.messages.append(f"{order_id}:{status}")

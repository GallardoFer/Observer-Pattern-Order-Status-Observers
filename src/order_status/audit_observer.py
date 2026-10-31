class AuditObserver:
    def __init__(self): self.entries=[]
    def record(self,order_id,status): self.entries.append((order_id,status))

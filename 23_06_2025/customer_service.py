'''
write a python program to create a customer service by 
1.adding a customer into the queue and 
2.once the custumer is served he has to be removed from the queue.

'''
class CustomerService:
    def __init__(self):
        self.queue = []
    def add_customer(self, customer_name):
        self.queue.append(customer_name)
        print(f"{customer_name} has been added to the queue.")
    def serve_customer(self):
        if not self.is_empty():
            served = self.queue.pop(0)
            print(f"{served} has been served and removed from the queue.")
        else:
            print("No customers to serve.")
    def is_empty(self):
        return len(self.queue) == 0
    def display_queue(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("QUEUE:- ", self.queue)
service = CustomerService()
service.add_customer("ruhani")
service.add_customer("madhu")
service.add_customer("sravya")

service.display_queue()
service.serve_customer()
service.display_queue()

service.serve_customer()
service.serve_customer()
service.serve_customer()  


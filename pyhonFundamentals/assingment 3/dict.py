class oneline_store:
    count=0
    def __init__(self,name, price):
        self.name = name
        self.price = price
        oneline_store.count+=1

    def product_info(self):
        print(f"This store sales {self.name} and the price of the product is {self.price} rs")
    @classmethod
    def product_count(cls):
        print(f"The numbers of products are dispacting from the godown is {oneline_store.count}")
    @staticmethod
    def discount(price,percentage):
        print(f"the final price of the product is = {price-(price*percentage/100)}")

product1 = oneline_store("phone",10_000)

product2 = oneline_store("laptop",50_000)

product2.product_info()

product1.product_info()

product2.discount(10_000,10)
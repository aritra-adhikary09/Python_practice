'''Create a class Book with the following attributes:
• title
• author
• list of reviews
And add methods to:
• add a new review
• count reviews
• display all reviews
Concept: Encapsulation'''

class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.reviews = []
        
    def new_review(self,review):
        self.reviews.append(review)
        print("Review add succesfully.")
    
    def count_reviews(self):
        return len(self.reviews)
    
    def all_reviews(self):
        return self.reviews
    

book1 = Book("One pice","Ichihiro Oda")

book1.new_review("very long story!!")
print(book1.count_reviews())
print(book1.all_reviews())


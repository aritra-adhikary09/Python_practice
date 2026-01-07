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
        self.author =author
        self.ListOfReviews = []

    def add_a_new_review(self,review):
        self.ListOfReviews.append(review)
        print("Review add succesfully.")
    
    def count_reviews(self):
        return len(self.ListOfReviews)
    
    def display_all_reviews(self):
        return self.ListOfReviews
    
book1 = Book("Gud marbar 200 t upay","aritra adhikary")

print(book1.display_all_reviews())
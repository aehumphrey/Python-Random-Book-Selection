import random

# List of books with their genres and page counts
books = [
    {"title": "Children of Dune", "genre": "Science Fiction", "pages": 480, "weight": 0.6},
    {"title": "Gormenghast", "genre": "Fantasy", "pages": 505, "weight": 1.1},
    {"title": "The Notary", "genre": "Historical", "pages": 155, "weight": 0.8},
    {"title": "The Inheritance", "genre": "Historical", "pages": 177, "weight": 1.2},
    {"title": "The Tale of the Body Thief", "genre": "Horror", "pages": 464, "weight": 0.9},
    {"title": "The Fairies in Tradition and Literature", "genre": "Nonfiction", "pages": 352, "weight": 0.9},
    {"title": "The Good Soldier", "genre": "Classics", "pages": 368, "weight": 1.2},
    {"title": "The Return of the Soldier", "genre": "Classics", "pages": 112, "weight": 1.0},
    {"title": "Lud-in-the-Mist", "genre": "Fantasy", "pages": 239, "weight": 1.3}
]

def select_books():
    # Shuffle the list of books to randomize selection
    random.shuffle(books)
    
    selected_books = []
    selected_genres = set()
    total_pages = 0
    
    while len(selected_books) < 3:
        # Calculate total weight for normalization
        total_weight = sum(book["weight"] for book in books if book["genre"] not in selected_genres)
        
        # Randomly select a book with weighted probability
        rand = random.uniform(0, total_weight)
        cumulative_weight = 0
        
        for book in books:
            if book["genre"] in selected_genres:
                continue
            
            cumulative_weight += book["weight"]
            
            if rand < cumulative_weight:
                selected_book = book
                break
        
        # Check if the selected book's genre is already chosen
        if selected_book["genre"] in selected_genres:
            continue
        
        # Check if adding this book exceeds the page count limit
        if total_pages + selected_book["pages"] > 800:
            continue
        
        # Add the book to the selected list
        selected_books.append(selected_book)
        selected_genres.add(selected_book["genre"])
        total_pages += selected_book["pages"]
        
    return selected_books

# Function to check if the selected books satisfy the page count criteria
def check_page_count(selected_books):
    total_pages = sum(book["pages"] for book in selected_books)
    return 600 <= total_pages <= 800

# Select 3 books that satisfy the criteria
selected_books = select_books()

# Check if the selected books satisfy the page count criteria
while not check_page_count(selected_books):
    selected_books = select_books()

# Print the selected books
print("Randomly selected books:")
for book in selected_books:
    print(f"- {book['title']} ({book['genre']}, {book['pages']} pages)")


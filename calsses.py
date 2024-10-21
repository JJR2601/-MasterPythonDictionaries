pythonclasses = [
# Product 1
    {
    "Product Name": ["Laptop", "Desk Chair", "Smartwatch", "Notebook", "Running Shoes"],
    "Price": ["750", "100", "200", "5", "80"]
},

# Employee 2
    {
    "Employee Name": ["John Doe", "Jane Smith", "Mark Johnson", "Lisa Wong", "Paul McDonald"],
    "Job Titles": ["Sales", "Human Resources", "IT", "Marketing", "Finance"]
},

# Books 3
    {
    "Book titles": ["The Great Gatsby", "To Kill a Mockingbird", "1984", "The Catcher in the Rye",
                    "A Brief History of Time"],
    "Book Author": ["F. Scott Fitzgerald", "Harper Lee", "George Orwell", "J.D. Salinger", "Stephen Hawking"]
},

# University 4
    {
    "University Name": ["University of the Philippines", "Ateneo de Manila University", "De La Salle University",
                        "University of Santo Tomas", "Polytechnic University of the Philippines"],
    "University Location": ["Quezon City", "Quezon City", "Manila", "Manila", "Manila"]
},

# Restaurant 5
    {
    "Restaurant Name": ["Vikings Luxury Buffet", "Antonio's Restaurant", "Mesa Filipino Moderne", "Manam Comfort Filipino"
                        , "Ramen Nagi"],
    "Cuisine Type": ["Buffet", "Fine Dining", "Filipino", "Filipino", "Japanese"]
}
]
for category in pythonclasses:
    for key, value in category.items():
        print(f"{key}:")
        for item in value:
            print(f" · {item}")
    print()
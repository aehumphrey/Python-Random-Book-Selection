# Books on Vacation Project 

## Objective

A friend of mine asked for help picking out books to take on vacation. To help her choose books, I developed a Python algorithm to randomly choose three books from her predefined list. My further goal was to meet specific criteria: first, that each book came from a different genre; second, that the total page length was between 600 and 800 pages; third, that books higher up on her 'to-read' list were prioritized above those lower on her list. This approach was designed to provide a well-rounded collection of books that she could choose to take with her on vacation.

### Skills Learned

- Proficiency in implementing selection criteria to ensure specific attributes are met, facilitating precise item selection and task completion.
- Ability to navigate and manipulate data structures such as dictionaries and lists to organize information efficiently.
- Skill in designing algorithms that meet defined objectives, balancing multiple factors like genre diversity and page length.
- Competence in employing conditional statements to control program flow based on varying conditions and requirements.
- Experience in problem-solving by breaking down complex tasks into systematic steps for effective solution development.
- Advanced proficiency in Python programming through practical application and algorithm development.

## Steps

### Step One

I began by defining a list of dictionaries where each dictionary represents a book with its genre and page count.
<img width="784" alt="Screenshot 2024-07-12 at 2 20 28 PM" src="https://github.com/user-attachments/assets/b96cac8d-2a8e-4a08-b09e-d5c82c6106f6">

*Ref 1. Defining a dictionary in Python*

As I'm using Python 3.7, this dictionary is *ordered*. As this list is relatively short, I was able to input each list item manually. A lengthier list would have required a more complex algorithm.

This dictionary contains four value pairs: "title", a string; "genre", also a string; "pages", an integer; "weight", a float. Most of these are self-explanatory: each book is listed by its title, genre, and page count, but an additional value, "weight," was added to impact the probability that the algorithm would return a given book. Values of 1.0 are considered "base weight", while 0.6, 0.8, and 0.9 are less likely to be chosen and 1.1, 1.2, and 1.3 are more likely to be chosen. 

My friend had slightly preferences for her book selection, but didn't dramatically favor any titles, so I kept the weights within |0.4| from base weight.


### Step Two
<img width="424" alt="Screenshot 2024-07-12 at 2 26 11 PM" src="https://github.com/user-attachments/assets/2d9a3187-4f80-4aa5-88ab-928d253e04e7">


### Step Three
<img width="718" alt="Screenshot 2024-07-12 at 2 26 47 PM" src="https://github.com/user-attachments/assets/b6bf0eed-112c-4b95-8a79-77cf45c903f0">



### Step Four

<img width="484" alt="Screenshot 2024-07-12 at 2 27 18 PM" src="https://github.com/user-attachments/assets/07b4bf53-8888-4a8d-8f70-9d3d4f836738">


### Step Five

<img width="626" alt="Screenshot 2024-07-12 at 2 27 45 PM" src="https://github.com/user-attachments/assets/b7761582-7d61-4faa-b47b-6992e428d435">


## Results


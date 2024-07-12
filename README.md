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

<img width="753" alt="Screenshot 2024-07-12 at 2 36 32 PM" src="https://github.com/user-attachments/assets/67c1c5cf-bd04-408f-85d1-7c6f74763048">

*Ref 1. Defining a dictionary in Python*

As I'm using Python 3.7, this dictionary is *ordered*. As this list is relatively short, I was able to input each list item manually. A lengthier list would have required a more complex algorithm.

This dictionary contains four value pairs: "title", a string; "genre", also a string; "pages", an integer; "weight", a float. Most of these are self-explanatory: each book is listed by its title, genre, and page count, but an additional value, "weight," was added to impact the probability that the algorithm would return a given book. Values of 1.0 are considered "base weight", while 0.6, 0.8, and 0.9 are less likely to be chosen and 1.1, 1.2, and 1.3 are more likely to be chosen. 

My friend had slightly preferences for her book selection, but didn't dramatically favor any titles, so I kept the weights within |0.4| from base weight.

### Step Two

The first step of defining and implementing this function is to intialize the variables. In this case, the initial page count is 0, no book is initially selected, and no genre is initially selected. The algorithm uses a while loop to repeatedly select books until it finds a set that satisfies both genre diversity and page count criteria. The length of the loop (<3) represents the number of books: the program should keep selecting books until the number specified (3) is met.

<img width="379" alt="Screenshot 2024-07-12 at 2 36 54 PM" src="https://github.com/user-attachments/assets/becf37ca-eadb-431c-838b-388fe62e2ef9">

*Ref 2: Initializing variables for the function.*

### Step Three

While the program will select books at random, the weighted probabilities need to be accounted for.

<img width="659" alt="Screenshot 2024-07-12 at 2 37 21 PM" src="https://github.com/user-attachments/assets/660ae102-1182-4ccb-901d-5e4308b4c283">

*Ref 3: Ensuring random selection* 

total_weight is computed by summing up the weights of all books where the genre is not in the selected genres. Books who **are** in the selected genres are not considered for selection (the genre has already been picked).

random.uniform(0, total_weight) generates a random number in the range [0, total_weight). The **for** loop will iterate through each book in the list, accumulating their weights in cumulative_weight. If rand (the random number) is less than cumulative_weight, it means the loop has accumulated enough weight to select this book as selected_book.

### Step Four

In addition to considering random selection, this algorithm also checks to see if a book's genre was already chosen.

<img width="346" alt="Screenshot 2024-07-12 at 3 20 12 PM" src="https://github.com/user-attachments/assets/2e13ba2b-e13d-4e31-926b-134d2329a95f">

*Ref 4: Genre criteria*

If the book's genre was already chosen, the program will continue on the loop until it selects a book with a new genre.

The program will also check if adding this book to the list will exceed the page count targets set:

<img width="380" alt="Screenshot 2024-07-12 at 3 20 12 PM copy" src="https://github.com/user-attachments/assets/92ac14a7-80d3-4792-9cc4-67defb678126">

*Ref 5: Page count criteria*

If adding this book to the list would "break" the page count rule, the loop will continue and select a new book.

Once the algorithm has checked to see if the book has met the criteria, it will add the book to the selected_books list. There is no need to append the weight of the book - that information was necessary in the selection phase, but not in the output.

<img width="398" alt="Screenshot 2024-07-12 at 3 20 12 PM copy 2" src="https://github.com/user-attachments/assets/c0c6cb8a-ed1e-4986-ba2b-947800318efd">

### Step Five

I need to check to see that the minimum page count is met. My friend wants to have enough to read on vacation! This was a late-stage addition to my algorithm; initially, the program returned values averaging in the 300s and it took some trial and error to determine this step was a necessary addition.

<img width="467" alt="Screenshot 2024-07-12 at 3 20 12 PM copy 3" src="https://github.com/user-attachments/assets/db4751e4-46d6-4b6d-9316-3221ab611f44">

*Ref 6: Check page count function*

This is the final step of my function. I can now use this function to select three books:

<img width="249" alt="Screenshot 2024-07-12 at 3 20 12 PM copy 4" src="https://github.com/user-attachments/assets/c1e31367-7b96-4988-b1e3-33e307e37419">

*Ref 7: Selecting three books that satisfy the criteria*

<img width="344" alt="Screenshot 2024-07-12 at 3 20 12 PM copy 5" src="https://github.com/user-attachments/assets/c0ab3534-4bc8-4cc1-bcab-103eb722b3c5">

*Ref 8: Checking that the selected books satisfy the page count criteria*

### Step Five

The final step of this algorithm is to print the selected list of books:

<img width="533" alt="Screenshot 2024-07-12 at 3 20 12 PM copy 6" src="https://github.com/user-attachments/assets/8b3f2c07-08eb-4b17-b18a-002b27da6406">

*Ref 9: Printing the selected books chosen by the algorithm*


## Results

I ran the code, which returned the following output:

![image](https://github.com/user-attachments/assets/64b0e8b1-feb7-471c-b4c3-bf4d6bd6dd8a)

*Ref 10: Output of the program*

My friend was happy with these results, and I was satisfied that I now have a tested way of choosing books from my own lengthy TBR list, 




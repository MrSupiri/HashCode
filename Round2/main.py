libraries = []

file_name = "a_example.txt".strip(".txt")

data = open(f"data/{file_name}.txt").read().split("\n")

n_books, n_libraries, days_to_scan = list(map(int, data[0].split(" ")))
book_scores = list(map(int, data[1].split(" ")))

for i in range(2, n_libraries + 3, 2):
    n_books_, sign_up, days_to_ship = list(map(int, data[i].split(" ")))
    books = list(map(int, data[i+1].split(" ")))
    libraries.append([{"books": n_books_, "sign-up": sign_up, "days-2-ship": days_to_ship}, books])

print(n_books, n_libraries, days_to_scan)
print(book_scores)
for library in libraries:
    print(library)

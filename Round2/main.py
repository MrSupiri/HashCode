libraries = []

file_name = "b_read_on.txt".strip(".txt")

data = open(f"data/{file_name}.txt").read().split("\n")

n_books, n_libraries, days_to_scan = list(map(int, data[0].split(" ")))
book_scores = list(map(int, data[1].split(" ")))

x = 0
for i in range(2, n_libraries + 3, 2):
    n_books_, sign_up, books_per_day = list(map(int, data[i].split(" ")))
    total_value = 0
    books = list(map(int, data[i+1].split(" ")))
    for book in books:
        total_value += book_scores[book]
    libraries.append([{"library-id": x, "books": n_books_, "sign-up": sign_up, "books-per-day": books_per_day, "total-value": total_value}, books])
    x += 1

sorted_libraries = sorted(libraries, key=lambda k: k[0]['sign-up'])

selected_libraries = []

for library in sorted_libraries:
    time_take = library[0]["sign-up"] + round(library[0]["books"]/library[0]["books-per-day"])
    if time_take <= days_to_scan:
        selected_libraries.append(library)
        days_to_scan -= time_take

with open(f"output/{file_name}.out", "w") as f:
    f.write(f"{len(selected_libraries)}\n")
    for library in selected_libraries:
        f.write(f'{library[0]["library-id"]} {library[0]["books"]}\n')
        f.write(f"{' '.join(list(map(str, library[1])))}\n")

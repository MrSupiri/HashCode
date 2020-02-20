def common(a, b):
    c = [value for value in a if value in b]
    return c


def remove_overlap(a, b):
    return list(set(a) - set(b))


libraries = []

file_name = "f_libraries_of_the_world.txt".strip(".txt")

data = open(f"data/{file_name}.txt").read().split("\n")

n_books, n_libraries, days_to_scan = list(map(int, data[0].split(" ")))
book_scores = list(map(int, data[1].split(" ")))
books = {}

x = 0
for i in range(2, n_libraries + 3, 2):
    n_books_, sign_up, books_per_day = list(map(int, data[i].split(" ")))
    total_value = 0
    library_books = list(map(int, data[i + 1].split(" ")))
    library_books = [[book, book_scores[book]] for book in library_books]
    library_books = sorted(library_books, key=lambda k: k[1], reverse=True)
    library_books = [book[0] for book in library_books]
    for i, book in enumerate(library_books):
        total_value += book_scores[book]

    libraries.append([{"library-id": x, "books": n_books_, "sign-up": sign_up, "books-per-day": books_per_day,
                       "total-value": total_value}, library_books])
    x += 1

sorted_libraries = sorted(libraries, key=lambda k: k[0]['sign-up'])

selected_libraries = []

selected_books = []

x = -1
for library in sorted_libraries:
    x += 1
    if x == 0:
        time_take = library[0]["sign-up"] + round(library[0]["books"] / library[0]["books-per-day"])
        selected_books += library[1]
    else:
        d = common(selected_books, library[1])
        new_books = remove_overlap(library[1], d)
        time_take = round(len(new_books) / library[0]["books-per-day"])
        library = [{"library-id": library[0]["library-id"], "books": len(new_books),
                    "sign-up": library[0]["sign-up"], "books-per-day": library[0]["books-per-day"],
                    "total-value": library[0]["total-value"]}, new_books]
    if time_take <= days_to_scan:
        selected_libraries.append(library)
        days_to_scan -= time_take
    else:
        for i in range(library[0]["books"], 0, -1):
            if x == 0:
                time_take = library[0]["sign-up"] + round(len(library[1][:i]) / library[0]["books-per-day"])
            else:
                time_take = round(len(library[1][:i]) / library[0]["books-per-day"])
            if time_take <= days_to_scan:
                library_ = [{"library-id": library[0]["library-id"], "books": len(library[1][:i]),
                             "sign-up": library[0]["sign-up"], "books-per-day": library[0]["books-per-day"],
                             "total-value": library[0]["total-value"]}, library[1][:i]]
                selected_libraries.append(library_)
                days_to_scan -= time_take
                break

with open(f"output/{file_name}.out", "w") as f:
    f.write(f"{len(selected_libraries)}\n")
    for library in selected_libraries:
        f.write(f'{library[0]["library-id"]} {library[0]["books"]}\n')
        f.write(f"{' '.join(list(map(str, library[1])))}\n")

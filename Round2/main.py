books = {}

file_name = "a_example.txt".strip(".txt")

data = open(f"data/{file_name}.txt").read().split("\n")

n_slices, n_types = list(map(int, data[0].split(" ")))
pizza_types = data[1].split(" ")

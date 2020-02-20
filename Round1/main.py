pizzas = {}

file_name = "a_example.in".strip(".in")

data = open(f"data/{file_name}.in").read().split("\n")

n_slices, n_types = list(map(int, data[0].split(" ")))
pizza_types = data[1].split(" ")


for i, pizza_type in enumerate(pizza_types):
    pizzas[i] = int(pizza_type)

selected_types = {}

mid_value = (len(pizzas) // 2)

list_1 = list(pizzas.keys())[::-1][:mid_value]
list_2 = list(pizzas.keys())[:mid_value] 

for pizza in list(pizzas.keys())[::-1][:mid_value] + list(pizzas.keys())[:mid_value]:
    if sum(selected_types.values()) + pizzas[pizza] <= n_slices:
        selected_types[pizza] = pizzas[pizza]

output = map(str, list(selected_types.keys())[::-1])

with open(f"data/{file_name}.out", "w") as f:
    f.write(f"{len(selected_types)}\n{' '.join(output)}")

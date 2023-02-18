def solve(num_heads, num_legs):
    rabbits = (num_legs - (num_heads * 2)) / 4
    chickens = num_heads - rabbits
    return list[rabbits,chickens]


print(solve(35, 94))
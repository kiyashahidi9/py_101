import random as r

problem_sets = {
    'easy1': 11,
    'easy2': 12,
    'easy3': 10,
}

list_keys = list(problem_sets.keys())
rand_key = list_keys[r.randint(0, 2)]

prob_endpoint = problem_sets[rand_key]
rand_problem = r.randint(1, prob_endpoint)

print(f"Your problem is {rand_key} question {rand_problem}")


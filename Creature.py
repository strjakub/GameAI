import random


class Creature:
    def __init__(self, path_len, path=None, generate=True, from_index=None, to_index=None):
        self.path = None
        self.create_path(path_len, path, generate, from_index, to_index)

        # variable to store distance traveled by creature
        self.dist = 0

    def create_path(self, path_len, path, generate, from_index, to_index):
        if not path:
            self.path = random.choices(population=[0, 1], weights=[0.7, 0.3], k=path_len)
        else:
            # generating left and right inclusive range [from_index, to_index]
            if generate:
                generated_path = random.choices(population=[0, 1], weights=[0.7, 0.3], k=to_index - from_index + 1)
                path[from_index: to_index + 1] = generated_path
            self.path = path

    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other):
        return self.dist == other.dist

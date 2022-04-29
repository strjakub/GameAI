from Creature import Creature


class Generation:
    def __init__(self, generation_num,  leave_best_num, path_len):
        self.generation_num = generation_num
        self.leave_best_num = leave_best_num
        self.creatures = [Creature(path_len) for _ in range(self.generation_num)]

    def update_generation(self):
        ...

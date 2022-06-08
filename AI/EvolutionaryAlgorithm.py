from AI.Generation import Generation


class EvolutionaryAlgorithm:
    def __init__(self, game_map, map_length, leave_best_num):
        self.map = game_map
        self.map_length = map_length
        self.leave_best_num = leave_best_num
        self.generation = Generation(game_map=self.map, generation_num=50,
                                     leave_best_num=self.leave_best_num, path_len=self.map_length)
        self.generation.evaluate()
        # variables for storing how many moves should be changed before and after death position
        self.prev_indexes_num = 9
        self.next_indexes_num = 10

    # return the path to be displayed in the GUI
    def make_evolution_step(self):
        self.generation.update_generation(self.prev_indexes_num, self.next_indexes_num)
        self.generation.evaluate()
        return self.generation.creatures[self.leave_best_num - 1].path

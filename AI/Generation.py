from AI.Creature import Creature
from Map.Map import Map
from Map.Vector import Vector
from Map.Square import Square
from queue import PriorityQueue


class Generation:
    def __init__(self, game_map, generation_num,  leave_best_num, path_len):
        self.map = game_map
        self.generation_num = generation_num
        self.leave_best_num = leave_best_num
        self.path_len = path_len
        self.frames_per_block = 10
        self.creatures = [Creature(self.frames_per_block * self.path_len) for _ in range(self.generation_num)]
        self.best_creatures = PriorityQueue()

    # evaluate whole generation and return the best creatures, which will be later reproduced
    def evaluate(self):
        player = Square(Vector(Map.graininess, (self.map.blocks_height - 1) * Map.graininess - 1), self.map)
        for creature in self.creatures:
            player.position = Vector(Map.graininess, (self.map.blocks_height - 1) * Map.graininess - 1)
            player.alive = True
            player.jump = False
            for move in creature.path:
                if move == 1:
                    player.jump = True

                player.move()
                death_pos = player.is_dead()
                if death_pos != -1:
                    creature.dist = death_pos // 12 - 1
                    self.best_creatures.put(creature)
                    break

            if self.best_creatures.qsize() > self.leave_best_num:
                self.best_creatures.get()

        self.creatures = []
        while not self.best_creatures.empty():
            creature = self.best_creatures.get()
            self.creatures.append(creature)

    # reproduce best_creatures
    def update_generation(self, prev_indexes_num, next_indexes_num):
        reproduction_num = (self.generation_num - self.leave_best_num) // self.leave_best_num
        for i in range(self.leave_best_num):
            creature = self.creatures[i]
            left_range = max(0, creature.dist - prev_indexes_num * self.frames_per_block)
            right_range = min(self.frames_per_block * self.path_len - 1,
                              creature.dist + next_indexes_num * self.frames_per_block)
            creature.create_path(path_len=self.frames_per_block * self.path_len, path=creature.path, generate=True,
                                 from_index=creature.dist, to_index=right_range)
            for _ in range(reproduction_num):
                child = Creature(path_len=self.frames_per_block * self.path_len, path=creature.path, generate=True,
                                 from_index=left_range, to_index=right_range)
                self.creatures.append(child)

        while len(self.creatures) < self.generation_num:
            creature = self.creatures[self.leave_best_num - 1]
            left_range = max(0, creature.dist - prev_indexes_num * self.frames_per_block)
            right_range = min(self.frames_per_block * self.path_len - 1,
                              creature.dist + next_indexes_num * self.frames_per_block)
            child = Creature(path_len=self.frames_per_block * self.path_len, path=creature.path, generate=True,
                             from_index=left_range, to_index=right_range)
            self.creatures.append(child)

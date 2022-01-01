import numpy as np
class Spliner:
    def __init__(self, data):
        self.data = data

    def run(self):
        if self.data.path[-1] != self.data.next_point:
            print(f"Next point is {self.data.next_point}")
            new_path = np.linspace(self.data.path[-1], self.data.next_point, 10).tolist()
            print(type(new_path))
            # self.data.path.append(new_path)
            # print(self.data.path)
import matplotlib.pyplot as plt
import itertools
import random
import copy
import os
import shutil
from PIL import Image as PILImage
from datetime import datetime

class The_Schelling_Model:
    def __init__(self, 
                 columns = 50, 
                 rows = 50, 
                 percentage_population = 80, 
                 satisfaction_threshold = 4, 
                 iter_count = 1000):
        
        self.columns = columns
        self.rows = rows
        self.races = 2
        self.percentage_population = percentage_population
        self.vacant_space = 1 - (self.percentage_population/100)
        self.satisfaction_threshold = float(satisfaction_threshold)/float(8)
        self.iter_count = iter_count
        self.vacant_cells = []
        self.agents = {}
        self.filenames = []
        self.image_count = 1
        self.images = []
        self.image_directory_path = f"P={(self.percentage_population/100)} t={satisfaction_threshold}"
        if (os.path.exists(self.image_directory_path)):
            shutil.rmtree(self.image_directory_path)
            os.mkdir(self.image_directory_path)
        else:
            os.mkdir(self.image_directory_path)
        self.fill()
 
    def fill(self):
        self.total_cells = list(itertools.product(range(self.columns),range(self.rows)))
        random.shuffle(self.total_cells)
    
        self.empty_num = int( self.vacant_space * len(self.total_cells) )
        self.vacant_cells = self.total_cells[:self.empty_num]
    
        self.remaining_cells = self.total_cells[self.empty_num:]
        houses_by_race = [self.remaining_cells[i::self.races] for i in range(self.races)]
        for i in range(self.races):
            self.agents = dict(
                                self.agents.items() |
                                dict(zip(houses_by_race[i], [i+1]*len(houses_by_race[i]))).items()
                                )
        self.filename = f'{self.image_directory_path}/{self.image_count}.png'
        self.filenames.append(self.filename) 
        self.plot(file_name=self.filename)
        self.image_count += 1
 
    def is_unhappy(self, x, y):
 
        race = self.agents[(x,y)]
        num_same = 0
        num_discrete = 0
    
        if x > 0 and y > 0 and (x-1, y-1) not in self.vacant_cells:
            if self.agents[(x-1, y-1)] == race:
                num_same += 1
            else:
                num_discrete += 1
        if y > 0 and (x,y-1) not in self.vacant_cells:
            if self.agents[(x,y-1)] == race:
                num_same += 1
            else:
                num_discrete += 1
        if x < (self.columns-1) and y > 0 and (x+1,y-1) not in self.vacant_cells:
            if self.agents[(x+1,y-1)] == race:
                num_same += 1
            else:
                num_discrete += 1
        if x > 0 and (x-1,y) not in self.vacant_cells:
            if self.agents[(x-1,y)] == race:
                num_same += 1
            else:
                num_discrete += 1        
        if x < (self.columns-1) and (x+1,y) not in self.vacant_cells:
            if self.agents[(x+1,y)] == race:
                num_same += 1
            else:
                num_discrete += 1
        if x > 0 and y < (self.rows-1) and (x-1,y+1) not in self.vacant_cells:
            if self.agents[(x-1,y+1)] == race:
                num_same += 1
            else:
                num_discrete += 1        
        if x > 0 and y < (self.rows-1) and (x,y+1) not in self.vacant_cells:
            if self.agents[(x,y+1)] == race:
                num_same += 1
            else:
                num_discrete += 1        
        if x < (self.columns-1) and y < (self.rows-1) and (x+1,y+1) not in self.vacant_cells:
            if self.agents[(x+1,y+1)] == race:
                num_same += 1
            else:
                num_discrete += 1
    
        if (num_same+num_discrete) == 0:
            return False
        else:
            return float(num_same)/(num_same+num_discrete) < self.satisfaction_threshold
 
    def step(self):
        for i in range(self.iter_count):
            self.old_agents = copy.deepcopy(self.agents)
            n_changes = 0
            for agent in self.old_agents:
                if self.is_unhappy(agent[0], agent[1]):
                    agent_race = self.agents[agent]
                    empty_house = random.choice(self.vacant_cells)
                    self.agents[empty_house] = agent_race
                    del self.agents[agent]
                    self.vacant_cells.remove(empty_house)
                    self.vacant_cells.append(agent)
                    n_changes += 1
            
            self.filename = f'{self.image_directory_path}/{self.image_count}.png'
            self.filenames.append(self.filename) 
            self.plot(file_name=self.filename)
            self.image_count += 1
            print("Changes =", n_changes, "Image Count =", self.image_count-1)

            if n_changes == 0:
                break

    def relocate(self, x, y):
        race = self.agents[(x,y)]
        empty_house = random.choice(self.vacant_cells)
        self.updated_agents[empty_house] = race
        del self.updated_agents[(x, y)]
        self.vacant_cells.remove(empty_house)
        self.vacant_cells.append((x, y))
 
    def plot(self, file_name = 'test.png'):
        fig, ax = plt.subplots()
        agent_colors = {2:'#FF671F', 1:'#046A38'}
        agent_shapes = {1:'o', 2:'o'}
        for agent in self.agents:
            ax.scatter(agent[0]+0.5, agent[1]+0.5, 
                       color = agent_colors[self.agents[agent]],
                       marker = agent_shapes[self.agents[agent]]                        
                       )
    
        ax.set_title(f"P = {(self.percentage_population/100)}, t = {self.satisfaction_threshold*8}", fontsize=16, fontweight='bold')
        ax.set_xlim([0, self.columns])
        ax.set_ylim([0, self.rows])
        # ax.set_xticks([])
        # ax.set_yticks([])
        plt.savefig(file_name)
        plt.close('all')
    
    def create_gif(self):
        for n in self.filenames:
            frame = PILImage.open(n)
            self.images.append(frame)
        current_time = datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        self.images[0].save(f'{self.image_directory_path}/{current_time} P={(self.percentage_population/100)} t={self.satisfaction_threshold*8}.gif',
                                save_all=True,
                                append_images=self.images[1:],
                                duration=750,
                                loop=0)

if __name__ == "__main__":

    print("P = 0.6, t = 3")
    print("-"*80)
    schelling_model_object1 = The_Schelling_Model(  columns = 50, 
                                        rows = 50, 
                                        percentage_population = 60, 
                                        satisfaction_threshold = 3)
    schelling_model_object1.step()
    schelling_model_object1.create_gif()
    print("="*80)

    print("P = 0.6, t = 4")
    print("-"*80)
    schelling_model_object2 = The_Schelling_Model(  columns = 50, 
                                        rows = 50, 
                                        percentage_population = 60, 
                                        satisfaction_threshold = 4)
    schelling_model_object2.step()
    schelling_model_object2.create_gif()
    print("="*80)

    print("P = 0.8, t = 3")
    print("-"*80)
    schelling_model_object3 = The_Schelling_Model(  columns = 50, 
                                     rows = 50, 
                                     percentage_population = 80, 
                                     satisfaction_threshold = 3)
    schelling_model_object3.step()
    schelling_model_object3.create_gif()
    print("="*80)

    print("P = 0.8, t = 4")
    print("-"*80)
    schelling_model_object4 = The_Schelling_Model(  columns = 50, 
                                        rows = 50, 
                                        percentage_population = 80, 
                                        satisfaction_threshold = 4)
    schelling_model_object4.step()
    schelling_model_object4.create_gif()
    print("="*80)

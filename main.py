from app.scene import DynaQMazeScene, DynaQMazeMultiAgentScene, DynaQPlusMazeMultiAgentScene, MixedAgentsScene, ObstacleCourseScene
from app.rf.maze import Maze, MazeGenerator
from app.rf.obstacle_course import ObstacleEnvironment
from app.rf.model import MazeModel, DynaQPlusMazeModel, Model
from app.rf.agents import DynaQAgent, AgentVisualizer, DynaQPlusAgent, ObstacleEnvironmentAgent
from threading import Thread

if __name__ == "__main__":
    # DynaQMazeScene(1920, 1080, "DynaQ-Demo", Maze.load_from_numpy_array("./mazes/first_example_maze_positive_reward.npy", (2, 0))).run()
    # DynaQMazeScene(1920, 1080, "DynaQ-Demo", MazeGenerator.generate(80, 100, goal_reward=1)).run()
    # DynaQMazeMultiAgentScene(1920, 1080, "DynaQ-Multi-Agent-Demo", MazeGenerator.generate(20, 40, algorithm="binary_tree", goal_reward=1)).run()    
    # DynaQPlusMazeMultiAgentScene(1920, 1080, "DynaQ+-Multi-Agent-Demo", Maze.load_from_numpy_array("./mazes/blocking_maze_example.npy", (5, 3))).run()



    # maze = MazeGenerator.generate(20, 30, algorithm="prims", goal_reward=1)
    # maze_model = MazeModel(maze) # just there for compatibility
    # dynaq_plus_maze_model = DynaQPlusMazeModel(maze)
    # learning_rate = 0.1
    # epsilon = 0.9
    # discount_factor = 0.985
    # planning_steps = 0
    # max_steps_per_episode = 1000000
    # pause = None
    # agent_one = DynaQPlusAgent(maze, dynaq_plus_maze_model, learning_rate, discount_factor, epsilon, max_steps_per_episode, planning_steps, k = 0, pause = pause)        
    # agent_two = DynaQAgent(maze, maze_model, learning_rate, discount_factor, epsilon, max_steps_per_episode, planning_steps, pause = pause, use_prioritized_sweeping=True, theta=0.000001)        
    # agent_three = DynaQAgent(maze, maze_model, learning_rate, discount_factor, epsilon, max_steps_per_episode, planning_steps, pause = pause)
    # train_threads = []
    # for agent in (agent_one, agent_two, agent_three):
    #     t = Thread(target = agent.train_episode, args = [], daemon=True)
    #     train_threads.append(t)
    #     t.start()
    # for thread in train_threads:
    #     thread.join()
    # print(agent_one.step, agent_two.step, agent_three.step)
    # MixedAgentsScene(1920, 1080, "DynaQ+-Multi-Agent-Demo", maze, (agent_one, agent_two, agent_three)).run()


    obstacle_environment = ObstacleEnvironment(100, 100, [], (8, 8, 0), [])
    model = Model(obstacle_environment) # just there for compatibility
    learning_rate = 0.1
    epsilon = 0.9
    discount_factor = 0.985
    planning_steps = 0
    max_steps_per_episode = 1000000
    pause = None
    agent_one = ObstacleEnvironmentAgent(obstacle_environment, model, learning_rate, discount_factor, epsilon, max_steps_per_episode, planning_steps, 5, pause = pause)        
    agent_two = ObstacleEnvironmentAgent(obstacle_environment, model, learning_rate, discount_factor, epsilon, max_steps_per_episode, planning_steps, 5, pause = pause, use_prioritized_sweeping=True, theta=0.000001)        
    train_threads = []
    for agent in (agent_one, agent_two):
        t = Thread(target = agent.train_episode, args = [], daemon=True)
        train_threads.append(t)
        t.start()
    for thread in train_threads:
        thread.join()
    print(agent_one.step, agent_two.step)
    ObstacleCourseScene(1920, 1080, "Obstacle-Course-Demo", obstacle_environment, (agent_one, agent_two)).run()
## ECE 372 - Dynamic Programming and Optimal Control

### Setup

- First install [miniconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html#regular-installation). Follow the steps corresponding to your operating system.
- Create a `conda` environment for this course. This will be useful to separate packages required in the course from any others and avoid version conflicts.

    `conda create --name ece372 -y python=3.10`

- Activate the environment you just created. You need to do this every time you open a terminal to run the course scripts.

    `conda activate ece372`

- Create a folder for the course and enter it

    `cd PATH_TO_FOLDER` <- change it here

- Clone this repository and install its packages (including Gymnasium)

    ```
    git clone https://github.com/lcdbezerra/kaust_ece372.git
    pip install -r kaust_ece372/requirements.txt
    ```

- Clone and install the `gym-maze` environment

    ```
    git clone https://github.com/lcdbezerra/gym-maze.git
    cd gym-maze
    pip install -e .
    cd ..
    ```

- Make sure the environment is set up properly. Launch Python and try the following block. It should open a window and run without errors

    ```
    import gym
    import gym_maze
    env = gym.make("maze-random-10x10-v0")
    obs = env.reset()
    act = env.action_space.sample()
    obs = env.step(act)
    env.render()
    ```

- Clone and install the `gym-pybullet-drones` environment

    ```
    git clone https://github.com/lcdbezerra/gym-pybullet-drones.git
    cd gym-pybullet-drones
    pip install -e .
    cd ..
    ```

- Make sure the `gym-pybullet-drones` environment is set up properly. The following line should run without errors

    `python gym-pybullet-drones/gym_pybullet_drones/examples/pid.py`

- If you are unlucky and the above line doesn't work, run the following command and try again

    ```
    sudo apt install build-essential
    conda install -c conda-forge gcc=12.1.0
    ```
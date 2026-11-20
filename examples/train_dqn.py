"""Train a DQN signal controller on Tigerpass with Stable-Baselines3.

    pip install "mixed-traffic-sumo[train]"
    python examples/train_dqn.py
"""
from stable_baselines3 import DQN
import mixed_traffic_sumo as mts

env = mts.make_env("tigerpass", num_seconds=3600, out_csv_name="outputs/tigerpass_dqn")
model = DQN("MlpPolicy", env, learning_rate=1e-3, buffer_size=50_000,
            learning_starts=0, train_freq=1, target_update_interval=500,
            exploration_fraction=0.05, exploration_final_eps=0.01, verbose=1)
model.learn(total_timesteps=100_000)
model.save("outputs/tigerpass_dqn_model")

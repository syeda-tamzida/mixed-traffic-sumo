"""Run the Tigerpass intersection with a random policy for one simulated hour."""
import tigerpass_traffic as tp

env = tp.make_env(num_seconds=3600)
obs, info = env.reset(seed=0)
done = False
while not done:
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated
print({k: round(float(v), 2) for k, v in info.items() if k.startswith("system_")})
env.close()

"""Run a scenario with a random policy for one simulated hour."""
import mixed_traffic_sumo as mts

print("Available scenarios:", mts.list_scenarios())
env = mts.make_env("tigerpass", num_seconds=3600)
obs, info = env.reset(seed=0)
done = False
while not done:
    obs, reward, terminated, truncated, info = env.step(env.action_space.sample())
    done = terminated or truncated
print({k: round(float(v), 2) for k, v in info.items() if k.startswith("system_")})
env.close()

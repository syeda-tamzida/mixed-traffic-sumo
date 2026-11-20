"""Fixed-time signal baseline: run the original signal plan and report average metrics."""
import numpy as np
import tigerpass_traffic as tp

env = tp.make_env(num_seconds=3600, fixed_ts=True)
env.reset(seed=0)
waits, queues, speeds = [], [], []
done = False
while not done:
    _, _, terminated, truncated, info = env.step(None)
    waits.append(info["system_mean_waiting_time"])
    queues.append(info["system_total_stopped"])
    speeds.append(info["system_mean_speed"])
    done = terminated or truncated
env.close()
print(f"Fixed-time, 1 h: mean waiting time {np.mean(waits):.1f} s, "
      f"mean queued vehicles {np.mean(queues):.1f}, mean speed {np.mean(speeds):.2f} m/s")

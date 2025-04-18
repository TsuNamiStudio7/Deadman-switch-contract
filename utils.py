import time

# Simulate checking last activation time and timeout
def get_time_until_timeout(last_activation_time, timeout):
    current_time = int(time.time())
    time_remaining = timeout - (current_time - last_activation_time)
    if time_remaining > 0:
        return f"Time remaining until timeout: {time_remaining} seconds"
    else:
        return "Timeout reached, action will be triggered"

# Example: Get time remaining for Dead Man's Switch
last_activation_time = 1625670000  # Simulated timestamp
timeout = 604800  # 1 week in seconds
print(get_time_until_timeout(last_activation_time, timeout))

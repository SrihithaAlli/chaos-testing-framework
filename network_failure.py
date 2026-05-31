import random

def simulate_network_failure():
    """
    Simulates network behavior.
    Sometimes works, sometimes fails.
    """

    outcomes = [
        "Network Connected",
        "Network Timeout",
        "Connection Refused",
        "Packet Loss Detected"
    ]

    result = random.choice(outcomes)

    if result == "Network Connected":
        return result
    else:
        raise Exception(result)


# Testing
if __name__ == "__main__":
    try:
        print(simulate_network_failure())
    except Exception as e:
        print("Network Failure:", e)
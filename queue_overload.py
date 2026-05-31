import random

def simulate_queue_overload():
    """
    Simulates request queue behavior.
    """

    requests = random.randint(50, 1000)

    if requests < 500:
        return f"Queue Healthy - {requests} requests"

    raise Exception(f"Queue Overloaded - {requests} requests")


# Testing
if __name__ == "__main__":
    try:
        print(simulate_queue_overload())
    except Exception as e:
        print("Queue Failure:", e)
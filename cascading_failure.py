import random

def simulate_cascading_failure():

    print("Database Crash Occurred!")

    db_failed = True

    if db_failed:
        print("AI Service Failed because DB is unavailable")

    if db_failed:
        print("Network Congestion Increased")

    if db_failed:
        print("Queue Overloaded due to retries")

    return "Cascading Failure Simulation Complete"


if __name__ == "__main__":
    print(simulate_cascading_failure())
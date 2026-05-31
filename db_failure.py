import random

def simulate_db_failure():
    """
    Simulates database behavior.
    Sometimes works, sometimes crashes.
    """

    outcomes = [
        "Database Running",
        "Database Connection Lost",
        "Database Crash",
        "Database Timeout"
    ]

    result = random.choice(outcomes)

    if result == "Database Running":
        return result
    else:
        raise Exception(result)


# Testing
if __name__ == "__main__":
    try:
        print(simulate_db_failure())
    except Exception as e:
        print("Database Failure:", e)
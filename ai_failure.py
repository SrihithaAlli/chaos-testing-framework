import random

def simulate_ai_failure():
    """
    Simulates AI service behavior.
    Sometimes works, sometimes fails.
    """

    outcomes = [
        "AI Response Generated",
        "AI Timeout Error",
        "AI Model Unavailable",
        "Invalid AI Output"
    ]

    result = random.choice(outcomes)

    if result == "AI Response Generated":
        return result
    else:
        raise Exception(result)


# Testing
if __name__ == "__main__":
    try:
        print(simulate_ai_failure())
    except Exception as e:
        print("AI Failure:", e)
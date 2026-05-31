# Chaos Testing Framework

## Overview

The Chaos Testing Framework is a Python-based testing suite designed to intentionally simulate failures in system components to evaluate system resilience and fault tolerance. The framework introduces controlled failures and monitors system behavior under adverse conditions.

## Objective

To simulate and analyze different failure scenarios such as AI service failures, network disruptions, database crashes, queue overloads, and cascading failures in order to assess system reliability and robustness.

## Features

* AI Failure Simulation
* Network Loss Simulation
* Database Crash Simulation
* Queue Overload Simulation
* Cascading Failure Simulation
* Automated Multi-Run Chaos Testing
* Statistical Test Reporting

## Project Structure

Chaos_Testing_Framework/

├── ai_failure.py

├── network_failure.py

├── db_failure.py

├── queue_overload.py

├── cascading_failure.py

├── chaos_test.py

└── README.md

## Technologies Used

* Python 3.8+
* Random Module
* Git
* GitHub
* Visual Studio Code

## How to Run

Run the chaos testing suite:

```bash
python chaos_test.py
```

## Sample Results

* Total Simulations: 50
* Total Tests Executed: 200
* Passed Tests: 79
* Failed Tests: 121
* Cascading Failures: 5

## Future Enhancements

* Configurable failure probabilities
* Automated report generation
* Real-time monitoring dashboard
* Distributed system simulation

## Author

Srihitha Alli

AI & ML Internship Project

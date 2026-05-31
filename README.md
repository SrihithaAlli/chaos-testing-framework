# Chaos Testing Framework

## Overview

The Chaos Testing Framework is a Python-based testing suite designed to intentionally simulate failures in system components to evaluate system resilience and fault tolerance. The framework helps identify weaknesses by introducing controlled failures and monitoring system behavior under adverse conditions.

## Objective

To simulate and analyze different failure scenarios such as AI service failures, network disruptions, database crashes, queue overloads, and cascading failures in order to assess system reliability and robustness.

---

## Features

* AI Failure Simulation
* Network Loss Simulation
* Database Crash Simulation
* Queue Overload Simulation
* Cascading Failure Simulation
* Automated Multi-Run Chaos Testing
* Statistical Test Reporting

---

## Project Structure

```text
Chaos_Testing_Framework
│
├── ai_failure.py
├── network_failure.py
├── db_failure.py
├── queue_overload.py
├── cascading_failure.py
├── chaos_test.py
└── README.md
```

---

## Technologies Used

* Python 3.8+
* Random Module
* Git
* GitHub
* Visual Studio Code

---

## Failure Scenarios Tested

### AI Failures

Simulates:

* AI Timeout Errors
* AI Model Unavailability
* Invalid AI Responses

### Network Failures

Simulates:

* Network Timeouts
* Connection Refused
* Packet Loss

### Database Failures

Simulates:

* Database Crashes
* Connection Loss
* Database Timeouts

### Queue Overload

Simulates:

* Excessive Request Load
* Queue Saturation

### Cascading Failures

Simulates:

* Database Failure
* AI Service Failure
* Network Congestion
* Queue Overload

---

## How to Run

Clone the repository:

```bash
git clone https://github.com/SrihithaAlli/chaos-testing-framework.git
```

Navigate to the project directory:

```bash
cd chaos-testing-framework
```

Run the chaos test suite:

```bash
python chaos_test.py
```

---

## Sample Output

```text
===== CHAOS TEST REPORT =====

AI Failures: 33
Network Failures: 35
Database Failures: 32
Queue Overloads: 21
Cascading Failures: 5
Successful Tests: 79

Total Simulations: 50
Total Tests Executed: 200
Passed Tests: 79
Failed Tests: 121
```

---

## Results

The framework successfully simulated multiple failure conditions and generated statistical reports summarizing system behavior under stress. The implementation demonstrates the concept of chaos engineering and helps evaluate system reliability and fault tolerance.

---

## Future Enhancements

* Real-time monitoring dashboard
* Logging and reporting system
* Configurable failure probabilities
* Distributed system simulation
* Automated test report generation

---

## Author

Srihitha Alli

AI & ML Internship Project

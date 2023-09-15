# HMAssessment Project

Welcome to the my assessment, showcasing comprehensive problem-solving and coding proficiency. This project provides detailed answers to various challenges, accompanied by robust testing and database integration. Dive in to explore the solutions, validate code correctness, and witness a commitment to code quality.

[Click here for my answers in a text file](answers.txt)


## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python (3.7 or higher) installed on your system.
- A code editor or IDE of your choice.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/asaki222/hmassessment.git

2. Navigate to the project directory:
    ```bash
    cd hmassessment

3. Create a virtual environment and active a virtual enviroment(optional):
    ```bash
    python -m venv venv
    source venv/bin/activate

4. To run the tests, and play with the code:
    
    ##### Create the databases:

    For test:

    ```bash
    sqlite3 mytestdatabase.sqlite < setup_test_database_sqlite.sql
    ```

    For prod:
    
    ```bash
    sqlite3 mydatabase.sqlite < setup_test_database_sqlite.sql
    ```

    #### RUN TESTS

    ```bash
    python3 -m unittest tests.test_sql_questions 
    python3 -m unittest tests.test_python_questions
    ```

    #### FOR EXPERIMENTATION

    ```bash
    python3
    ```
    and import the methods you would like to test

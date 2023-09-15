# HMAssessment Project

Hey there! Welcome to my assessment project where I've tackled some interesting coding challenges. I've not only provided solutions but also added some testing to make sure everything works as expected. Feel free to dig in, check out the answers, and see how I've ensured code quality!

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
    cd tests/databases
    sqlite3 mytestdatabase.sqlite < setup_test_database_sqlite.sql
    ```

    For prod:
    
    ```bash
    cd questions/databases
    sqlite3 mydatabase.sqlite < setup_database_sqlite.sql
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
    and import the methods you would like to test(example):

    ```python   
       from questions.python_questions import create_job_status_dict, find_local_maxima
       data = [3, 6, 1, 2, 5, 4, 10, 5, 7, 2, 4]
       find_local_maxima(data)
    ```
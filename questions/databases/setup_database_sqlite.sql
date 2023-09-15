PRAGMA foreign_keys = ON;
ATTACH DATABASE 'mydatabase.sqlite' AS mydb;

CREATE TABLE IF NOT EXISTS mydb.status (
    key INTEGER PRIMARY KEY,
    test_id INTEGER NOT NULL,
    code_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status BOOLEAN NOT NULL
);


INSERT INTO mydb.status (test_id, code_id, date, status)
VALUES
    (3, 1, '2019-11-20', TRUE),
    (3, 1, '2020-06-13', FALSE),
    (1, 2, '2020-11-02', FALSE),
    (1, 1, '2020-05-07', FALSE),
    (3, 1, '2020-03-26', FALSE),
    (1, 3, '2020-04-17', TRUE),
    (3, 1, '2020-01-05', TRUE),
    (1, 3, '2020-04-25', TRUE),
    (1, 1, '2020-09-22', FALSE),
    (1, 1, '2020-09-16', FALSE)
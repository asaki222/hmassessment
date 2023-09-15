PRAGMA foreign_keys = ON;
ATTACH DATABASE 'mytestdatabase.sqlite' AS mytestdb;

-- Create the "status" table
CREATE TABLE IF NOT EXISTS mytestdb.status (
    key INTEGER PRIMARY KEY,
    test_id INTEGER NOT NULL,
    code_id INTEGER NOT NULL,
    date DATE NOT NULL,
    status BOOLEAN NOT NULL
);


INSERT INTO mytestdb.status (test_id, code_id, date, status)
VALUES
    (3, 1, '2019-11-20', TRUE),
    (3, 1, '2020-06-13', FALSE),
    (1, 2, '2020-11-02', FALSE),
    (1, 1, '2020-05-07', FALSE),
    (1, 2, '2020-05-07', TRUE);;
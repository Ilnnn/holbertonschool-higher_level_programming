-- Usin the hbtn_0d_tvshows db in school project
CREATE TABLE if not exists second_table(
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT into second_table (id, name, score) 
VALUES (1, 'John', 10),
        (2, 'Alex', 3),
        (3, 'Bob', 14),
        (4, 'George', 8);

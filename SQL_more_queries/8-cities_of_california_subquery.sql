SELECT id, name FROM cities
WHERE cities id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;
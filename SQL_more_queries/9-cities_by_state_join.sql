-- Using the hbtn_0d_tvshows db in school project
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states on cities.state_id = states.id
ORDER BY cities.id ASC;

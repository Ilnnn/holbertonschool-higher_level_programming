-- Usin the hbtn_0d_tvshows db in school project
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;

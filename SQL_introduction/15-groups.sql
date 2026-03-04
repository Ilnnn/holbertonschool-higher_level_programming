-- Usin the hbtn_0d_tvshows db in school project
SELECT score, COUNT(*) AS number 
FROM second_table 
GROUP BY score 
ORDER BY number DESC;

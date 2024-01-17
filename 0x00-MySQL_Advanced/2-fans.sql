-- SQL script that creates a table users

-- Creating table users
SELECT origin, COUNT(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

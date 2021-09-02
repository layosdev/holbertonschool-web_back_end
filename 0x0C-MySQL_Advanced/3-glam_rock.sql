-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT m.band_name, ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands m
WHERE m.style LIKE '%Glam rock%'
ORDER BY lifespan DESC;

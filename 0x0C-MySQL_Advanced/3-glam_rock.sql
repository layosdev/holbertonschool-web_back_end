-- 3 first students in the Batch ID=3
SELECT band_name,
	ifnull(split, YEAR(CURDATE())) - formed as lifespan
FROM metal_bands
WHERE style LIKE "%Glam rock%"
ORDER BY lifespan DESC;
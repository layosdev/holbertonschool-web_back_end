-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id int)
BEGIN
    UPDATE users 
    SET average_score = (SELECT AVG(score) FROM corrections as avid WHERE avid.user_id=user_id)
    WHERE id = user_id;
END;
//
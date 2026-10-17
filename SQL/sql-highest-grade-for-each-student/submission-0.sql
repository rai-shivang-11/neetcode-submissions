-- Write your query below
SELECT student_id, min(exam_id) as exam_id, score FROM exam_results
GROUP BY student_id, score
HAVING (student_id, score) in (SELECT student_id, max(score) as score FROM exam_results GROUP BY student_id)
ORDER BY student_id ASC
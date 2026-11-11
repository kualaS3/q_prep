-- LC 1148 Article Views I
-- Accepted on LeetCode 2026-11-11
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;

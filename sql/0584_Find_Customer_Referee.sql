-- LC 584 Find Customer Referee
-- Accepted on LeetCode 2026-11-11
SELECT name FROM Customer WHERE referee_id != 2 OR referee_id IS NULL;

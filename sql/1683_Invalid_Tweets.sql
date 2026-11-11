-- LC 1683 Invalid Tweets
-- Accepted on LeetCode 2026-11-11
SELECT tweet_id FROM Tweets WHERE LENGTH(content) > 15;

-- LC 595 Big Countries
-- Accepted on LeetCode 2026-11-11
SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;

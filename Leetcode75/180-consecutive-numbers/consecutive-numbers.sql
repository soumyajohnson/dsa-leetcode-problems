-- Write your PostgreSQL query statement below
SELECT DISTINCT num as  ConsecutiveNums 
FROM ( 
    SELECT num,
        LEAD(num,1) OVER (ORDER BY id) as next1,
        LEAD(num,2) OVER (ORDER BY id) as next2
    FROM Logs
) tmp
WHERE num=next1 AND num=next2;

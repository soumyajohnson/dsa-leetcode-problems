-- Write your PostgreSQL query statement below
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d
ON e.departmentId=d.id
JOIN (
    SELECT departmentId, salary
    FROM  (
        SELECT DISTINCT departmentId, salary,
        DENSE_RANK() OVER (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) AS sals
        FROM Employee
    ) tmp
    WHERE sals<=3
) tmp2
ON tmp2.departmentId=e.departmentId
WHERE e.salary = tmp2.salary;
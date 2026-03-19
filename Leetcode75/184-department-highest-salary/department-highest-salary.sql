-- Write your PostgreSQL query statement below
SELECT d.name AS Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d
ON e.departmentId=d.id
JOIN (
    SELECT departmentId,max(salary) AS max_sal FROM Employee
    GROUP BY departmentId
) tmp
ON d.id=tmp.departmentId
AND e.salary=tmp.max_sal

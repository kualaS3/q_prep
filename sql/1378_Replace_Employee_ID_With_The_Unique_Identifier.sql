-- LC 1378 Replace Employee ID With The Unique Identifier
SELECT name, unique_id
FROM Employees
LEFT JOIN EmployeeUNI ON Employees.id = EmployeeUNI.id;

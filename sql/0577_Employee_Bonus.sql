SELECT name, bonus 
FROM Employee
LEFT JOIN Bonus ON Employee.empID = Bonus.empID
WHERE Bonus.bonus < 1000 or Bonus.bonus IS NULL

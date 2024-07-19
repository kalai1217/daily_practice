-- Create tables
use students
CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY,
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    DepartmentID INT,
    Salary DECIMAL(10, 2)
);

CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName NVARCHAR(50)
);

-- Insert records
INSERT INTO Employees (EmployeeID, FirstName, LastName, DepartmentID, Salary) VALUES
(1, 'John', 'Doe', 1, 60000.00),
(2, 'Jane', 'Smith', 2, 75000.00),
(3, 'Mike', 'Johnson', 1, 80000.00),
(4, 'Emily', 'Davis', 3, 65000.00),
(5, 'Anna', 'Brown', 2, 70000.00);

INSERT INTO Departments (DepartmentID, DepartmentName) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

-- Subquery example
SELECT 
    FirstName, 
    LastName, 
    Salary
FROM 
    Employees
WHERE 
    Salary > (SELECT AVG(Salary) FROM Employees);

-- CTE example
WITH DepartmentSalary AS (
    SELECT 
        d.DepartmentName,
        e.Salary
    FROM 
        Employees e
    JOIN 
        Departments d ON e.DepartmentID = d.DepartmentID
)
SELECT 
    DepartmentName, 
    AVG(Salary) AS AverageSalary
FROM 
    DepartmentSalary
GROUP BY 
    DepartmentName;

-- Conditional Aggregations example
SELECT 
    DepartmentID,
    SUM(CASE WHEN Salary > 70000 THEN Salary ELSE 0 END) AS HighSalaries,
    SUM(CASE WHEN Salary <= 70000 THEN Salary ELSE 0 END) AS LowSalaries
FROM 
    Employees
GROUP BY 
    DepartmentID;

-- Stored Procedure example
CREATE PROCEDURE GetEmployeesByDepartment
    @DepartmentID INT
AS
BEGIN
    SELECT 
        EmployeeID, 
        FirstName, 
        LastName, 
        Salary
    FROM 
        Employees
    WHERE 
        DepartmentID = @DepartmentID;
END;

-- Execute the stored procedure
EXEC GetEmployeesByDepartment @DepartmentID = 2;

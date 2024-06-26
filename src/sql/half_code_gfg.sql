SELECT * FROM students
--1. Write a SQL query to fetch “FIRST_NAME” from the Student table in upper case and use ALIAS name as STUDENT_NAME.
SELECT UPPER(FIRST_NAME) AS STUDENT_NAME FROM STUDENTS
--2. Write a SQL query to fetch unique values of MAJOR Subjects from Student table.
SELECT DISTINCT(MAJOR) FROM STUDENTS
SELECT MAJOR FROM STUDENTS GROUP BY MAJOR
--3. Write a SQL query to print the first 3 characters of FIRST_NAME from Student table.
SELECT SUBSTRING(FIRST_NAME,1,3) FROM STUDENTS
--4. Write a SQL query to find the position of alphabet (‘a’) int the first name column ‘Shivansh’ from Student table.
SELECT CHARINDEX('A',FIRST_NAME) FROM STUDENTS WHERE FIRST_NAME='Shivansh'
--5. Write a SQL query that fetches the unique values of MAJOR Subjects from Student table and print its length.
SELECT DISTINCT  MAJOR , LEN(MAJOR) AS LENGTH_OF_SUBJECT FROM STUDENTS
--6. Write a SQL query to print FIRST_NAME from the Student table after replacing ‘a’ with ‘A’.
SELECT REPLACE(FIRST_NAME,'a','A') as replaced_names from students
--7. Write a SQL query to print the FIRST_NAME and LAST_NAME from Student table into single column COMPLETE_NAME.
SELECT CONCAT(FIRST_NAME,' ',LAST_NAME) AS CONCATENATED_STRING FROM STUDENTS
--8. Write a SQL query to print all Student details from Student table order by FIRST_NAME Ascending and MAJOR Subject descending .
SELECT * FROM STUDENTS ORDER BY FIRST_NAME , MAJOR DESC
--9. Write a SQL query to print details of the Students with the FIRST_NAME as ‘Prem’ and ‘Shivansh’ from Student table.
SELECT * FROM STUDENTS WHERE FIRST_NAME IN ('prem','shivansh')
--10. Write a SQL query to print details of the Students excluding FIRST_NAME as ‘Prem’ and ‘Shivansh’ from Student table.
SELECT * FROM STUDENTS WHERE FIRST_NAME  NOT IN ('prem','shivansh')
--11. Write a SQL query to print details of the Students whose FIRST_NAME ends with ‘a'
select * from students where FIRST_NAME like '%a'
--12. Write an SQL query to print details of the Students whose FIRST_NAME ends with ‘a’ and contains six alphabets.
select * from students where FIRST_NAME like '_____a'
--13. Write an SQL query to print details of the Students whose GPA lies between 9.00 and 9.99.
select * from students where gpa between 9.00 and 9.99
--14. Write an SQL query to fetch the count of Students having Major Subject ‘Computer Science’.
select count(*) from students where major='computer science'
--15. Write an SQL query to fetch Students full names with GPA >= 8.5 and <= 9.5.
select concat(first_name,' ',last_name) as full_name from students where gpa between 8.5 and 9.5
--16. Write an SQL query to fetch the no. of Students for each MAJOR subject in the descending order.
select major, count(*) from students group by major order by major desc
--17. Display the details of students who have received scholarships, including their names, scholarship amounts, and scholarship dates.

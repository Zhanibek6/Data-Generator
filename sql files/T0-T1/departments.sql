CREATE TABLE departments(
   dept_id   VARCHAR(12) NOT NULL PRIMARY KEY
  ,dept_name VARCHAR(18) NOT NULL
);
INSERT INTO dbo.departments(dept_id,dept_name) VALUES ('DEPT_SALES','Sales');
INSERT INTO dbo.departments(dept_id,dept_name) VALUES ('DEPT_MAIN','Maintenance');
INSERT INTO dbo.departments(dept_id,dept_name) VALUES ('DEPT_SUPPORT','Support');
INSERT INTO dbo.departments(dept_id,dept_name) VALUES ('DEPT_CANCEL','Anti-Cancellation');

--
--  Script that creates the 'sample' tables, views, procedures,
--  functions, triggers, etc.
--

--
--  Create and load tables used in the documentation examples.

--
--  Create the 'department' table
--
CREATE TABLE department (
 department_no   INTEGER NOT NULL PRIMARY KEY
,department_name VARCHAR(14) UNIQUE
,location        VARCHAR(13)
);

--
--  Create the 'employee' table
--
CREATE TABLE employee (
 employee_no     INTEGER NOT NULL PRIMARY KEY
,employee_name   VARCHAR(10)
,job             VARCHAR(9)
,manager_no      INTEGER
,hire_date       DATE
,salary          INTEGER CHECK (salary > 0)
,comm            INTEGER
,department_no   INTEGER REFERENCES department(department_no)
);

--
--  Create the 'jobhist' table
--
CREATE TABLE jobhist (
 employee_no     INTEGER NOT NULL REFERENCES employee(employee_no) ON DELETE CASCADE
,start_date      DATE NOT NULL
,end_date        DATE
,job             VARCHAR(9)
,salary          INTEGER
,comm            INTEGER
,department_no   INTEGER REFERENCES department (department_no) ON DELETE SET NULL
,chgdesc         VARCHAR(80)
,PRIMARY KEY (employee_no, start_date)
,CHECK (start_date <= end_date)
);

--
--  Load the 'department' table
--
INSERT INTO department VALUES
 (10, 'ACCOUNTING', 'NEW YORK')
,(20, 'RESEARCH',   'DALLAS')
,(30, 'SALES',      'CHICAGO')
,(40, 'OPERATIONS', 'BOSTON')
;

--
--  Load the 'employee' table
--
INSERT INTO employee VALUES
 (7369, 'SMITH',  'CLERK',     7902, '17-DEC-80', 800,  NULL, 20)
,(7499, 'ALLEN',  'SALESMAN',  7698, '20-FEB-81', 1600, 300,  30)
,(7521, 'WARD',   'SALESMAN',  7698, '22-FEB-81', 1250, 500,  30)
,(7566, 'JONES',  'MANAGER',   7839, '02-APR-81', 2975, NULL, 20)
,(7654, 'MARTIN', 'SALESMAN',  7698, '28-SEP-81', 1250, 1400, 30)
,(7698, 'BLAKE',  'MANAGER',   7839, '01-MAY-81', 2850, NULL, 30)
,(7782, 'CLARK',  'MANAGER',   7839, '09-JUN-81', 2450, NULL, 10)
,(7788, 'SCOTT',  'ANALYST',   7566, '19-APR-87', 3000, NULL, 20)
,(7839, 'KING',   'PRESIDENT', NULL, '17-NOV-81', 5000, NULL, 10)
,(7844, 'TURNER', 'SALESMAN',  7698, '08-SEP-81', 1500, 0,    30)
,(7876, 'ADAMS',  'CLERK',     7788, '23-MAY-87', 1100, NULL, 20)
,(7900, 'JAMES',  'CLERK',     7698, '03-DEC-81', 950,  NULL, 30)
,(7902, 'FORD',   'ANALYST',   7566, '03-DEC-81', 3000, NULL, 20)
,(7934, 'MILLER', 'CLERK',     7782, '23-JAN-82', 1300, NULL, 10)
;

--
--  Load the 'jobhist' table
--
INSERT INTO jobhist VALUES
 (7369, '17-DEC-80', NULL,        'CLERK',     800,  NULL, 20, 'New Hire')
,(7499, '20-FEB-81', NULL,        'SALESMAN',  1600, 300,  30, 'New Hire')
,(7521, '22-FEB-81', NULL,        'SALESMAN',  1250, 500,  30, 'New Hire')
,(7566, '02-APR-81', NULL,        'MANAGER',   2975, NULL, 20, 'New Hire')
,(7654, '28-SEP-81', NULL,        'SALESMAN',  1250, 1400, 30, 'New Hire')
,(7698, '01-MAY-81', NULL,        'MANAGER',   2850, NULL, 30, 'New Hire')
,(7782, '09-JUN-81', NULL,        'MANAGER',   2450, NULL, 10, 'New Hire')
,(7788, '19-APR-87', '12-APR-88', 'CLERK',     1000, NULL, 20, 'New Hire')
,(7788, '13-APR-88', '04-MAY-89', 'CLERK',     1040, NULL, 20, 'Raise')
,(7788, '05-MAY-90', NULL,        'ANALYST',   3000, NULL, 20, 'Promoted to Analyst')
,(7839, '17-NOV-81', NULL,        'PRESIDENT', 5000, NULL, 10, 'New Hire')
,(7844, '08-SEP-81', NULL,        'SALESMAN',  1500, 0,    30, 'New Hire')
,(7876, '23-MAY-87', NULL,        'CLERK',     1100, NULL, 20, 'New Hire')
,(7900, '03-DEC-81', '14-JAN-83', 'CLERK',     950,  NULL, 10, 'New Hire')
,(7900, '15-JAN-83', NULL,        'CLERK',     950,  NULL, 30, 'Changed to Department 30')
,(7902, '03-DEC-81', NULL,        'ANALYST',   3000, NULL, 20, 'New Hire')
,(7934, '23-JAN-82', NULL,        'CLERK',     1300, NULL, 10, 'New Hire')
;

--
--  Populate statistics table and view (pg_statistic/pg_stats)
--
ANALYZE department;
ANALYZE employee;
ANALYZE jobhist;

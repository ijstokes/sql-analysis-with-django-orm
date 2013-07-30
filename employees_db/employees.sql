--  Sample employee database 
--  See changelog table for details
--  Copyright (C) 2007,2008, MySQL AB
--  
--  Original data created by Fusheng Wang and Carlo Zaniolo
--  http://www.cs.aau.dk/TimeCenter/software.htm
--  http://www.cs.aau.dk/TimeCenter/Data/employeeTemporalDataSet.zip
-- 
--  Current schema by Giuseppe Maxia 
--  Data conversion from XML to relational by Patrick Crews
-- 
-- This work is licensed under the 
-- Creative Commons Attribution-Share Alike 3.0 Unported License. 
-- To view a copy of this license, visit 
-- http://creativecommons.org/licenses/by-sa/3.0/ or send a letter to 
-- Creative Commons, 171 Second Street, Suite 300, San Francisco, 
-- California, 94105, USA.
-- 
--  DISCLAIMER
--  To the best of our knowledge, this data is fabricated, and
--  it does not correspond to real people. 
--  Any similarity to existing people is purely coincidental.
-- 

DROP TABLE IF EXISTS dept_emp;
DROP TABLE IF EXISTS dept_manager;
DROP TABLE IF EXISTS titles;
DROP TABLE IF EXISTS salaries; 
DROP TABLE IF EXISTS employees; 
DROP TABLE IF EXISTS departments;

CREATE TABLE employees (
    emp_no      INTEGER         NOT NULL,
    birth_date  DATE            NOT NULL,
    first_name  VARCHAR(14)     NOT NULL,
    last_name   VARCHAR(16)     NOT NULL,
    gender      CHAR(1)         NOT NULL,    
    hire_date   DATE            NOT NULL,
    PRIMARY KEY (emp_no)
);

-- gender: M or F

CREATE TABLE departments (
    dept_idx    INTEGER         NOT NULL,
    dept_no     VARCHAR(4)      NOT NULL,
    dept_name   VARCHAR(40)     NOT NULL,
    UNIQUE  (dept_name),
    PRIMARY KEY (dept_idx)
);

CREATE TABLE dept_manager (
    mgr_idx     INTEGER        NOT NULL,
    dept_idx    INTEGER        NOT NULL,
    emp_no      INTEGER        NOT NULL,
    from_date   DATE           NOT NULL,
    to_date     DATE           NOT NULL,
    FOREIGN KEY (emp_no)   REFERENCES employees   (emp_no)   ON DELETE CASCADE,
    FOREIGN KEY (dept_idx) REFERENCES departments (dept_idx) ON DELETE CASCADE,
    PRIMARY KEY (mgr_idx)
); 

CREATE TABLE dept_emp (
    deptemp_idx INTEGER         NOT NULL,
    emp_no      INTEGER         NOT NULL,
    dept_idx    INTEGER        NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no)  REFERENCES employees   (emp_no)  ON DELETE CASCADE,
    FOREIGN KEY (dept_idx) REFERENCES departments (dept_idx) ON DELETE CASCADE,
    PRIMARY KEY (deptemp_idx)
);

CREATE TABLE titles (
    titles_idx  INTEGER         NOT NULL,
    emp_no      INTEGER         NOT NULL,
    title       VARCHAR(50)     NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (titles_idx)
); 

CREATE TABLE salaries (
    salary_idx  INTEGER         NOT NULL,
    emp_no      INTEGER         NOT NULL,
    salary      INTEGER         NOT NULL,
    from_date   DATE            NOT NULL,
    to_date     DATE            NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (salary_idx)
); 

.read 'load_departments.dumpnew'
.read 'load_employees.dumpnew'
.read 'load_dept_emp.dumpnew'
.read 'load_dept_manager.dumpnew'
.read 'load_titles.dumpnew'
.read 'load_salaries.dumpnew'

CREATE TABLE Patientsdb (
    name VARCHAR(255),
    ID INT PRIMARY KEY,
    City VARCHAR(255),
    State VARCHAR(255),
    DOB DATE,
    Email VARCHAR(255),
    PHnumb BIGINT
);

CREATE TABLE Staff (
    Name VARCHAR(255),
    ID INT PRIMARY KEY,
    City VARCHAR(255),
    Department VARCHAR(255),
    DOB DATE,
    Email VARCHAR(255),
    PHnumb BIGINT
);

CREATE TABLE BillDetails (
    Name VARCHAR(255),
    ID INT PRIMARY KEY,
    City VARCHAR(255),
    State VARCHAR(255),
    DOB DATE,
    Email VARCHAR(255),
    Cost DECIMAL(10, 2)
);

CREATE TABLE SalaryDetails (
    Name VARCHAR(255),
    ID INT PRIMARY KEY,
    Salary DECIMAL(10, 2)
);

CREATE TABLE Medical (
    Name VARCHAR(255),
    ID INT PRIMARY KEY,
    Price DECIMAL(10, 2),
    Origin VARCHAR(255),
    Rating FLOAT
);

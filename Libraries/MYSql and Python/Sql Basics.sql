use  nit;

create table student (
name varchar(30),
id int not null primary key,
address varchar(50),
marks int
);


select * from student;

desc student;

#Secure way
insert into student(marks,address,id,name) values(85,'Hyderabad',1,'SairamVenkat');
#insecure way
insert into student value ('Subrahmanaya',2,'Hyderabad',85);

insert into student value ('Ravi',3,'Hyderabad',85),
('Krishna',4,'Hyderabad',85),
('Satya',5,'Hyderabad',85),
('Lakshmi Narasimha',6,'Hyderabad',85),
('Hanumath',7,'Hyderabad',85),
('Koti',8,'Hyderabad',85),
('Triyumabakeshwara',9,'Hyderabad',85),
('Sharma',10,'Hyderabad',85)
;

select name,id from student  where id=2;
select * from student;
update student set address ="Chennai" where id=2;


alter table student add phonenumber varchar(20) ;
update student set phonenumber ="+91 7417038967" where id!=5;

alter table student modify column name varchar(100);
alter table student drop column phonenumber;

SELECT @@hostname; 
SHOW VARIABLES LIKE 'hostname';
SELECT HOST FROM information_schema.processlist WHERE ID = connection_id();

select sum(marks) as 'Count Of Marks'  from student;
select avg(marks) as 'Avg Of Marks'  from student;
select count(name) as 'Names Count'  from student;
select max(marks) as 'Max Marks'  from student;
select min(marks) as 'Min Marks'  from student;

select * from student order by marks desc;
select * from student order by marks asc;
select * from student order by marks;

# Wild Card Characters
# Like 
# % one or more charcters
# _  for any wild charcter at specific pos

select * from student where name like 'saikrishna%';
select * from student where name like '%venkat';
# to get  records where a specific character is present at specific position
select * from student where name like '_a%';  # here data of 2nd charcter is a in name
select * from student where marks like '8%%';  


# Date and Time 

select current_date();
select current_date()+02;

create table Employee (
id int not null primary key,
salary int,
empcode int,
name varchar(30),
address varchar(50)
);


insert into Employee values(1,25000,1,'SairamVenkat','Hyd');
insert into Employee values(2,15000,1,'Ravi','Hyd');
insert into Employee values(3,35000,1,'Krishna','Hyd');
insert into Employee values(4,45000,1,'Swarna','Hyd');


select id from Employee;
select id from student;

# Inner Join
select e.* from Employee e
inner join student s
on
e.id=s.id;

#Left Join

select * from Employee e
left join student s
on
e.id=s.id;


# Right  Join

select * from Employee e
right join student s
on
e.id=s.id;

#Cross Join
SELECT * 
FROM student 
CROSS JOIN employee;

SELECT * 
FROM employee 
CROSS JOIN student;








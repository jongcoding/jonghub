create table emp_new(
    empno number(10) primary key,
    ename varchar2(20),
    sal number(10)
);

-- 데이터 삽입
insert into emp_new values(1000, '임베스트', 20000);
insert into emp_new values(1001, '조조', 20000);
insert into emp_new values(1002, '관우', 20000);
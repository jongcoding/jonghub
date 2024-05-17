select deptno, sum(sal) from emp_dept
where mgr between 1000 and 1003
group by deptno
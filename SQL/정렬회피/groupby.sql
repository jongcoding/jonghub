SELECT deptno, sum(sal)
from emp_dept
group by deptno
SELECT deptno, mgr, AVG(sal)
from emp_dept
group by deptno, mgr;
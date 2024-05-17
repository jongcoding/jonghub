SELECT dept, mgr, sum(sal)
from emp_dept
group by dept
having sum(sal)>=5000;
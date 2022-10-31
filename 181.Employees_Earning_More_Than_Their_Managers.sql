-- Write an SQL query to find the employees who earn more than their managers.

-- Return the result table in any order
        
        select e.name as Employee 

        from employee m, employee e
        
        where 
                m.id = e.managerId and e.managerId is not null 
                
        and     m.salary < e.salary 
          
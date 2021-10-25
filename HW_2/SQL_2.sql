1. Вывести всех работников чьи зарплаты есть в базе, вместе с зарплатами.

select employee_name, monthly_salary
from employees join employees_salary
on employees.id = employees_salary.employee_id;

2. Вывести всех работников у которых ЗП меньше 2000.

select employee_name, monthly_salary
from employees join employees_salary
on employees.id = employees_salary.employee_id
where monthly_salary < 2000;

3. Вывести все зарплатные позиции, но работник по ним не назначен. (ЗП есть, но не понятно кто её получает.)

select employee_name, monthly_salary
from employees full join employees_salary
on employees.id = employees_salary.employee_id
where employee_name is null;

4. Вывести все зарплатные позиции  меньше 2000 но работник по ним не назначен. (ЗП есть, но не понятно кто её получает.)

select employee_name, monthly_salary
from employees full join employees_salary
on employees.id = employees_salary.employee_id
where monthly_salary < 2000 and employee_name is null;

5. Найти всех работников кому не начислена ЗП.

select employee_name, monthly_salary
from employees full join employees_salary
on employees.id = employees_salary.employee_id
where monthly_salary is null;

6. Вывести всех работников с названиями их должности.

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id;

7. Вывести имена и должность только Java разработчиков.

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
where role_name like '%Java%'


8. Вывести имена и должность только Python разработчиков.

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
where role_name like '%Python%';



9. Вывести имена и должность всех QA инженеров.

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
where role_name like '%QA%';



10. Вывести имена и должность ручных QA инженеров.

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
where role_name like '%Manual QA%';



11. Вывести имена и должность автоматизаторов QA

select employee_name, role_name
from employees join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
where role_name like '%Automation QA%';



12. Вывести имена и зарплаты Junior специалистов

select employee_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%Junior%';


13. Вывести имена и зарплаты Middle специалистов

select employee_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%Middle%';



14. Вывести имена и зарплаты Senior специалистов

select employee_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%Senior%';



15. Вывести зарплаты Java разработчиков

select role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name in ('Junior Java developer', 'Middle Java developer', 'Senior Java developer');



16. Вывести зарплаты Python разработчиков

select role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name in ('Junior Python developer', 'Middle Python developer', 'Senior Python developer');



17. Вывести имена и зарплаты Junior Python разработчиков

select role_name, employee_name, monthly_salary
from employees 
full join roles_employees
on employees.id = roles_employees.employee_id
full join roles 
on roles_employees.role_id = roles.id
full join employees_salary
on employees.id = employees_salary.employee_id
where role_name = 'Junior Python developer';



18. Вывести имена и зарплаты Middle JS разработчиков

select role_name, employee_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name = 'Middle JavaScript developer';



19. Вывести имена и зарплаты Senior Java разработчиков

select role_name, employee_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name = 'Senior Java developer';


20. Вывести зарплаты Junior QA инженеров

select role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name = 'Junior Manual QA engineer';




21. Вывести среднюю зарплату всех Junior специалистов

select AVG(monthly_salary)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%Junior%';



22. Вывести сумму зарплат JS разработчиков

select sum(monthly_salary)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%JavaScript%';



23. Вывести минимальную ЗП QA инженеров

select min(monthly_salary)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%QA%';



24. Вывести максимальную ЗП QA инженеров

select max(monthly_salary)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%QA%';



25. Вывести количество QA инженеров

select count(roles_employees)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%QA%';


26. Вывести количество Middle специалистов.

select count(roles_employees)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%Middle%';



27. Вывести количество разработчиков

select count(role_id)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%developer%';



28. Вывести фонд (сумму) зарплаты разработчиков.

select sum(monthly_salary)
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where role_name like '%developer%';



29. Вывести имена, должности и ЗП всех специалистов по возрастанию

select employee_name, role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
order by monthly_salary asc;



30. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП от 1700 до 2300

select employee_name, role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
order by monthly_salary asc;



31. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП меньше 2300

select employee_name, role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where monthly_salary < 2300
order by monthly_salary asc;



32. Вывести имена, должности и ЗП всех специалистов по возрастанию у специалистов у которых ЗП равна 1100, 1500, 2000


select employee_name, role_name, monthly_salary
from employees 
join roles_employees
on employees.id = roles_employees.employee_id
join roles 
on roles_employees.role_id = roles.id
join employees_salary
on employees.id = employees_salary.employee_id
where monthly_salary in ('1100', '1500', '2000')
order by monthly_salary asc;


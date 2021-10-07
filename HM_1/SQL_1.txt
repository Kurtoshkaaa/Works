select * from qa_users;                             

select username, user_id from qa_users;

select user_id from qa_users;

select username from qa_users;

select email from qa_users;

select user_id, username, email, created_on from qa_users;

select * from qa_users 
where password='12333';

select * from qa_users
where created_on = '2021-03-26 00:00:00';

select * from qa_users
where username like 'Anna%';

select * from qa_users
where username like '%8';

select * from qa_users
where username like '%a%';

select * from qa_users
where created_on = '2021-07-12 00:00:00';

select * from qa_users
where created_on = '2021-07-12 00:00:00' and password = '1m313';

select * from qa_users
where created_on = '2021-07-12 00:00:00' and username LIKE 'Andrey%';

select * from qa_users
where created_on = '2021-07-12 00:00:00' and username LIKE '%8%';

select * from qa_users
where user_id = 10;

select * from qa_users
where user_id = 53;

select * from qa_users
where user_id > 40;

select * from qa_users
where user_id < 30;

select * from qa_users
where user_id < 27 or user_id > 88;

select * from qa_users
where user_id <= 37;

select * from qa_users
where user_id >= 37;

select * from qa_users
where user_id > 80 and user_id < 90;

select * from qa_users
where user_id between 80 and 90;

select * from qa_users
where created_on in ('2020-10-03 00:00:00', '2021-05-19 00:00:00', '2021-03-26 00:00:00');

select min(user_id)
from qa_users;

select max(user_id)
from qa_users;

select count(user_id)
from qa_users;

select user_id, username, created_on
from qa_users
order by created_on;

select user_id, username, created_on
from qa_users
order by created_on DESC;

# SQL Test Assignment

Attached is a mysqldump of a database to be used during the test.

Below are the questions for this test. Please enter a full, complete, working SQL statement under each question. We do not want the answer to the question. We want the SQL command to derive the answer. We will copy/paste these commands to test the validity of the answer.

**Example:**

_Q. Select all users_

- Please return at least first_name and last_name

SELECT first_name, last_name FROM users;


------

**— Test Starts Here —**

1. Select users whose id is either 3,2 or 4
- Please return at least: all user fields

	Select * from users where id in (3,2,4)

2. Count how many basic and premium listings each active user has
- Please return at least: first_name, last_name, basic, premium

	Select U.first_name, U.last_Name, 
	Count(Distinct Case when L.status = 2 then L.id END) basic, 
	Count(Distinct Case when L.status = 3 then L.id END) premium 
	from users U 
	inner join listings L on U.id = L.user_id
	where U.status = 2  
	group by U.id

3. Show the same count as before but only if they have at least ONE premium listing
- Please return at least: first_name, last_name, basic, premium

	Select U.first_name, U.last_Name, 
	Count(Distinct Case when L.status = 2 then L.id END) basic, 
	Count(Distinct Case when L.status = 3 then L.id END) premium 
	from users U 
	inner join listings L on U.id = L.user_id
	where U.status = 2
	group by U.id 
	having Count(Distinct Case when L.status = 3 then L.id END) > 0


4. How much revenue has each active vendor made in 2013
- Please return at least: first_name, last_name, currency, revenue

	Select u.first_name, u.last_name, c.currency, sum(c.price) revenue from clicks c
	join listings l on c.listing_id = l.id
	join users u on l.user_id= u.id
	where year(c.created) = 2013 and u.status = 2 
	group by u.id, c.currency

5. Insert a new click for listing id 3, at $4.00
- Find out the id of this new click. Please return at least: id

	INSERT INTO clicks(listing_id, price, created)
	Values (3, 4.00, now())
	Select Last_Insert_Id()

6. Show listings that have not received a click in 2013
- Please return at least: listing_name

	Select DISTINCT(l.name) from clicks c
	join listings l on c.listing_id = l.id
	where l.name NOT IN (Select l.name from clicks c
	join listings l on c.listing_id = l.id
	where year(c.created) = 2013)

7. For each year show number of listings clicked and number of vendors who owned these listings
- Please return at least: date, total_listings_clicked, total_vendors_affected

	Select DISTINCT(year(c.created)) date, COUNT(DISTINCT(l.id)) total_listings_clicked, 
	COUNT(DISTINCT(u.id)) total_vendors_affected from clicks c
	inner join listings l on c.listing_id = l.id
	inner join users u on l.user_id = u.id
	group by year(c.created)

8. Return a comma separated string of listing names for all active vendors
- Please return at least: first_name, last_name, listing_names

	SELECT u.first_name, u.last_name, GROUP_CONCAT(l.name) listing_names  FROM users u
	join listings l on u.id = l.user_id 
	where u.status = 2
	group by u.id;
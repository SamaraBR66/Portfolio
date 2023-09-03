
#SAMARA BECERRA
select rating, AVG (replacement_cost)
from film
group by rating
order by rating DESC;

#SAMARA BECERRA
SELECT rating, MAX(rental_rate), MIN(rental_rate),
	avg(rental_rate), SUM(rental_rate), COUNT(rental_rate), COUNT(*)
FROM film 
group by rating
having  avg(rental_rate) >3;

#SAMARA BECERRA
SELECT rating, avg (replacement_cost)
FROM film
WHERE length >119
GROUP BY rating
HAVING avg(replacement_cost);

##HAVING BY "is for the extra buckets"
#Find products ID by category
#https://www.w3schools.com/sql/trysql.asp?filename=trysql_select_groupby
SELECT COUNT (ProductID), CategoryID
FROM Products 
GROUP BY CategoryID;

#This one joins the categories table and shows the categ name 

SELECT c.CategoryName, COUNT(p.SupplierID)
FROM products p
JOIN categories c ON p.CategoryID = c.CategoryID
GROUP BY c.CategoryID;

#In class exercise SELECT c.categoryname, COUNT(*)
FROM products p
JOIN categories c ON p.CategoryID = c.CategoryID
WHERE p.price > 20
GROUP BY c.CategoryID
HAVING COUNT(*) >5;

#Construct a query that counts the number of rows in the payment table.
SELECT COUNT(*)
FROM payment;
# count the number of payments made by each customer. 
#Show the customer_id and the total amount paid for each customer.
SELECT COUNT(*), SUM(amount),customer_id
FROM payment
GROUP BY customer_id;

# include only those customers who have at least 40 payments.
SELECT COUNT(*), SUM(amount),customer_id
FROM payment
GROUP BY customer_id
HAVING COUNT(*) >= 40;


#Highest replacement cost for any movie?

SELECT max(replacement_cost)
FROM film;

#Titles that all share this highest replacement cost 
SELECT title
FROM film
WHERE replacement_cost = 29.99;

#AVG replacement cost for movies which rentak rate equals .99
SELECT avg(replacement_cost)
FROM film
WHERE rental_rate = 0.99;

#1 The business wants to offer a deal for those customers who have rented at least 5 times and a total of at least $100
SELECT customer_id, SUM(amount) AS total
FROM payment
GROUP BY customer_id
HAVING COUNT(*)>=5 AND SUM(amount) >=100;

#2
SELECT * 
FROM film;

#2 As the store manager I need to know on average what store is making the highest profit leaving out the films that cost 0.99 to rent 
SELECT  st.store_id, AVG(amount)
FROM payment p
JOIN staff s
ON p.staff_id= s.staff_id
JOIN store st
ON s.store_id = st.store_id
WHERE amount != 0.99
GROUP BY st.store_id
ORDER BY SUM(amount) desc;




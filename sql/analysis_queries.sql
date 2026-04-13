-- 1. Basic Data Preview
SELECT *
FROM `your_project.customer_curated.customers`
LIMIT 10;


-- 2. Customer Segmentation
SELECT 
  customer_segment, 
  COUNT(*) AS total_customers
FROM `your_project.customer_curated.customers`
GROUP BY customer_segment
ORDER BY total_customers DESC;


-- 3. Region Analysis
SELECT 
  region, 
  COUNT(*) AS total
FROM `your_project.customer_curated.customers`
GROUP BY region
ORDER BY total DESC;


-- 4. Email Domain Insight
SELECT 
  email_domain, 
  COUNT(*) AS users
FROM `your_project.customer_curated.customers`
GROUP BY email_domain
ORDER BY users DESC;

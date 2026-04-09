SELECT
  product,
  SUM(sales) AS total_sales
FROM `your_project.dataset.clean_table`
GROUP BY product
ORDER BY total_sales DESC;

SELECT COUNT(*) as total_count, COUNT(fruit) as non_null_count,
       MIN(fruit) as min, MAX(fruit) as max
FROM (SELECT NULL as fruit UNION ALL
      SELECT "apple" as fruit UNION ALL
      SELECT "pear" as fruit UNION ALL
      SELECT "orange" as fruit)
sel

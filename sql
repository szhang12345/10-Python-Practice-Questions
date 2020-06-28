SELECT COUNT(*) as total_count, COUNT(fruit) as non_null_count,
       MIN(fruit) as min, MAX(fruit) as max
FROM (SELECT NULL as fruit UNION ALL
      SELECT "apple" as fruit UNION ALL
      SELECT "pear" as fruit UNION ALL
      SELECT "orange" as fruit)
with table a （）

    l = lambda x:len(str(x))
    for i in range(20):
        if l(809*i)==4 and l(8*i)==2 and l(9*i)==3:
            x = i
            print(x)
    print(809*x==800*x+9*x)
    print(809*x)

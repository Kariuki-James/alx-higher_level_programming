-- display average temperature by `city` ordered by `temperatures.value`
SELECT `state`, MAX(`value`) AS 'max_temp'
FROM `temperatures`
GROUP BY `state`
ORDER BY `state` ASC;

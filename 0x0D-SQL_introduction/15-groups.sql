-- lists number of records with the same `score` from `second_table`
SELECT `score`, COUNT(`score`) AS "score"
FROM `second_table`
GROUP BY `score`;

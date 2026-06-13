-- 7-max_state.sql
SELECT state, max(value) as max_temp
GROUP BY state
ORDER BY 1;

SELECT FOOD_TYPE, 
        REST_ID, 
        REST_NAME,
        FAVORITES
FROM (
    SELECT 
        FOOD_TYPE, 
        REST_ID, 
        REST_NAME,
        FAVORITES,
        ROW_NUMBER() OVER (
            PARTITION BY FOOD_TYPE
            ORDER BY FAVORITES DESC
        ) AS RN
    FROM REST_INFO
) t 
-- t => FROM (SELECT ...)를 썼으면 뒤에 반드시 별칭(아무거나 가능) 붙이기 !!!!!!!
WHERE RN = 1
ORDER BY FOOD_TYPE DESC;

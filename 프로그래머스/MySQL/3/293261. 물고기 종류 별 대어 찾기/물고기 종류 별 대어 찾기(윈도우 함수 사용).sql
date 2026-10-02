-- FISH_TYPE별로 !!!행을 유지한 채!!! ROW_NUMBER로 길이 순위를 매긴 후
-- FISH_NAME_INFO와 JOIN하여 종류별 1위 물고기의 이름을 조회

SELECT a.ID, b.FISH_NAME, a.LENGTH
FROM (
    SELECT ID,
            FISH_TYPE,
            LENGTH,
            ROW_NUMBER() OVER(
                PARTITION BY FISH_TYPE
                ORDER BY LENGTH DESC
            ) AS RN
    FROM FISH_INFO
) a
JOIN FISH_NAME_INFO b
    ON (a.FISH_TYPE = b.FISH_TYPE)
WHERE RN = 1
ORDER BY a.ID;

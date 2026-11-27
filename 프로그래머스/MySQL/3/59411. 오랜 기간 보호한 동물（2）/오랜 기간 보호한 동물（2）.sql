-- 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문
-- 결과는 보호 기간이 긴 순으로 조회

SELECT o.ANIMAL_ID, o.NAME
FROM ANIMAL_INS i
JOIN ANIMAL_OUTS o
    ON i.ANIMAL_ID = o.ANIMAL_ID
ORDER BY DATEDIFF(o.DATETIME, i.DATETIME) DESC
LIMIT 2;




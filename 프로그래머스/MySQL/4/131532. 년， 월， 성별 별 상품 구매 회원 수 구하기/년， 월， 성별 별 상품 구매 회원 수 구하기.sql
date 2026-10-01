-- 쇼핑몰에 가입한 회원 정보를 담은 USER_INFO 
-- 온라인 상품 판매 정보를 담은 ONLINE_SALE
-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계하는 SQL문을 작성
-- 1. 결과는 년, 월, 성별을 기준으로 오름차순 정렬
-- 2. 이때, 성별 정보가 없는 경우 결과에서 제외

SELECT YEAR(o.SALES_DATE) AS YEAR, MONTH(o.SALES_DATE) AS MONTH, u.GENDER, COUNT(DISTINCT u.USER_ID) AS USERS
FROM USER_INFO u
JOIN ONLINE_SALE o
    ON (
        u.USER_ID = o.USER_ID
    )
WHERE u.GENDER IS NOT NULL
GROUP BY YEAR, MONTH, u.GENDER
ORDER BY YEAR, MONTH, u.GENDER
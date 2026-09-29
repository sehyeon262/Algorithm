-- 2022년 1월의 카테고리 별 도서 판매량을 합산하고, 카테고리(CATEGORY), 총 판매량(TOTAL_SALES) 리스트를 출력하는 SQL문 작성
-- 결과는 카테고리명을 기준으로 오름차순 정렬

SELECT b.CATEGORY, SUM(s.SALES) AS TOTAL_SALES
FROM BOOK b
LEFT JOIN BOOK_SALES s
    ON b.BOOK_ID = s.BOOK_ID
WHERE 
    SUBSTRING(s.SALES_DATE, 1, 7) = '2022-01'        
GROUP BY b.CATEGORY
ORDER BY b.CATEGORY
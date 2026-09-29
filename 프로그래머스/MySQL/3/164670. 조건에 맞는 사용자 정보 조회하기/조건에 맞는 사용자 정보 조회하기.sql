-- '중고 거래 게시물을 3건 이상 등록한 사용자'의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문
-- 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 
-- 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
-- 결과는 회원 ID를 기준으로 내림차순 정렬

SELECT u.USER_ID, u.NICKNAME,
CONCAT_WS(
    ' ',
    u.CITY,
    u.STREET_ADDRESS1,
    u.STREET_ADDRESS2	
) AS 전체주소,
CONCAT(
    SUBSTRING(u.TLNO, 1, 3), '-',
    SUBSTRING(u.TLNO, 4, 4), '-',
    SUBSTRING(u.TLNO, 8, 4)
) AS 전화번호
FROM USED_GOODS_USER u
LEFT JOIN USED_GOODS_BOARD b
    ON u.USER_ID = b.WRITER_ID
GROUP BY b.WRITER_ID
HAVING COUNT(b.WRITER_ID) >= 3
ORDER BY USER_ID DESC;
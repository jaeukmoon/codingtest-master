"""
[0535] Encode and Decode TinyURL (Medium)
https://leetcode.com/problems/encode-and-decode-tinyurl/

## 문제

`Codec` 클래스를 구현:
- `encode(longUrl)`: 긴 URL을 짧은 URL로 인코딩
- `decode(shortUrl)`: 짧은 URL을 원래의 긴 URL로 디코딩

조건: encode 결과를 decode하면 원래 URL이 나와야 한다.

## 예시

Example 1:
    Input:  url = "https://leetcode.com/problems/design-tinyurl"
    Output: "https://leetcode.com/problems/design-tinyurl"
    Explanation:
        encoded = codec.encode(url)
        decoded = codec.decode(encoded)
        decoded == url

## 조건 (Constraints)

- 1 <= url.length <= 10^4
- url은 유효한 URL 형태

## Hint (설계 자유도 큼)

- 단순한 방법: 카운터 기반 ID + dict 매핑
- 좀 더 정교한 방법: 무작위 short code 생성 + 충돌 처리
"""


class Codec:
    def __init__(self):
        pass

    def encode(self, longUrl: str) -> str:
        pass

    def decode(self, shortUrl: str) -> str:
        pass


if __name__ == "__main__":
    codec = Codec()
    url = "https://leetcode.com/problems/design-tinyurl"
    encoded = codec.encode(url)
    decoded = codec.decode(encoded)
    print(decoded == url)   # True

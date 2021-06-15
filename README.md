
# Programmers
이 레포는 프로그래머스 연습문제를 푼 자료와 함께, 제가 풀며 배운 알고리즘 스킬들을 기록해 놓는 곳입니다.
======

## 2진수 관련 코드

### 라이브러리 사용없이 변환하기
```
tmp = ''
    while i:
        tmp += str(i % n)
        i = i // n

```

### 10진수를 2진수로 변환하여 string문자열로 변환
```
bin(num) 

```

## 문자열 처리

<<<<<<< HEAD
###공백을 채우는 rjust
=======
### 공백을 채우는 rjust
>>>>>>> 4a4668306fe1caa36a54eaafb6dc2d27e00fc3d5

```
rjust (필요한 문자열의 길이, 공백을 채울 문자)

ex) a = '1001'
    a = a.rjust(6,'0')
    
    print(a)
    #001001
```
<<<<<<< HEAD
=======

## 정규표현식
### 문자 클래스
#### 문자 클래스 []
문자 클래스 []는 "[]사이의 문자들과 매치"라는 의미이다.
만약 정규표현식 [abc]라면 

    "a"는 정규식과 일치하는 문자인 "a"가 있으므로 매치
    "before"는 정규식과 일치하는 문자인 "b"가 있으므로 매치
    "dude"는 정규식과 일치하는 문자인 a, b, c 중 어느 하나도 포함하고 있지 않으므로 매치되지 않음

[] 안에 하이픈(-)을 넣으면 범위를 나타낸다.


#### 문자 클래스 Dot(.)
문자 클래스 Dot(.)은 \n을 제외한 모든 문자와 매치됨을 의미한다.
만약 정규표현식 a.b라면

    "aab"는 가운데 문자 "a"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
    "a0b"는 가운데 문자 "0"가 모든 문자를 의미하는 .과 일치하므로 정규식과 매치된다.
    "abc"는 "a"문자와 "b"문자 사이에 어떤 문자라도 하나는있어야 하는 이 정규식과 일치하지 않으므로 매치되지 않는다.

 
 #### 반복 (*)
 * 는 반복되는 문자와 매치됨을 의미한다.
 만약 ab*의 경우
 
    "ab"는 "b"가 0번 반복되어 매치된다.
    "abb"는 "b"가 0번 이상 반복되어 매치된다.
    
#### 반복 (+)
+ 는 최소 한번 이상 반복되는 문자와 매치됨을 의미한다.
 만약 ab+의 경우
 
    "ab"는 "b"가 0번 반복되어 매치되지 않는다.
    "abb"는 "b"가 0번 이상 반복되어 매치된다.

#### 반복 ({m,n}, ?}
{} 메타 문자는 반복횟수를 지정할 수 있다. 예를 들어 {2,4}라면, 2번이상 4번이하 반복되는 문자만 매치된다.

 만약 ab{2}의 경우
 
    "ab"는 "b"가 0번 반복되어 매치되지 않는다.
    "abb"는 "b"가 2번 반복되어 매치된다.
    
 반복은 아니지만 비슷한 개념으로는 ?가 있는데, ?는 {0,1}을 의미한다.
 따라서 있거나, 없거나 둘다 매치된다.
 
 ### 정규표현식을 사용하기 위한 re모듈
 1. match() : 문자열의 처음부터 정규식과 매치되는지 조사한다.
 2. search() : 문자열 전체를 검색하여 정규식과 매치되는지 조사한다.
 3. findall() : 정규식과 매치되는 모든 문자열을 리스트로 돌려준다.
 4. finditer() : 정규식과 매치되는 모든 문자열을 반복 가능한 객체로 돌려준다.
 
 re모듈의 사용을 위해선 re라이브러리를 import 해준뒤, 표현식을 compile해주어야 한다.
 
```
>>> import re
>>> p = re.compile('[a-z]+')
```
 
 #### match()
 match 메서드는 문자열이의 처음부터 정규식과 매치되는지를 조사한다.
 ```
>>> m = p.match("python")
>>> print(m)
<_sre.SRE_Match object at 0x01F3F9F8>
```

"python" 문자열은 [a-z]+ 정규식에 부합하므로, match 객체가 반환된다.

```
>>> m = p.match("3 python")
>>> print(m)
None
```

"3 python" 문자열은 처음에 오는 3이 정규식에 부합되지 않으므로 None 객체가 반환된다.
이러한 match의 특성을 이용해 보통 if else문에 사용되는데, 사용방법은 아래와 같다.

```
p = re.compile(정규표현식)
m = p.match( 'string goes here' )
if m:
    print('Match found: ', m.group())
else:
    print('No match')
```

#### search()
search 메서드는 문자열을 처음부터 검색하는 것이 아닌, 전체를 검색하는 메서드이다.

```
>>> m = p.search("3 python")
>>> print(m)
<_sre.SRE_Match object at 0x01F3FA68>
```

"3 python"은 3이 앞에 오지만, search는 match와 다르게 문자열 전체를 검색하므로,
뒤에 오는 "python"이 이 정규표현식을 만족시키므로 매치된다.

#### findall()
findall 메서드는 문자열의 띄어쓰기를 분리하여, 리스트로 돌려주는 메서드이다.

```
>>> result = p.findall("life is too short")
>>> print(result)
['life', 'is', 'too', 'short']
```

위와 같이 문장으로 된 문자열을 각각 [a-z]+ 문자열과 매칭하여 리스트로 돌려준다.

#### finditer()
이번에는 finditer 메서드를 수행해 보자.

```
>>> result = p.finditer("life is too short")
>>> print(result)
<callable_iterator object at 0x01F5E390>
>>> for r in result: print(r)
...
<_sre.SRE_Match object at 0x01F3F9F8>
<_sre.SRE_Match object at 0x01F3FAD8>
<_sre.SRE_Match object at 0x01F3FAA0>
<_sre.SRE_Match object at 0x01F3F9F8>
```
finditer는 findall과 동일하지만 그 결과로 반복 가능한 객체를 돌려준다.
"life" "is" "too" "short"를 각각 반복가능한 객체로, r에 대입하여 매치되는지를 확인할 수 있다.
>>>>>>> 4a4668306fe1caa36a54eaafb6dc2d27e00fc3d5

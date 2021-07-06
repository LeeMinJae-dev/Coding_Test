
# Coding_Test
이 레포는 코딩테스트 연습문제들을 푼 자료와 함께, 문제를 풀며 배운 알고리즘 스킬들을 기록해 놓는 곳입니다.
## 함수 사용법
### try, except 문
try, except문은 예외나 오류를 처리하는데, 이를 이용해서 입력이 끝날때까지
값을 받는 방식으로 코딩을 할 수 있다.
```
>>>while 1:
        try:
            i = input()
        except:
            break
    
```
### for ~ else 문
for else 문은 for문이 break에 걸리지 않았을 때는 else가 실행되고, break에 걸려서
for문을 탈출하게 되면 else가 실행되지 않는 함수이다.
```
>>>for x in range(4):
    if x == 2:
        print ('loop out')
        break
    else:
        print ('loop end')
```
break에 걸렸으므로 else가 실행되지 않아 loop out이 실행되고,
```
for x in range(4):
  # nop
  pass
else:
  print ('loop end')

```
break가 없으므로 else가 실행되어 loop end가 출력된다.

## 리스트 처리 코드
### 리스트 슬라이싱 ::
::는 리스트를 슬라이싱할때 일정 개수씩 띄어서 슬라이싱하거나 뒤집을 때 사용한다.
[::n]의 경우
```
>>> a = [1,2,3,4]
>>> a[::2]
a = 1,3
```
[::2]로 2칸씩 슬라이싱 한것을 볼 수 있다.

```
>>>a[1,2,3,4]
>>> a[::-1]
a = [5,4,3,2,1]
```
[::-1]은 주어진 리스트를 뒤집어서 슬라이싱 하는것을 알 수 있다.
### 리스트의 데이터타입을 바꿔주는 map()
```
>>> n = ['1','2','3']
>>> n = list(map(int, n))
n = [1,2,3]
```
### 리스트가 비었는지 확인해주는 not()
```
>>> a= []
>>> not(a)
True
```
### 리스트를 sorted를 사용하여 key를 기준으로 정렬하기
어떠한 기준으로 리스트를 정렬하여야 할때, sorted메서드의 key를 이용하면 쉽게 정렬할 수 있다.
abe, abc, cxc를 2번째 글자를 기준으로 정렬 할 경우,
```
>>> sorted(strings,key=lambda x:x[n])
[abe, abc, cxc]
```
이렇게 하면 2번째 글자를 기준으로 정렬을 알아서 해준다.

만약 두가지 기준을 가진 정렬의 경우, 예를들어 2번째 글자를 기준후로 정렬후, 2번째 글자가 같은 문자열은 사전순으로 정렬 하여야 하는경우, lambda의 조건을 하나 더 두면 알아서 첫번째 기준으로 정렬 후 두번째 기준으로 정렬해준다.

```
>>> sorted(strings,key=lambda x:(x[n],x))
[abc, abe, cxc]
```
## 수학 관련 코드
### 최대공약수를 구해주는 gcd()
fractions 라이브러리에 있는 gcd() 메서드는 두 매개변수의 최대공약수를 구해준다.
```
>>> gcd(3,12)
3
```
### 유클리드 호제법
유클리드 호제법은 두수의 최대공약수를 구하는 공식이다.
ex) 1071과 1029의 최대공약수를 구하면,
    1071은 1029로 나누어떨어지지 않기 때문에, 1071을 1029로 나눈 나머지를 구한다. ≫ 42
    1029는 42로 나누어떨어지지 않기 때문에, 1029를 42로 나눈 나머지를 구한다. ≫ 21
    42는 21로 나누어떨어진다.

```
>>> c, d = max(a, b), min(a, b)
>>> t = 1
>>> while t > 0:
        t = c % d
        c, d = d, t
```
### 최소공배수
a와 b의 최공배수는 a*b를 최대공약수로 나눈것이다.
따라서 a*b/최대공약수

### 에라토스테네스의 체
```
>>> def solution(n):
        num=set(range(2,n+1))

        for i in range(2,n+1):
            if i in num:
                num-=set(range(i*i,n+1,i))
        return len(num)
    
```

## 문자열 처리

### 문자를 입력받는 input()
변수를 외부로 부터 입력받고 싶을 때는 input()을 쓴다.
만약 a를 입력으로 받고싶다면,
```
>>> a = input()
```
위와 같이 하면된다.
## 진수 관련 코드

### 진수를 변환해주는 재귀함수

```
>>> def convert(n, base):
        T = "0123456789ABCDEF"

        q, r = divmod(n, base)

        if q == 0:
            return T[r]
        else:
            return convert(q, base) + T[r]
    
```
이 함수는 divmod로 몫과 나머지를 받아 몫이 0이 될때까지 함수가 자신을
재참조 하면서 나머지를 T의 인덱스로 받아 문자열로 출력하는 진수변환 함수이다.


### 라이브러리 사용없이 변환하기
```
>>> tmp = ''
>>> while i:
        tmp += str(i % n)
        i = i // n

```

### 10진수를 2진수로 변환하여 string문자열로 변환
```
>>> bin(num) 

```

## 문자열 처리
### 문자열 맨 앞글자를 대문자로 바꿔주는 capitalize()
```
>>> s = 'abc'
>>> s.capitalize()
'Abc'
```
### 문자열의 데이터타입을 바꿔주는 map()
```
>>> n = "12345"
>>> map(int, n)
n = 12345
```

### 문자가 숫자인지 판단하는 함수 isdigit()

ex) 
```
>>> s = "123"
>>> s.isdigit()
True

```

### 공백을 채우는 rjust
만약, 두개의 수를 받고싶다면,
```
>>> a,b = input()
```
이고, 입력은 ab이렇게 원하는 수를 붙여서 대입한다. 만약 입력방식은 a b이렇게 중간이나 
왼쪽, 오른쪽에 공백을 두어도 알아서 대입하기를 원한다면,
```
>>> a,b = input().strip().split()

```
이렇게 코드를 짜주면, 들어온값의 양쪽공백을 제거(strip())하고, 
글자사이의 공백을 기준으로 나누어 각각 a,b에 대입하게된다. 


## 내장 함수 라이브러리
### import sys
#### 가장 작은 수, 가장 큰 수 maxsize
크기를 서로 비교하는 함수를 작성할때, 들어올 수 있는 값들이 다양해 초깃값을 설정하기가 어려울때는, maxsize 메서드를 사용하여 초깃값을 지정하면 시스템이 갖는 가장 높은 값, 혹은 가장 낮은 값을 초깃값으로 둘 수 있다.
```
mx = sys.maxsize #최댓값
mx = -sys.maxsize #최솟값

```

#### for문에서 input() 대신 사용하는 sys.stdin.readline()
for 문에서는 input()을 사용하여 입력을 받으면 시간초과가 일어날 수 있기 때문에,
input 대신에 stdin.readline()을 사용해야 한다.

### import re
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
>>> p = re.compile(정규표현식)
>>> m = p.match( 'string goes here' )
>>> if m:
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

#### split()
split() 메서드는 정규표현식을 기준으로 문자를 나눠주는 메서드이다.

```
>>> re.split('[0-9]+','python3hello')
['python','hello']
```
기준으로 나눈 문자도 포함하고 싶다면 ( )를 정규표현씩에 씌워주면 된다. 
```
>>> re.split('[0-9]+','python3hello')
['python','3,'hello']
```

### import collections
#### collections.Counter()
Counter는 리스트안에 있는 원소들의 종류를 나누어 그 원소들이 몇번씩 반복되었는지를 각각 키와 밸류로 반환한 딕셔너리 타입으로 알려주는 메서드이다.

```
>>> from collections import Counter
>>> a = [1,1,2,2,2,3]
>>> Counter(a)
Counter({1: 2, 2: 3, 3: 1})
```
위처럼 1은 2개, 2는 3개, 3은 1개의 정보를 담은 딕셔너리로 반환된다.

#### collections.Counter().most_common()
most_common은 가장 개수가 많은, 즉 밸류의 값이 높은 원소를 출력한다.
```
>>> from collections import Counter
>>> a = [1,1,2,2,2,3]
>>> Counter(a).most_common(1)
[(2, 3)]
```
most_common의 매개변수를 1로 하면 가장 밸류가 높은 원소 하나, 2로 하면 두개가 출력된다.

#### collections.defaultdict()
defaultdict()는 딕셔너리에 없는 키값을 호출할때 오류가 발생하는 것을 막아주기 위해 호출한 키값이 없으면 알아서 패스해주는 딕셔너리를 선언하게 해주는 메서드이다.
```
>>> dic = collections.defaultdict(int)
>>> dic
defaultdict(int, {})

>>> dic['a'] 
>>> dic
defaultdict(int, {'a': 0})

>>> dic['b'] = 1
>>> dic
defaultdict(int, {'a': 0, 'b': 1})

```
defaultdic()의 인자로 int를 주면 키값만을 호출했을때 0을 밸류로 저장하고,
list로 주면 빈리스트인 [ ], set()을 주면 빈 집합인 {}로 저장해준다.

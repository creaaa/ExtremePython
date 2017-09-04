
## __name__ と "__main__"

# __name__ には、スクリプトとして起動した際に、"__main__" という値が入る。
# 別のモジュールから呼び出された時には、自身のモジュール名が入る(ので実行されない)

# 「スクリプトとして直接呼び出した時のみ実行し、
# 別のモジュールから呼び出された時（インポート）には実行しない」という条件になる
# if __name__ == '__main__':
# 	print("from main!!")


## ユーザから入力を受付
"""
print("let me know your name")
yourName = input(">> ")
print(yourName)
"""


## array モジュール (あえて使うメリットは?? いまはどうでもよい。)

# import array
# print(array.array("u", 'hello world'))


# コマンドライン引数
# もちろん ちゃんと管理しないと out of range発生するので注意。

# import sys

# args = sys.argv

# print(args)
# print(args[0])  # 実行ファイル名
# print(args[1])  # 第一引数
# print(args[2])  # 第二引数


## プログラムの終了

# import sys
# sys.exit()


## インポート

"""
import testmod  # ファイル名がモジュール名となる、ということか...

# モジュール名.クラス名でインスタンス化
myTestClass1 = testmod.TestClass()
myTestClass1.test_method(42)

# 毎回、「モジュール名.クラス名」と書くのはダルいあなたに
# これにより、クラス名だけで使用可能になる
from testmod import TestClass

myTestClass2 = TestClass()
myTestClass2.test_method("Unison Square Guaden")

# モジュール内に定義されている関数・変数なんかもfromでインポート可能
from testmod import globalValue
from testmod import oreoreFunc

print(globalValue)  # 42
oreoreFunc()        # Ore!!
"""

# 別名定義

"""

import another as an
an.hello("Advent Calender")
an.goodbye( an.year )

# 注意: importされるファイルに実行コマンド(トップレベルのコマンド)が描かれていると、
# インポートした時点でそれが実行される。
# Swiftと違って main.swift以外にも実行命令が書け、実際にコンパイルエラーにならず実行されてしまう。

# 防ぐには、 another.py (インポートされるファイル内)で

if __name__ == '__main__':
    print("Hello from another.py")

# と、if __name__ == '__main__': の中で実行コマンドを書けば良い。


# どこからインポートされているのかを確認したければ、

import Special
print( Special.__path__ )

で見れる。


"""





# 制御構造

## if

# 複数条件は and / or で

"""
value1 = "Python3"
value2 = "Swift"

if value1 == "Python3" and value2 == "Swift":
	# print("perfect!!")
	# "なにもしない"場合は、 pass が必要
	pass
elif value1 == "Python" or value2 == "Swift":
	print("so so...")
"""

# ついにこれができる言語に初めて会ってしまった...
"""
x = 42
if 40 < x < 44:
	print("mazika!!!")

# もいっちょついでに、三項演算子

y = "hello" if False else "byebye"
print(y)
"""

## for文

# すなわち、文字列は、シーケンス([]をサポート)であるとともに、
# "反復可能オブジェクト(for文で使用可能)" という、2つの性質を持つ

"""
for char in "Hi World":
	print(char)  # H i   W o r l d

# こんなのもできる

multiAry = [["http", "www"], ["Python", "Swift"]]

for value1, value2 in multiAry:
	# http www
	# Python Swift
	print(value1, value2) 

count = 0
while count < 5:
	print(count)
	count += 1
"""


## switch文… は、Pythonには存在しない！マジか！大胆やな...

# もちろん工夫の余地は存在する。たとえば、これは str 2回書くのダルいので...

"""
myStr = "a"

if myStr == 'a' or myStr == 'b':
    print('a,b')
elif myStr == 'c':
    print('c')

# こう書く

# タプル(a,b) だけでなく、リスト [a,b]、辞書 {a.b} でも全部いける
if myStr in ("a", "b"):
	print("a,b")
elif myStr == "c":
	print("c")
"""


## is と == の違い

# == は、オブジェクト同士が等価(同じ値)かどうかを判定する演算子

# リストは、要素の順序が違えば等価ではない

# == はオーバーロードして、等価判定をねじまげられる。

# is

# オブジェクトを生成すると、他のオブジェクトと重複しない一意の番号を保持する。
# これは id() で取得できる。
# is は、これを比較し、「同じオブジェクト(同一)かどうか」を判定する

# st = "hello"
# print(id(st))  # 4384929248

# これにより、「等価だが同一ではない」みたいな関係が誕生しうる。
# 要は多言語における == と === と同じやな。

# print(st is st)  # True

# Noneかどうか、は is を用いる！

# 理由1: == よりも is のほうが速い
# 理由2: == はオーバーロードできるので、想定外がおこりうる

# None = 「何もない状態」を表すオブジェクト。 NoneType. IDも持つ。

# NoneのIDは、プログラム開始から終了まで、一個だけしか存在しない(=シングルトン)。
# オブジェクトにNoneが代入された時点で、すべてのオブジェクトは"Noneオブジェクト"として一括りにされる。

# == のオーバーロード

# == 演算子は、そのオブジェクト(クラス)が定義している[__eq__]メソッドの結果を見る。
# (__eq__が定義されてない場合は、最上位のobjectクラスの__eq__の結果は利用するが、
# これは is と同じく、"id" を比較している)

"""
class TestClass:
	pass

c1 = TestClass()
c2 = TestClass()

print(c1 == c2)  # False
print(c1 is c2)  # False

# すなわち、独自クラスは、独自の__eq__を定義しない限り、
# == と is は同じ結果となる。
# == は __eq__を経由し、かつその処理は is と同じことしてるだけなので、
# is で比較したほうが速い。
# では、 == のオーバーロード、すなわち、独自の __eq__を定義しよう

class TestClass:
	
	def __eq__(self, other):
		return True

c1 = TestClass()

print(c1 == None)  # True(ヤバ...)
print(c1 is None)  # False(よかった...)
"""


## 文字列オブジェクト

# 文字列の型は、2系ではunicodeとstrの2種類あったのが、
# 3系では unicodeのみに統一された

# st = "hello"
# print(type(st)) # <class 'str'> とデルが、内部的には unicode型(strと統合された)。

### クオート3つで複数行！

'''
testStr = """
test1
test2
test3!!
print(testStr)
"""
'''

"""
### 文字列へ変換
testInt = 100
print(str(testInt) + " yen")

### 置換
testStr1 = "Python-izm"
print(testStr1.replace("izm", "ism"))

### 分割

testStr2 = "Python-izm"
# split()の引数のデフォルト値はスペース。空白で分割できるっつー話。
print(testStr2.split("-"))  # 結果はリストで返る

### 検索

str.startswith("")  # Boolで返る

### 大文字・小文字変換

str.upper()
str.lower()
"""

### 文字列 + 数字の足し算は不可

"""
stock = 13
# だめ。TypeError
# "stock:" + stock


stock = 13
print("stock:" + str(stock))

# 地味に型に厳格なのな...
"""

### format

"""
stock = 42
print('stock: {:d}'.format(stock))
"""


## 数値オブジェクト

### 数値変換

"""
testStr = "100"
print(int(testStr))   # 失敗するとValueErrorになる
print(float(testStr)) # 100.0 
"""

## 日付オブジェクト

# import datetime でOK.

"""
import datetime
print(datetime.date.today())     # 2017-09-03
print(datetime.datetime.today()) # 2017-09-03 16:15:40.878370

print(type(datetime.date.today())) # 'datetime.date'

print(datetime.date.today().year)  # 2017
print(datetime.date.today().month) # 9
print(datetime.date.today().day)   # 3

# 他にhour, minute, second, microsecond などがある

"""

## Pythonの配列

# リスト [] : 要素の追加・削除可
# タプル () : 要素の追加・削除不可
# 辞書  {}  : 要素の追加・削除可だが、同じkeyは持てない
# セット    :  要素の追加・削除可だが、同じ要素は持てない


# タプル 

"""
import datetime

def get_today():

	today = datetime.date.today()
	return (today.year, today.month, today.day)  # タプル

result = get_today()

print(result)     # (2017, 9, 3)
print(result[0])  # 2017
print(result[1])  # 9
print(result[2])  # 3
"""

## シーケンス型

# タプル・リスト・文字列など。[]を使って各要素にアクセス可能。
# Swiftでいうところの Collectionプロトコルやな


## リスト

"""
### 追加

myList = []
print(myList)  # []

myList.append("12")
myList.append(24)
myList.append(True)

print(myList)  # ['12', 24, True]

### 引数に渡した要素の数
print(myList.count(24))  # 1
"""

## ディクショナリ

"""
myDict = {"Year": 2010, 'Month': "9", "Day": False}
# print(myDict)  # {'Year': 2010, 'Month': '9', 'Day': False} めちゃくちゃやな...

# for key in myDict:
# 	print(key)          # keyが取得できるので...
# 	print(myDict[key])  # これで value が取れる

# print(myDict["USG"])  ## キーが存在しない場合はKeyErrorで死ぬ

### valueはこれでも取れるし、メリットがある

print(myDict.get("Year"))  # 2010
print(myDict.get("Boke"))  # None (KeyErrorにならない)
print(myDict.get("Boke", 'NotFound'))  # キーが存在しない場合の出力を指定

### 要素の削除 (なんでここでいきなり大局関数になるんだよ...)
del(myDict["Month"])
print(myDict)  # {'Year': 2010, 'Day': False}


### keyだけ or valueだけ取得

print(myDict.keys())   # dict_keys(['Year', 'Day'])
print(myDict.values()) # dict_values([2010, False])

# key と value を同時取得

for key, value in myDict.items():
	print("res: ", key, value)

# 指定のキーを保持しているかを確認
print("Year" in myDict)   # True
print("Years" in myDict)  # False
"""

## 辞書の辞書

# { "coca cola": {"total": 320, "count": 2}, "coffee": {"total": 360, "count": 3} }



## セット


## リスト操作

"""
list = [2,6,3,8]

for x in list:
	print(x)                #=> 2, 6, 3, 8

print([x**2 for x in list]) #=> 4, 36, 9, 64

print([x for x in list if x>4]) #=> 6, 8
"""


## 内包表記

# リスト・辞書をシンプルに作成する方法

### リスト内包表記

# comp_list = [<式> for <変数> in <反復可能オブジェクト>]

# comp_list = [i for i in range(5)]
# print(comp_list)  # [0,1,2,3,4]

# ↑ はこれと同じ
# comp_list = []
# for i in range(5):
# 	comp_list.append(i)
# print(comp_list)

# こんなこともできる。mapみてぇだな
# comp_list = [str(i * i) for i in range(5)]
# print(comp_list)


### ディクショナリ内包表記

# comp_dict = { <式(key:value)> for <変数> in <反復可能オブジェクト> }

# comp_dict = {str(i): i * i for i in range(5)}
# print(comp_dict)

# ↓ と同じ
# comp_dict = {}
# for i in range(5):
# 	comp_dict[str(i)] = i * i
# print(comp_dict)


# set内包表記

# comp_set = {<式> for <変数> in <反復可能オブジェクト>}

# comp_set = {str(i*i) for i in range(5)}
# print(comp_set)

# # ↓ と同じ
# comp_set = set()
# for i in range(5):
# 	comp_set.add(str(i*i))
# print(comp_set)


### forのネスト
# comp_list = [i * ii for i in range(1,10) for ii in range(1,10)]
# print(comp_list)

# # ↓ と同じ
# comp_list = []
# for i in range(1,10):
# 	for ii in range(1,10):
# 		comp_list.append(i*ii)
# print(comp_list)


### ifとの併用

# comp_list = [i for i in range(5) if i % 2 == 0]
# print(comp_list)  # [0,2,4]


### タプル内包表記

# んなもんはない。下記のように書くとタプルではなくジェネレータを生成する

# gen = (i for i in range(10))
# print(gen)


# ラムダ式

# normal

# def plus(num1, num2):
# 	return num1 + num2

# print(plus(42, 1))

# # lambda

# lambdaPlus = lambda num1, num2: num1 * num2

# print(lambdaPlus(20, 10))


# UUIDを生成
# import uuid
# print(uuid.uuid4())


# 環境変数の取得

# import os

# for env in os.environ:
# 	print(env)

# ## 特定の環境変数を取得（ないと None と出る）
# print(os.environ.get('HOME'))


# range

# for i in range(10):
# 	print(i) # 0 1 2 3 4 5 6 7 8 9

# for i in range(1, 10):
# 	print(i) # 1 2 3 4 5 6 7 8 9, すなわちSwiftの 1..<10 みたいな感じ


# 関数の基礎

# def testFunc():
#     print("called")

# testFunc()

# 引数にはデフォルト値を設定可能
# def testFunc2(num1, num2, calcType=1):
	
# 	if calcType == 1:
# 		print("plus!")
# 		print(num1 + num2)

# 	elif calcType == 2:
# 		print("minus!")
# 		print(num1 - num2)

# 	else:
# 		print("error!")

# testFunc2(42, 1)
# testFunc2(42, 1, 2)
# testFunc2(42, 1, 3)


## ジェネレータ(yield)

# "ジェネレータ関数" と "ジェネレータ式" があり、
# 単にジェネレータといった場合、前者のジェネレータ関数を指す

# ジェネレータとは、反復可能なオブジェクト。
# forに使えるが、リスト等と異なる点は、"その都度、必要な分だけ"値を生成して返す 点にある


# この時点で　myGeneratorは"ジェネレータ関数"となっている
# def myGenerator():
	
# 	yield("otohasu")
# 	yield("mariri")
# 	yield("haru")
# 	yield("annu")


# こうすれば値を取得できる
# for i in myGenerator():
# 	print(i)

# 他にもこんな方法が
# f = myGenerator()
# print(f) # generator object

# print(next(f))  # otohasu
# print(next(f))  # mariri
# print(next(f))  # haru
# print(next(f))  # annu

# エラー。
# 余談だが、for文でジェネレータがぴったり止まるのは、
# この例外を捕捉してループ脱出する処理を行っているから
# print(next(f))  # StopIteration error

# この書き方もできるっていってるが、うそやんけ
# print(f.next())

# ジェネレータ式とは、
# いわば「タプル内包表記」によって、ジェネレータを生成すること

# gen = (i for i in "goodmorning hello goodnight".split())

# for i in gen:
# 	print(i)

# こうしても、ジェネレータ関数オブジェクトそのものがprintされるだけ
# print(myGenerator())


















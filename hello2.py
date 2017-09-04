
# 関数の可変長引数

# 可変長引数は、関数内においてタプルとして渡される。
# argsは、割と暗黙の慣習なので、従ったほうが無難

"""
def testFunc(*args):
	print(args)

testFunc(1, 2, 3, 4, 5) # (1, 2, 3, 4, 5)

# ** をつけると、ディクショナリとして渡される。
# kargs というのも暗黙の慣習っぽい。 
def testFunc2(**kargs):
	print(kargs)

# {'code': 100, 'name': 'Python'}
testFunc2(code = 100, name = "Python")

# * と ** は併用可能。すげぇな...
"""


# プロパティの定義

# property関数を使う方法と @property を使う方法がある

# property関数

"""
class MyProperty:

	def __init__(self, url):
		self._url = url

	def get_url(self):
		return self._url

	# 関数オブジェクトを渡す(適用はしない点に注意)
	# 第一引数しかないため、getterのみ。
	# つまり url は readonly なので、更新しようとするとエラーになる
	
	# これが「プロパティ」。インスタンス属性とは異なるもの。
	# あー、だからこの2つを峻別する目的で、
	# インスタンス属性のほうには _ (アンダーバー)つけるんや。うーむ...
	url = property(get_url)

prop = MyProperty("http://yahoo.co.jp")
print(prop.url)

# setしようとするとエラー。
# prop.url = "http://google.co.jp"  # AttributeError: can't set attribute


class Another:

	def __init__(self, url):
		self._url = url

	def get_url(self):
		return self._url

	def set_url(self, url):
		self._url = url

	def del_url():
		del self._url

	url = property(get_url, set_url, del_url, "url property")

prop = Another("hoge.txt")
# setterへアクセス
prop.url = "fuga.txt"

# 変わっている
print(prop.url)   # fuga.txt
# 結局これもできるんかい。。。
print(prop._url)  # fuga.txt


class YetAnother:

	def __init__(self, url):
		self._url = url

	# 関数に @property を付与すると、その関数はgetterとなる
	@property
	def url(self):
		return self._url

	# setter, deleterを定義する方法はこう
	@url.setter
	def url(self, url):
		self._url = url

	@url.deleter
	def url(self):
		del self._url


prop = YetAnother("pero1.txt")
print(prop.url)
prop.url = "pero2.txt"  # AttributeError: can't set attribute
print(prop.url)
"""

# クラス作成

"""
class TestClass:
	
	# ここでの code, name を、「インスタンス属性(変数)」という言い方をする。
	# Swiftのインスタンスプロパティ = Pythonの「インスタンス属性」。
	# つまり、プロパティという扱いではない点に注意。

	def __init__(self, code, name):
		self.code = code
		self.name = name

classes = []

# これ、第１引数のselfは常に暗黙的に渡ってる、だから意識しなくてもよい、って仕様なのか...?
classes.append(TestClass(1, "test 1"))
classes.append(TestClass(2, "test 2"))

for cl in classes:
	print("code: ", str(cl.code))
	print("name: ", cl.code)


# __init__ について

# self は、「クラスのインスタンス自身」
# __init__に限らず、インスタンスメソッドは self は省略できない

# うーん...微妙やけど、プロパティへのアクセスを言語レベルで明示することを強制している、
# と思えば悪くはないが...うーん...


## 継承 (2系)

class Country:

	def __init__(self, name):
		self.name = name

	def hoge(self):
		print("hoge---!!")


class City(Country):

	def __init__(self, countryName, cityName):

		# 2系旧の書き方
		# Country.__init__(self, countryName)

		# 2系新。やっぱ断然こっちでしょ。と思いきやこっちも相当キモかった
		# super(City, self).__init__(countryName)

		# 3系.
		super().__init__(countryName)


		self.cityName = cityName

	def hoge(self):

		# 2系旧スタイル。実はまだこっちも動く。
		# Country.hoge()

		# 2系新スタイル。これは相当キモいな。。
		# super(City, self).hoge()

		# 3系。なんだ、いけるやん...
		# super().hoge()



classes = []
classes.append(City("Japan", "Tokyo"))
classes.append(City("USA", "Washington"))


for cl in classes:
	print("country: " + cl.name)
	print("city: "    + cl.cityName)

print(type(City))  # <class 'type'> メタクラスへの入り口か...??

classes[0].hoge()
"""


# メソッド一覧

"""
class TestClass:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def instance(self, arg1):
		if arg1:
			print("arg is {}".format(self.x))

	@classmethod
	def classmethod(cls, arg1):
		pass

	@staticmethod
	def staticmethod(arg1):
		pass


## インスタンスメソッドの実行
myClass = TestClass(200, 50)

# 外部引数名(ラベル)はこう書く
myClass.instance(arg1 = True)
"""


## クラスメソッド・スタティックメソッド

"""
import datetime

class TestClass:

	def __init__(self, year, month, day):
		self.year  = year
		self.month = month
		self.day   = day

	@classmethod
	def classmethod(cls, date_diff=0):
		
		today = datetime.date.today()
		# d => <class 'datetime.date'>
		d = today + datetime.timedelta(days=date_diff)

		# ここの文法は今は謎
		return cls(d.year, d.month, d.day)

	@staticmethod
	def staticmethod(x, y):
		return x + y



## クラスメソッド

# cls は「クラス自身」を表す。名前は強制ではないが、暗黙のルール。
# なにげに datetime.date.today もクラスメソッドである。

# <class '__main__.TestClass'> なんやこれ
myClass = TestClass.classmethod()
print(myClass.year, myClass.month, myClass.day)  # (2017, 9, 3)

myClass = TestClass.classmethod(-10)
print(myClass.year, myClass.month, myClass.day)  # (2017, 8, 24)

myClass = TestClass(2016, 12, 25)
print(myClass.year, myClass.month, myClass.day)  # (2016, 12, 25)

## スタティックメソッド

# インスタンス化しなくても呼べる「が、インスタンスからでも呼び出せる」メソッド

# インスタンス化せず呼び出し
print(TestClass.staticmethod(42, 1))  # 43

# インスタンス化してからも呼び出せる
myClass = TestClass(2014, 12, 14)
print(TestClass.staticmethod(42, 1))  # 43
"""

## パッケージ化

# この2行、なくても動くんだが。。。。。
# import sys
#sys.path.append("./submodule1")

# import submodule1.sub1
# submodule1.sub1.myHello()


## 変数の型チェック

"""
myTuple = ("tuple", "instance")

# 第二引数: tuple, list, dict, set, クラス名そのもの...
if isinstance(myTuple, tuple):
	print("tuple!!")
else:
	print("tigau...")
"""

## 呼び出し可能チェック

# 変数・オブジェクトが、()で適用可能かどうか。
# 要は、メソッド・ラムダ式・クラスか否かを判定し返す、ってだけ。

"""
import sys

def func_test():
	pass

myLambda = lambda x: x + 1

class MyClass:
	pass

str_test = "hello"

print(callable(sys),        # false
 	  callable(func_test),  # true
 	  callable(myLambda),   # true
 	  callable(MyClass),    # true
 	  callable(str_test)    # false
 	 )
"""


## 属性(Swiftでいうプロパティ)の有無チェック

"""
class AttrTest:

	def __init__(self):
		self.code = -1

myAttrTest = AttrTest()

# あとからプロパティを「注入」できる。フリーダムすぎるだろ...
myAttrTest.name = "Python!"

print(hasattr(myAttrTest, "code"))  # true
print(hasattr(myAttrTest, "name"))  # true. てかこんなの許されんのかよ...
print(hasattr(myAttrTest, "hoge"))  # false

# hasattr関数は、getattr関数を利用して実装されている。
# getattrを利用した場合、保持していない属性を取得しようとすると AttributeErrorを投げるが、
# 第３引数でデフォルト値が設定されている場合は、それが返る。

class GetAttrTest:

	def __init__(self):
		self.code = -1

myAttr      = GetAttrTest()
myAttr.name = "Perl6"

print(getattr(myAttr, "code")) # -1
print(getattr(myAttr, "name")) # Perl6
# print(getattr(myAttr, "kana")) # AttributeError
print(getattr(myAttr, "kana", "No Attr")) # No Attr
"""

# 話はずれるが、これ、結果が違う！
# クラス名を渡した場合は code, name がないが、
# インスタンスを渡した場合は、code, name がある！
# プロパティがインスタンスに注入されている、というイメージか。面白い。
# print(dir(AttrTest))
# print(dir(myAttrTest))


## メンバの取得


# 引数なし = 自分自身(とは?)
# __builtins__, __file__, __name__, __package__ などが返る
# print(dir())

# python = "python!!"
# 上記に加え、 'python' が追加されている。
# print(dir())

# 引数にモジュールを渡した場合は、そのモジュール内で定義されているメンバを取得
# import sys
# print(dir(sys))

# myStr = "hello"
# いわずもがな、文字列オブジェクトのメンバが返る。
# print(dir(myStr))


# reduce

"""
from functools import reduce

def twice(x, y): return x + y
print(reduce(twice, range(5)))
"""



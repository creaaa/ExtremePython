
# クラス作成

"""
class TestClass:
	
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
"""


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

		# 2系の書き方。古い。
		# Country.__init__(self, countryName)

		# 3系。やっぱ断然こっちでしょ。と思いきやこっちも相当キモかった
		super(City, self).__init__(countryName)

		self.cityName = cityName

	def hoge(self):

		# 2系。実はまだこっちも動く。
		Country.hoge(self)

		# 3系。これは相当キモいな。。
		# super(City, self).hoge()


classes = []
classes.append(City("Japan", "Tokyo"))
classes.append(City("USA", "Washington"))
		
for cl in classes:
	print("country: " + cl.name)
	print("city: "    + cl.cityName)

print(type(City))  # <class 'type'> メタクラスへの入り口か...??

classes[0].hoge()



















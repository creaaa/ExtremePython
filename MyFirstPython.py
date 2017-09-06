
# coding: utf-8

# """
# この中もコメントアウトになります
# 複数行
# コメント!
# コメント!
# """
# # コメントです！
# # print ("Hello world!")

# # 数値として変数をセット
# num1 = 1
# num2 = 2
# # 1+2
# result = num1+num2
# # 出力
# print(result)

# # 文字列として変数をセット
# string1 = 'a'
# string2 = 'b'
# # ab
# concat = string1 + string2
# # 出力
# print(concat)

# 文字連結

# print ("hello"+"world")
# print ("hello" * 3)

# 文字列埋め込み

name = "Endo"
score = 52.6

# %で文字列埋め込み(整数は%d)
print("name: %s,score:%f" %(name,score)) # name: Endo,score:52.600000

# # リスト
# mylist1 = ['10', '20', '30'] # ['10', '20', '30']
# mylist2 = [10, 20, 42]       # [10, 20, 42]
# mylist3 = ["hello", 42]      # 型の違う要素も格納できる

# print(mylist1[1]) # 20
# # print(mylist1[3]) # IndexError: list index out of range

# mylist3[0] = "hello, goodbye"
# print(mylist3[0]) # hello, goodbye

# # 定数
# # 存在しない...だと? んなアホな...

# # タプル

# myTuple = ("bye", 420) # ('bye', 42)
# print(myTuple[1]) # 420

# # myTuple[1] = 0 # TypeError: 'tuple' object does not support item assignment

# # リスト(=配列)は再代入可能、タプルは再代入不可！


###############

# 基本的なクラス定義 その1

# # Personクラスを定義
# class Person:
#     # ageプロパティに22をセット
#     age = 22
 
# # Personクラスのインスタンスを作成
# myPerson = Person()
 
# # Personクラスのインスタンスpsnからageプロパティを参照し画面に出力
# print(myPerson.age) # 22


# 基本的なクラス定義 その2

# Personクラスを定義　

class Person:
    # ageプロパティに22をセット
    age = 22
    # greetメソッドを定義
    def greet(self):
        print('こんにちは！ほげ！')
 
# Personクラスのインスタンスを作成
# psnはオブジェクト変数
psn = Person()
 
# Personクラスのインスタンスpsnからageプロパティを参照し画面に出力
print(psn.age) # 22
 
# Personクラスのインスタンスpsnからgreet()メソッドを呼び出す
psn.greet()

psn.age = 42
print(psn.age)

# クラスの中で関数（正確にはメソッド）を定義するとき、第１引数に必ずselfを指定しなければならない！と覚えておいて下さい。
# 引数が不要なメソッドを書く場合でも、必ず第１引数にselfを指定しなければなりません。そうしないと文法エラーになります。

# self = クラスのインスタンスを受け取る特別な引数 
# メソッドはクラスの自分自身のインスタンスを必ず第１引数にとる


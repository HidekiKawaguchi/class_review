# クラス(データ型)の定義
class Customer:
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name    # インスタンス変数
        self.family_name = family_name  # インスタンス変数
        self.age = age  # インスタンス変数

    def full_name(self):
        return f"{self.first_name} {self.family_name}"

    def entry_fee(self):
        if self.age >= 65:
            return "1200"
        elif self.age >= 20:
            return "1500"
        else:
            return "1000"

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


# 実体化(インスタンス化)
# C-1. フルネームを取得できる


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)


# C-1出力(フルネームを取得できる)
print(ken.full_name())  # "Ken Tanaka" という値を返す
print(tom.full_name())  # "Tom Ford" という値を返す


# C-2出力(年齢という概念の追加)
print(ken.age)  # 15 という値を返す
print(tom.age)  # 57 という値を返す
print(ieyasu.age)  # 73 という値を返す


# C-3出力 年齢に応じた適切な入場料(entry_fee)を計算できる
print(ken.entry_fee())  # 1000 という値を返す
print(tom.entry_fee())  # 1500 という値を返す
print(ieyasu.entry_fee())  # 1200 という値を返す


# C-4. 単一の顧客情報をCSV形式で取得できる
print(ken.info_csv())  # "Ken Tanaka,15,1000" という値を返す
print(ken.info_csv())  # "Tom Ford,57,1500" という値を返す
print(ieyasu.info_csv())  # "Ieyasu Tokugawa,73,1200" という値を返す

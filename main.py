def main():
    goods = [{"name": "コーヒー", "amount": 300, "num": 3}, {"name": "本", "aount": 500, "num": 5}, {"name": "クッキー", "aoount": 100, "num": 10}]

    print("|商品名|金額|商品数|")
    print("|----|----|----|")
    print_goods(goods)


def print_goods(goods):
    for good in goods:
        name = good["name"]
        amount = good["amount"]
        num = good["num"]
        
        print(f"|{name}|{amount}|{num}|")
        

def add_goods(goods, name, amount, num):
    good = {"name": name, "amount": amount, "num": num}
    goods.append(good)
    return goods


if __name__ == "__main__":
    main()
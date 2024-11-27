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
        

def calculate_total_price(stock):
    #商品の単価と数量を取得
    amount = stock["amount"]
    num = stock["num"]

    #合計金額を計算
    total_price = amount * num

    #辞書に合計金額を追加
    stock["total_price"] = total_price

    return stock

if __name__ == "__main__":
    main()
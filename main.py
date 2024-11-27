def main():
    goods = [{"name": "コーヒー", "num": 3}, {"name": "本", "num": 5}]

    print("|商品名|商品数|")
    print("|----|----|")
    print_goods(goods)


def print_goods(goods):
    for good in goods:
        name = good["name"]
        num = good["num"]
        print(f"|{name}|{num}|")


if __name__ == "__main__":
    main()
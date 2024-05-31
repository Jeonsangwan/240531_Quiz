class Order:
    def __init__(self):
        self.menu = {
            "coffee": ("coffee", 3000),
            "green_tea": ("green_tea", 2500),
            "iced_tea": ("iced_tea", 3000)
        }
        self.name = None
        self.price = 0
        self.total = 0

    def calculate_total(self):
        return self.total * self.price

    def process_order(self):
        user_input_1 = input("메뉴를 입력하세요 (coffee, green_tea, iced_tea): ")
        user_input_2 = int(input("수량을 입력하세요: "))

        if user_input_1 in self.menu:
            self.name, self.price = self.menu[user_input_1]
            self.total = user_input_2
            total_price = self.calculate_total()
            print(f"{self.name} {self.total}개를 주문하였습니다. 총 가격은 {total_price}원 입니다.")
        else:
            print("존재하지 않는 메뉴입니다. 다시 시도해주세요.")

order = Order()
order.process_order()

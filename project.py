class InventoryItem:
    def __init__(self, item_id, name, category, quantity, unit_price, storate_fee):
        self.item_id = item_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.unit_price = unit_price
        self.storate_fee = storate_fee
        self.total_inventory_value = 0
        self.inventory_type = ""

        self.calculate_inventory_value()
        self.classify_inventory()

    def calculate_inventory_value(self):
        self.total_inventory_value = (self.quantity * self.unit_price) + self.storate_fee

    def classify_inventory(self):
        if self.calculate_inventory_value < 5000000:
            self.inventory_type = "Thấp"
        elif 5000000 < self.calculate_inventory_value < 20000000:
            self.inventory_type = "Trung bình"
        elif 20000000 < self.calculate_inventory_value < 50000000:
            self.inventory_type = "Cao"
        else:
            self.inventory_type = "Rất cao"


class InventoryManager():
    def __init__(self):
        self.inventory = []


    def show_all(self):
        if not self.inventory:
            print("Danh sách hàng hóa đang rỗng !")
            return
        for item in self.inventory:
            print(f"{item[self.item_id]} | ",            
                f"{item[self.name]} | ",
                f"{item[self.category]} | ",
                f"{item[self.quantity]} | ",
                f"{item[self.unit_pric]} | ",
                f"{item[self.storate_fee]} | "
                f"{item[self.total_inventory_value]} | "
                f"{item[self.inventory_type]}"
                )
            
    def find_by_id(self, item_id):
        for item in self.inventory:
            if self.item == item_id:
                return item
        return None
    

    def add_item(self):
        try:
            item_id = input("Nhập mã hàng hóa: ")
            item_id = item_id.strip().upper()
            if not item_id:
                print("Mã hàng hóa không được để rỗng !")
                return
            if self.find_by_id(item_id):
                print("Mã hàng hóa đã tồn tại !")
                return
            name = input("Nhập tên hàng hóa: ")
            if not name:
                print("Tên hàng hóa không được để rỗng !")
                return
            category = input("Nhập danh mục sản phẩm: ")
            if not category:
                print("Danh mục hàng hóa không được rỗng !")
                return
            quantity = int(input("Nhập số lượng tồn: "))
            if not quantity:
                print("Số tồn không được để rỗng !")
                return
            if 0 >= quantity >= 100000:
                print("Số lượng không hợp lệ !")
                return
            if quantity < 0 :
                print("Số tồn phải lớn hơn 0 !")
                return
            unit_price = float(input("Nhập đơn giá: "))
            if not unit_price:
                print("Đơn giá không được rỗng !")
                return
            if unit_price < 0:
                print("Đơn giá phải lớn hơn hoặc bằng 0 !")
                return
            storate_fee = float(input("Nhập chi phí lưu kho: "))
            if not storate_fee:
                print("Chi phí lưu kho không được để trống !")
                return
            if storate_fee < 0:
                print("Chi phí lưu kho phải lớn hơn hoặc bằng 0 !")
                return
            new_item = (item_id,name,category,unit_price,quantity,storate_fee)
            self.inventory.append(new_item)
            print("Đã thêm hàng hóa thành công !")

        except ValueError:
            print("Dữ liệu nhận vào không hợp lệ !")
        
    # def update_item(self):
    #     found = False
    #     update_item = input("Nhập mã đơn cần cập nhật: ")
    #     update_item = update_item.strip().upper()
    #     if self.find_by_id:
    #         try:
    #             quantity = int(input("Nhập số lượng tồn: "))
    #             if not quantity:
    #                 print("Số tồn không được để rỗng !")
    #                 return
    #             if 0 >= quantity >= 100000:
    #                 print("Số lượng không hợp lệ !")
    #                 return
    #             if quantity < 0 :
    #                 print("Số tồn phải lớn hơn 0 !")
    #                 return
    #             unit_price = float(input("Nhập đơn giá: "))
    #             if not unit_price:
    #                 print("Đơn giá không được rỗng !")
    #                 return
    #             if unit_price < 0:
    #                 print("Đơn giá phải lớn hơn hoặc bằng 0 !")
    #                 return
    #             storate_fee = float(input("Nhập chi phí lưu kho: "))
    #             if not storate_fee:
    #                 print("Chi phí lưu kho không được để trống !")
    #                 return
    #             if storate_fee < 0:
    #                 print("Chi phí lưu kho phải lớn hơn hoặc bằng 0 !")
    #                 return
    #         except ValueError:
    #             print("Dữ liệu nhận vào không hợp lệ !")
            
        #     self.quantity = quantity
        #     self.unit_price = unit_price
        #     self.storate_fee = storate_fee
        #     self.total
        #     found = True
        # if not found:
        #     print("Không tìm thấy mã hàng hóa !")


def menu():
    print("""
=========== MENU ===========
1. Hiển thị danh sách hàng hóa
2. Thêm hàng hóa mới
3. Cập nhật hàng hóa
4. Xóa hàng hóa
5. Tìm kiếm hàng hóa
6.Thoát 
============================
""")
    

def main():
    manager = InventoryManager()
    while True:
        menu()
        choice = input("Nhập chức năng:  ")
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_item()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống kho hàng !")
                break
            case _:
                print("Lựa chọn không hợp lệ !")



main()
product_list = [{
    "id" : "SP001",
    "name" : "Chuot khong day",
    "price" : 250000,
    "cout" : 15,
    "safety_stock" : 20,
    "cout_price" : 3750000,
    "status" : "Cảnh báo"
}]

def test_int(number):
    if number.isdigit():
        number = int(number)
        if number >= 0:
            return number
        else:
            print("khong hop le")
            return
    else:
        print("khong hop le") 
        return   
    
def status_product(cout, safety_stock):
    if cout == 0:
        return "Hết hàng"
    elif cout < safety_stock:
        return "Cảnh báo"
    elif cout < 3 * safety_stock:
        return "An toàn"
    elif cout > 3 * safety_stock:
        return "Quá tải"
     
def show_product(product):
    if not product:
        print("không có nhân viên nào trong danh sách")
    else:
        print("--- Danh sách sản phẩm ---")
        print(f"{'ID':<5} | {'name_product':<17} | {'price':<8} | {'cout':<5} | {'safety_stock':<12} | {'cout_price':<12} | {'status':<10}")
        for pro in product:
            print(f"{pro["id"]:<5} | {pro["name"]:<17} | {pro["price"]:<8} | {pro["cout"]:<5} | {pro["safety_stock"]:<12} | {pro["cout_price"]:<12} | {pro["status"]:<10}")

def new_products(product):
    id = input("nhập mã sản phẩm: ").strip().upper()
    if not id:
        print("id không hợp lệ")
        return
    for pro in product:
        if id == pro["id"]:
            print("id kh được trùng")
            return
    name = input("nhap ten san pham: ").strip().lower().title()
    if not name:
        print("ten khong duoc de trong")
        return
    price = input("nhap don gia san pham: ").strip()
    price = test_int(price)
    cout = input("nhap so luong ton kho: ").strip()
    cout = test_int(cout)
    safety_stock = input("nhap dinh muc ton kho toi thieu: ").strip()
    safety_stock = test_int(safety_stock)
    cout_price = cout * price
    status = status_product(cout,safety_stock)
    new_product = {
        "id" : id,
        "name" : name,
        "price" : price,
        "cout" : cout,
        "safety_stock" : safety_stock,
        "cout_price" : cout_price,
        "status" : status
    }
    product.append(new_product)
    print("thêm sản phẩm thành công")

def update_product(product):
    check_id = input("nhập id cần chỉnh sửa: ").strip().upper()
    if not check_id:
        print("id kh để trống")
        return
    for pro in product:
        if check_id == pro["id"]:
            new_price = input("nnhập đơn giá mới: ").strip()
            new_price = test_int(new_price)
            pro["price"] = new_price
            new_cout = input("nhập số lượng kho mới: ").strip()
            new_cout = test_int(new_cout)
            pro["cout"] = new_cout
            new_safety_stock = input("nhập định mức tồn kho tối thiểu mới: ").strip()
            new_safety_stock = test_int(new_safety_stock)
            pro["safety_stock"] = new_safety_stock
            new_cout_price = new_price * new_cout
            pro["cout_price"] = new_cout_price
            pro["status"] = status_product(new_cout,new_safety_stock)

def delete_product(product):
    check_id = input("nhập id cần xóa: ").strip().upper()
    if not check_id:
        print("id kh để trống")
        return
    for pro in product:
        if check_id == pro["id"]:
            check = input("bạn có chắc muốn xóa sản phẩm khỏi danh mục này(Y/N): ").strip().upper()
            if check == "Y":
                print(f"bạn đã xóa sản phâm có id {pro["id"]}")
                product.remove(pro)
            
def seach_product(product):
    check = input("bạn muốn tìm kiếm theo mã hay tên(id/name): ").strip().lower()
    if check == "id":
        check_id = input("nhâp id cần tìm kiếm: ").strip().upper()
        if not check_id:
            print("id kh để trống")
            return
        for pro in product:
            if check_id == pro["id"]:
                print(f"{pro["id"]:<5} | {pro["name"]:<17} | {pro["price"]:<8} | {pro["cout"]:<5} | {pro["safety_stock"]:<12} | {pro["cout_price"]:<12} | {pro["status"]:<10}")
    if check == "name":
        check_name = input("nhập tên cần tìm kiếm: ").strip().lower().capitalize()
        for pro in product:
            if check_name == pro["name"]:
                print(f"{pro["id"]:<5} | {pro["name"]:<17} | {pro["price"]:<8} | {pro["cout"]:<5} | {pro["safety_stock"]:<12} | {pro["cout_price"]:<12} | {pro["status"]:<10}")

def check_status(product):
    het_hang = 0
    canh_bao = 0
    an_toan = 0
    qua_tai = 0
    for pro in product:
        if pro["status"] == "Hết hàng":
            het_hang += 1
        if pro["status"] == "Cảnh báo":
            canh_bao += 1
        if pro["status"] == "An toàn":
            an_toan += 1
        if pro["status"] == "Quá tải":
            qua_tai += 1
    print(f"""
--- Thống kê trạng thái kho hàng --
Số lượng sản phẩm hết hàng: {het_hang}
Số lượng sản phẩm cảnh báo: {canh_bao}
Số lượng sản phẩm an toàn: {an_toan}
Số lượng sản phẩm quá tải: {qua_tai}
""")
while True:
    print("""
        --- Quản lý sản phẩm ---
          1. Hiển thị danh sách kho hàng
          2. Khai báo sản phẩm mới
          3. Cập nhật số lượng và giá vốn
          4. xóa sản phẩm khỏi danh mục
          5. tìm kiếm sản phẩm
          6. thống kê trạng thái kho hàng
          7. thoát chương trình
""")
    choice = input("Mời bạn chọn chức năng(1-7): ")
    if choice == "1":
        show_product(product_list)
    elif choice == "2":
        new_products(product_list)
    elif choice == "3":
        update_product(product_list)
    elif choice == "4":
        delete_product(product_list)
    elif choice == "5":
        seach_product(product_list)
    elif choice == "6":
        check_status(product_list)
    elif choice == "7":
        print("bạn đã thoát chương trình")
    else:
        print("Lựa chọn không hợp lệ")
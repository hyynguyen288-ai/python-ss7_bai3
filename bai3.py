raw_data = "emp-001|nguyen van a|it|0912-345-678;emp-002|tran thi b|hr|0987-654-321;emp-003|le van c|finance|09ab-123-456"
while True:
    print("\n1. Du lieu goc")
    print("2. Bao cao")
    print("3. Tim nhan vien")
    print("4. Thoat")
    choose = input("Nhap: ")
    if choose == "1":
        print(raw_data)
    elif choose == "2":
        data = raw_data.split(";")
        print("ID        NAME                DEPARTMENT     PHONE")
        for i in data:
            p = i.split("|")
            emp_id = p[0].strip().upper()
            name = p[1].strip().title()
            dep = p[2].strip().upper()
            phone = p[3].replace("-", "").strip()
            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"
            print(emp_id, name, dep, phone)
    elif choose == "3":
        find = input("Nhap ID: ").strip().upper()
        data = raw_data.split(";")
        check = False
        for i in data:
            p = i.split("|")
            emp_id = p[0].strip().upper()
            if emp_id == find:
                name = p[1].strip().title()
                dep = p[2].strip().upper()
                phone = p[3].replace("-", "").strip()
                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"
                print("\nTim thay")
                print(emp_id)
                print(name)
                print(dep)
                print(phone)
                check = True
        if check == False:
            print("Khong tim thay nhan vien")
    elif choose == "4":
        print("Thoat")
        break
    else:
        print("Nhap sai")
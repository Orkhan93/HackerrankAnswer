def print_full_name(a, b):
   print(f"Hello {a} {b}! You just delved into python.")


name = input("Ad daxil edin : ")
surname = input("Soyad daxil edin : ")
if len(name)>=10 or len(surname)>=10:
    print("yeniden daxil edin : ")
else:
    print(f"Hello {name} {surname} ! You just delved into python.")



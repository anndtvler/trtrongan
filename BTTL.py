# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""
# Bài 1 

def chuyenDoiSoN( n, b):
    if (n < 0 or b < 2 or b > 16):
        print ("Nhập số n hoặc b không hợp lệ...");
        return;
 
    sb = "";
    m = 0;
    remainder = n;
 
    while (remainder > 0):
        if (b > 10):
            m = remainder % b;
            if (m >= 10):
                sb = sb + str(chr(55 + m));
            else:
                sb = sb + str(m);
        else:
            sb = sb + str(remainder % b);
        remainder = int(remainder / b);
    return "".join(reversed(sb)); # đảo ngược chuỗi sb
    
n = int (input("Nhập n: "));
b = int (input ("Nhập cơ số b: "));
print ("Số" ,n, "sau khi được chuyển đổi sang hệ cơ số ",b,":"  ,chuyenDoiSoN(n,b));
"""

"""
#Bài 2 

def lietKeCacSoChiaHetCho7 ():
    a = [];
    for x in range (10,201):
        if (x % 7 == 0 and x % 5 != 0):
            a.append(x);
    print ("Dãy số thỏa yêu cầu: " ,a);
lietKeCacSoChiaHetCho7();
"""

"""
#Bài 3 ax2 + bx + c = 0.
def giaiPTBac2(a,b,c):
    # kiểm tra các hệ số
    if (a == 0):
        if (b == 0):
            print ("Phương trình vô nghiệm!");
        else:
            print ("Phương trình có một nghiệm: x = ", + (-c / b));
        return;
 
    # tính delta
    delta = b * b - 4 * a * c;
    # tính nghiệm
    if (delta > 0):
        x1 = (float)((-b + math.sqrt(delta)) / (2 * a));
        x2 = (float)((-b - math.sqrt(delta)) / (2 * a));
        print ("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2);
    elif (delta == 0):
        x1 = (-b / (2 * a));
        print("Phương trình có nghiệm kép: x1 = x2 = ", x1);
    else:
        print("Phương trình vô nghiệm!");
    
a = float(input("Nhập hệ số a: "));
b = float(input("Nhập hệ số b: "));
c = float(input("Nhập hệ số c: "));
giaiPTBac2(a,b,c);
"""

"""
#Bài 4
def UCLN(a, b):
    if (b == 0):
        return a;
    return UCLN(b, a % b);
    
def BCNN (a,b):
    return int((a * b) / UCLN(a, b));
a = int (input("Nhập số nguyên dương a: "));
b = int(input("Nhập số nguyên dương b = "));
print("UCLN của",a, UCLN(a,b));
print("BCNN của",a, BCNN(a,b));
"""

"""
#Bài 5
def KTSNT (a):
    flag = 1;
    if (a <2):
        flag = 0;
        return flag  ;
    for p in range(2, a):
        if (a % p) == 0:
            flag = 0;
            return flag;
    return flag;

def lietKeSNTNhoHonN(n):
    list1 = [];
    for x in range(2,n):
        kt = KTSNT(x);
        if (kt == 1):
            list1.append(x); 
    return list1;
    
n = int(input("Nhập n: "));
print ("Dãy SNT nhỏ hơn",n,":", lietKeSNTNhoHonN(n));
"""

#Bài 6
def tinhTongCacChuSo(n):
    total = 0;
    while (n > 0):
        total = total + n % 10;
        n = int(n / 10);
    return total;
    
n = int(input("Nhập n: "));
print("Tổng các chữ số của", n , "là", tinhTongCacChuSo(n));






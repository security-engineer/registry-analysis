import winreg

def rot13(s):
    return s.translate(str.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"))

def get_userassist_data():
    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\UserAssist\{CEBFF5CD-ACE2-4F4F-9178-9926F41749EA}\Count"
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, reg_path) as key:
        for i in range(winreg.QueryInfoKey(key)[1]):
            name, value, _ = winreg.EnumValue(key, i)
            decoded_name = rot13(name)
            print(f"Program: {decoded_name}, Data: {value}")

get_userassist_data()
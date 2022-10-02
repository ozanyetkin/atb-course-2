# verilen bir string icerisinde baska bir stringin kac kez gectigini bulacagiz
# "lifeforlife", "life" => 2
# "lifeforlifeforlife", "lifeforlife" => 2
# "lifesforlifesforlife", "lifesforlife" => 2
# "lifeforlifeforlifea", "lifeforlife" => 2
# "lifeforlifeforlife", "eforlife" => 2

def substring_finder(str1, str2):
    i = 0
    count = 0
    while i <= (len(str1) - len(str2)):
        if str1[i:len(str2) + i] == str2:
            count += 1
        i += 1
    return count

def substring_finder(str1, str2):
    count = 0
    for i in range(len(str1) - len(str2) + 1):
        if str1[i:len(str2) + i] == str2:
            count += 1
    return count

print(substring_finder("lifeforlife", "life"))
print(substring_finder("lifeforlifeforlife", "lifeforlife"))
print(substring_finder("lifesforlifesforlife", "lifesforlife"))
print(substring_finder("lifeforlifeforlife", "eforlife"))

print(substring_finder("lifeforlifeforlifeforlife", "lifeforlife"))
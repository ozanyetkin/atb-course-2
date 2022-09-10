# Kenar uzunlugunu tanimladik
edge = float(input("Lutfen kenar uzunlugunu giriniz: "))

# Hacim formulunu yazdik
# https://www.google.com/search?q=dodecahedron&sxsrf=ALiCzsZjgOVosMCVFJh1WI2qytveCH1_cA%3A1660992311796&ei=N7sAY_6dMIuBxc8PoZWO4Aw&ved=0ahUKEwi-leDFntX5AhWLQPEDHaGKA8wQ4dUDCA4&uact=5&oq=dodecahedron&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCMQsAMQJzIHCCMQsAMQJzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQsAMQQzIHCAAQsAMQQzIHCAAQsAMQQzIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIKCAAQ5AIQsAMYATIVCC4QxwEQ0QMQ1AIQyAMQsAMQQxgCMg8ILhDUAhDIAxCwAxBDGAJKBAhBGABKBAhGGAFQAFgAYNkEaAFwAXgAgAEAiAEAkgEAmAEAyAERwAEB2gEGCAEQARgJ2gEGCAIQARgI&sclient=gws-wiz-serp
volume = (15 + 7 * 5 ** 0.5)/ 4 * edge ** 3

# Hesapladigimiz hacmi terminale yazdirdik
print(volume)
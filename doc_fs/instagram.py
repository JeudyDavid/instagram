import instaloader

def vole(non_profil):
    non_profil =input("antre non profil instagram nan:")
    print ("ok...")
    instaloader.Instaloader().download_profile(non_profil,profile_pic_only=False)
    print ("li telechaje! ")
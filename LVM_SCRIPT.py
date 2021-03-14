import os
import getpass

print("Just Press and get things done!!".center(100))
print("---------------------------------------".center(100))


passwd = getpass.getpass("Enter your password:")
if passwd!="1234":
    print("password incorrect")
    exit()

while True:
    os.system("clear")
    print("""
    Press 1 : To check how many storage is attached to the OS
    Press 2 : To create Physical Volume
    Press 3 : To display Physical Volume
    Press 4 : To create Volume Group
    Press 5 : To display Volume Group
    Press 6 : To create Logical Volume
    Press 7 : To display Logical Volume
    Press 8 : To format the LV
    Press 9 : To Exit
    """)

    ch = input("Enter your Choice:")
    print(ch)

    if int(ch)==1:
        os.system("fdisk -l")

    elif int(ch)==2:
        pv1=input("Enter the name of storage 1:")
        pv2=input("Enter the name of storage 2:")
        os.system("pvcreate {}".format(pv1))
        os.system("pvcreate {}".format(pv2))

    elif int(ch)==3:
        pv=input("Enter the name of storage:")
        os.system("pvdisplay {}".format(pv))
        
    elif int(ch)==4:
        Volume_Group_Name=input("Give name to the VG:")
        pv_Name1=input("Enter the name of storage 1:")
        pv_Name2=input("Enter the name of Storage 2:")
        os.system("vgcreate {} {} {}".format(Volume_Group_Name,pv_Name1,pv_Name2))

    elif int(ch)==5:
        Volume_Group_Name1=input("Enter the name of VG:")
        os.sytem("vgdisplay {}".format(Volume_Group_Name1))

    elif int(ch)==6:
        size=input("Enter size for your LV:")
        LV_Name=input("Give name to your LV:")
        Volume_Group_Name2=input("Enter name of the VG:")
        os.system("lvcreate --size{} --name{} {}".format(size,LV_Name,Volume_Group_Name2))
                         
    elif int(ch)==7:
        os.system("lvdisplay")

    elif int(ch)==8:
        Volume_Group_Name4=input("Enter the name of VG:")
        LV_Name2=input("Enter the name of LV:")
        os.system("mkfs.ext4  /dev{}{}".format(Volume_Group_Name4,LV_Name2))

    elif int(ch)==9:
        exit()

    else:
        print("Not Supported")

    input("\nPlease enter to continue...")

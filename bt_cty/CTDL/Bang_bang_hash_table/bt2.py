def main():
    bang_bam = dict()
    import random 
    for _ in range(10):
        khoa = random.randint(0,10)
        gia_tri = random.randint(0,100)
        print(f"** Them khoa = {khoa}, gia tri = {gia_tri}")
        bang_bam[khoa]=gia_tri
        print(bang_bam)
        print()
    
    khoa = int(input("Nhap vao mot khoa: "))
    gia_tri = bang_bam[khoa]
    print(f"Khoa {khoa} co gia tri la {gia_tri}")
    
if __name__ == "__main__":
    main()
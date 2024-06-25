import os



def main():
    source = "./output"
    folders = list(filter(lambda x: os.path.isdir(x), map(lambda x: os.path.join(source, x), os.listdir(source))))
    for folder in folders:
        print(folder)
        files = os.listdir(folder)
        for file in files:
            if file.endswith(".xlsx"):
                print(os.path.join(folder, file))
                print(folder + ".xlsx")
                os.rename(os.path.join(folder, file), folder + ".xlsx")
                


if __name__=="__main__":
    main()
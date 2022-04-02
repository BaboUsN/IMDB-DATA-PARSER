import Parser
import GetData


def main():
    print("1- Enter Your Custom Url")
    print("2- Enter Your Number to Current url")
    ans = input("What is your choice : ")
    try:
        if(ans in "1"):
            ans2 = input("Enter Your Custom Url : ")
            GetData.getDataWithNewUrl(ans2)
            Parser.start()
        elif(ans in "2"):
            ans2 = input("Enter Your Number to Current Url : ")
            GetData.getDataWithCurrentUrl(ans2)
            Parser.start()
        else:
            print("Invalid Value")
    except:
        print("Something's gone wrong")


while True:
    main()

import re
def regularExpressionex():

    #validate user email address without re
    # username, domain=input("email:").split("@")
    # # print(email)
    # if "@" in email and "." in email :
    #     print("yes")
    # print(username+' '+domain)
    # if username and domain.endswith(".com"):
    #     print("valid")
    # else:
    #     print("Invalid")



    #using regular expression libraray re
    email= input("email:")
    if re.search(r"^\w+@(\w+\.)*\w+\.com$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("invalid")



    #libraries that are commanly used
    email = input("email:")
    if re.search(r"^\w+@(\w+\.)*\w+\.com$", email, re.IGNORECASE):
        print("Valid")
    else:
        print("invalid")


    return


def reformatdata():

    name=input("name:").strip()
    # if "," in name:
    #     last, first=name.split(",")
    #     name= f"{first} {last}"
    #
    # print(name)

    if matches:= re.search(r"^(.+), *(.+)$",name):

        name=f"{matches.group(1)} {matches.group(2)}"
        print(matches.group(1)+" &  "+ matches.group(2))

    return

def extractinformation():

    url=input("URL:").strip()
    # print(url)
    # username=url.replace("https://twitter.com/","")
    # username=url.removeprefix("https://twitter.com/")
    # username=re.sub("^(https?://)?(www\.)?twitter\.com/","",url)
    # if username:= re.search(r"^https?://(www\.)?twitter\.com/(.+)$",url):
    #     print(username.group(1))
    if username:= re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_-]+)$",url):
        print(username.group(1))
    # print(username)
    return

import requests
import re
import sys

# def download(url, path, format):
#     #connect to a URL

#     website = requests.get(url)

#     #read html code
#     # print(website.text)

#     # #use re.findall to get all the links
#     links = re.findall('"((http|ftp)s?://.*?)"', website.text)

#     for link in links:

#         if format in link[0]:
#             name = link[0].split("/")[-1]
#             with open(path+name, 'wb') as fd:
#                 fd.write(requests.get(link[0]).content)
#
def main():
    #connect to a URL

    website = requests.get(sys.argv[1])

    #read html code
    # print(website.text)

    # #use re.findall to get all the links
    links = re.findall('"((http|ftp)s?://.*?)"', website.text)

    for link in links:

        if sys.argv[3] in link[0]:
            name = link[0].split("/")[-1]
            with open(sys.argv[2]+name, 'wb') as fd:
                fd.write(requests.get(link[0]).content)


# if __name__ == "__main__":
#     url = "http://www.cs.cmu.edu/~mgormley/courses/10701-f16/previous.html"
#     path = "D:\\GoogleUofT\\4-2\\411\\otherSchoolFinal&Solution\\"
#     download(url, path, "pdf")
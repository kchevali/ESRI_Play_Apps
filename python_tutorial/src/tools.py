"""
README
Requires python3 with arcgis installed.
Self note: use ~/opt/miniconda3/bin/python to run project files.
"""


def getCredentials(useRootPath):
    loginFilePath = 'assets/login.txt' if useRootPath else '../assets/login.txt'
    try:
        with open(loginFilePath) as file:
            username, password = tuple(file.read().split('\n'))
    except:
        username = input("Please enter your username:")
        password = input("Please enter your password:")
        with open(loginFilePath, "w") as file:
            file.write(username + '\n' + password)
            print("Saved credentials successfully")
    # print("username:'"+username+"'")
    # print("password:'"+password+"'")
    return username, password


def arcgisLogin(useRootPath=False):
    username, password = getCredentials(useRootPath=useRootPath)
    from arcgis.gis import GIS

    gis = GIS("https://www.arcgis.com", username=username, password=password)
    print("Login successful!!")
    return gis


if __name__ == '__main__':
    gis = arcgisLogin(useRootPath=True)

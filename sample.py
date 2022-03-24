import ip2proxy_python_c
import ip2location_python_c

path_ip2location = "C:\\Users\\bette\\Desktop\\knitify\\projects\\ip2info\\forks\\IP2Location-C-Library\\IP2Location.dll"
path_ip2proxy = "C:\\Users\\bette\\Desktop\\knitify\\projects\\ip2info\\forks\\ip2proxy-c\\IP2Proxy.dll"
db_ip2proxy = ip2proxy_python_c.IP2Proxy(libraryname=path_ip2proxy)
db_ip2location = ip2location_python_c.IP2Location(libraryname=path_ip2location)

db_ip2location.open("C:\\Users\\bette\\ipdata\\IP2LOCATION-LITE-DB11.IPV6.BIN")
db_ip2proxy.open("C:\\Users\\bette\\ipdata\\IP2PROXY-LITE-PX4.BIN")

print ('IP2Proxy Module Version: ' + db_ip2proxy.get_module_version())
print ('IP2Proxy Package Version: ' + db_ip2proxy.get_package_version())
print ('IP2Proxy Database Version: ' + db_ip2proxy.get_database_version())

# print ('IP2Location Module Version: ' + db_ip2location.get_module_version())
# print ('IP2Location Package Version: ' + db_ip2location.get_package_version())
# print ('IP2Location Database Version: ' + db_ip2location.get_database_version())

record_ip2proxy = db_ip2proxy.get_all("1.0.4.1")
record_ip2location = db_ip2location.get_all("94.252.122.6")

print(record_ip2proxy)
print(record_ip2location)
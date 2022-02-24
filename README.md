# Requisites

1. Microsoft visual studio, with the python extension and build tools option
2. Clone these projects to compile the libraries
https://github.com/ip2location/ip2proxy-c
https://github.com/chrislim2888/IP2Location-C-Library
3. The standalone .py files from each of the next two projects are included in this repository, together with the sample.py
https://github.com/ip2location/ip2proxy-python-c
https://github.com/ip2location/ip2location-python-c


# Clone & ompile the C libraries

## In windows (compile DLLs)

Add this to all the function headers in the .h files of both projects (in the public functions)
`__declspec(dllexport) `

Then replace the contents of the Makefile.win of both projects, with these:

```
TARGET_DLL = libIP2Proxy/IP2Proxy.dll
 
.SUFFIXES: .obj .c .dll .lib

all: $(TARGET_DLL)

$(TARGET_DLL):
	cl /nologo /DWIN32 /DWIN64 /I libIP2Proxy /LD /Tp libIP2Proxy/IP2Proxy.c Ws2_32.lib
```

```
TARGET_DLL = libIP2Proxy/IP2Location.dll
				 
.SUFFIXES: .obj .c .dll .lib

all: $(TARGET_DLL)

$(TARGET_DLL):
	cl /nologo /DWIN32 /DWIN64 /I libIP2Location /LD /Tp libIP2Location/IP2Location.c Ws2_32.lib
```

Open a terminal, run on it this
"C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"

Within the same terminal do the next

cd C:\Users\bette\Desktop\knitify\projects\extern\ip2proxy-c
nmake /A /f Makefile.win

cd C:\Users\bette\Desktop\knitify\projects\extern\IP2Location-python-c
nmake /A /f Makefile.win

## Python 3.9 compatibility

In the standard CDLL module, line 364, add to the condition "name and" ("if name and (...)") after the "import nt", or it will not work.
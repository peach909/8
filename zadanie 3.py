Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
1. def getInput(): return(input('запрашиваю ввод: '))
2. def testInput(n):
        try: n = int(n); return(True)
        except: return(False)
3. def strToInt(n): return(int(n))
4. def printInt(n): print(n)
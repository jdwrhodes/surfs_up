#%%
def addTwoNumbers(number1, number2):
    return number1 + number2
# %%
addTwoNumbers(3,4)
# %%
type(addTwoNumbers)
# %%
someotherfunction = addTwoNumbers
# %%
type(someotherfunction)
# %%
def functionInsideFunctions():
    print("hello")

    def inner1():
        print("bacon")
    def inner2():
        print("eggs")
    inner1()
    inner2()
# %%
functionInsideFunctions()
# %%
import time
# %%
def printTimeNow():
    timeNowObject = time.localtime()
    currentTime = time.strftime("%H:%M:%S", timeNowObject)
    print(currentTime)
# %%
printTimeNow()
# %%
def wrappingFunction(someFunctionLocation):
    print("Before Function")
    someFunctionLocation()
    print("After Function")
# %%
wrappingFunction(printTimeNow)
# %%
@wrappingFunction
def goodbyefunction():
    print('Goodbye')
# %%
goodbyefunction()
# %%

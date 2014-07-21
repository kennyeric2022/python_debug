import sys, traceback
traceOutput = sys.stdout
watchOutput = sys.stdout
rawOutput = sys.stdout

watch_format = ('File "%(fileName)s", line %(lineNumber)d, in'
                ' %(methodName)s\n %(varName)s <%(varType)s>'
                ' = %(value)s\n\n')
def watch(variableName):                
    if __debug__:
        stack = traceback.extract_stack()[-2:][0]
        actualCall = stack[3]
        if actualCall is None:
            actualCall = "watch([unknown])"
        left = actualCall.find('(')
        right = actualCall.rfind(')')
        paramDict = dict(varName = actualCall[left+1:right].strip(),
                         varType = str(type(variableName))[7:-2],
                         value = repr(variableName),
                         methodName = stack[2],
                         lineNumber = stack[1],
                         fileName = stack[0])
        watchOutput.write(watch_format % paramDict)                       

trace_format = ('File "%(fileName)s", line %(lineNumber)d, in'
                ' %(methodName)s\n  %(text)s\n\n')

def trace(text):
    if __debug__:
        stack = traceback.extract_stack()[-2:][0]
        paramDict = dict(text = text,
                         methodName = stack[2],
                         lineNumber = stack[1],
                         fileName = stack[0])
        traceOutput.write(trace_format % paramDict) 

def raw(text):        
    if __debug__:
        rawOutput.write(text)

def __testTrace():
    secretOfUniverse = 42
    watch(secretOfUniverse)

if __name__ == "__main__":
    a = "something else"
    watch(a)
    __testTrace()
    trace("This line was executed!")
    raw("Just some raw text...")

from tkinter import *

root = Tk()
root.geometry("800x800")
root.title("Code difference finder")

res = ""

def lcs(X, Y):
    m = len(X)
    n = len(Y)

    L = [[None] * (n + 1) for i in range(m + 1)]
    for i in range(m + 1):
        global res
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                #res+=X[i - 1]
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    l=m
    k=n
    lcsFin = ""
    while l>0 and k>0:
        if X[l-1]==Y[k-1]:
            lcsFin+=X[l-1]
            l-=1
            k-=1
        elif L[l-1][k]>L[l][k-1]:
            l-=1
        else:
            k-=1
    res=lcsFin

    return L[m][n]


def setAns(code1,code3):
    code3.delete("1.0","end-1c")
    in1=code1.get("1.0","end-1c")
    ind=0
    for i in in1:
        if(ind<len(res)):
            c = (res.__getitem__(ind))
        if i == c and ind<len(res):
            #print(END)
            ind+=1
            code3.insert(END,i)
        else:
            gg=code3.index("end-1c")
            print(gg)
            code3.insert(END,i)
            code3.tag_add("makeRed",gg)
            code3.tag_configure("makeRed",background="yellow",foreground='red')
            #code3.tag_remove("makeRed",gg)
        #ind+=1


def getDiff(code1,code2):
    in1=code1.get("1.0","end-1c")
    in2=code2.get("1.0","end-1c")
    #l3.configure(text=in1+in2)

    #res=res+in1+in2
    global res
    print(lcs(in1,in2))
    res="".join(reversed(res))
    print(res)
    global code3
    setAns(code1,code3)
    l3.configure(text="Deifferences between Code 1 and Code 2 have been HIGLIGHTED")
    #code1.highlight_pattern(res,res)
    #l3.configure(text=res)

l = Label(text="Code 1:")
code1 = Text(root,bg='light yellow',height=10)

l2 = Label(text="Code 2:")
code2 = Text(root,bg='light yellow',height=10)

btn = Button(root, height=2, width=10, text="Submit", command=lambda: getDiff(code1,code2))

l3 = Label()

code3 = Text(root,bg='light green',height=18)
code3.insert("end-1c","Result")

l.pack()
code1.pack()
l2.pack()
code2.pack()
btn.pack()
l3.pack()
code3.pack()

root.mainloop()
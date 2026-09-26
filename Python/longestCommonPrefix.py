strs = ["flower", "flow", "flight"]
pre = strs[0]

for i in range(1,len(strs),1):
    while not strs[i].startswith(pre):
        pre = pre[:-1]

print(pre)
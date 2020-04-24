#寫程式碼來讀取留言檔案

data = []
with open ('original.txt','r') as f :
	for line in f :
		data.append(line)
print(data)
from win32com.client import Dispatch
import win32com.client
import os

homedir = os.getcwd()
excel = win32com.client.Dispatch('Excel.Application')
"""
0代表隐藏对象，但可以通过菜单再显示
-1代表显示对象
2代表隐藏对象，但不可以通过菜单显示，只能通过VBA修改为显示状态
"""
excel.Visible = -1
myBooklst=list([
"AVSC1 limit-lossyG,lossyA,intra",
"AVSC2 losslG,lossyA,intra",
"AVSC3 losslG,limit-lossyA,intra",
"AVSC4 losslG,losslA,intra",
])

ori_lst =  list([
[5,38],
[5,36],
[5,40],
[5,33],
])

tar_lst =  list([
[5,15],
[5,15],
[5,15],
[5,15],
])

height_lst =  list([
132,
132,
110,
22,
])

wide_lst =  list([
13,
11,
15,
7,
])
# temp=tar_lst
# tar_lst=ori_lst
# ori_lst=temp
myBook = excel.Workbooks.Open(homedir + "\\pcem.xlsm")
for num in range(4):
	bookname=myBooklst[num]
	mySheet = myBook.Worksheets(bookname)
	height=height_lst[num]
	wide=wide_lst[num]
	heibegin_ori=ori_lst[num][0]
	widebegin_ori=ori_lst[num][1]
	heibegin_tar=tar_lst[num][0]
	widebegin_tar=tar_lst[num][1]
	for j in range(height):
		for i in range(wide):
			a=mySheet.Cells(heibegin_ori+j, widebegin_ori+i).Value
			if i==0 and a==None:
				break
			mySheet.Cells(heibegin_tar+j, widebegin_tar+i).Value = a
myBook.save
myBook.close
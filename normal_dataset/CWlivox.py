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


myBook = excel.Workbooks.Open(homedir + "\\pcem.xlsm")

mySheet = myBook.Worksheets("AVSC4 losslG,losslA,intra")

logpath = homedir + '\\log\\'

cond = 'C4-losslessG-losslessA-ai'
name1 = cond + '_'
CW_lst =  list([
'Livox_01_all_1mm',
'Livox_02_all_1mm'
])

pc=21

for name2 in CW_lst:
	points = 0
	total = 0
	positions = 0
	attributes = 0
	time = 0
	time2 = 0

	codname = (name1 +'r1_'+ name2)
	enclog = (logpath + codname  + '_enc.log')
	declog = (logpath + codname  + '_dec.log')
	reader = open( enclog, 'r')

	for line in reader:
		words = line.split()
		if (('points:' in words) and ('output' in words) and ('frames' in words)) :
			points= int(words[-1])
		if (('points' in words) and ('(averaged):' in words)) :
			points+= int(words[5])
		if (('Geometry' in words) and ('bits:' in words)):
			positions+=int(words[2])
		if (('Attributes' in words) and ('bits:' in words)):
			attributes+=int(words[2])
		if (('Total' in words) and ('bitstream' in words)):
			total+=int(words[3])
		if (('Total' in words) and ('(user):' in words)):
			time+=float(words[4])
	reader.close()
	reader = open(declog)
	for line in reader:
		words = line.split()
		if (('Total' in words) and ('(user):' in words)):
			time2+=float(words[4])
	reader.close()

	mySheet.Cells(pc, 33).Value = points
	mySheet.Cells(pc, 34).Value = total
	mySheet.Cells(pc, 35).Value = positions
	mySheet.Cells(pc, 37).Value = attributes
	mySheet.Cells(pc, 38).Value = time
	mySheet.Cells(pc, 39).Value = time2
	pc=pc+1


myBook.save


myBook.close
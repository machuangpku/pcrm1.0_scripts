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


mySheet = myBook.Worksheets("AVSC3 losslG,limit-lossyA,intra")

logpath = homedir + '\\log\\'
cond = 'C3-losslessG-limitlossyA-ai'
name1 = cond + '_'
C1_lst =  list([
'Livox_01_all_1mm',
'Livox_02_all_1mm'
])

r_lst = list([
		'r1',
		'r2',
		'r3',
		'r4',
		'r5'])

pc=85

for name2 in C1_lst:
	for name3 in r_lst:

		points = 0
		total = 0
		positions = 0
		attributes = 0
		time = 0
		time2 = 0
		D1 = 0
		D1h = 0
		Y = 0 
		U = 0
		V = 0
		R = 0
		Rh = 0

		enclog = (logpath + name1 + name3 + '_' + name2 + '_enc.log')
		declog = (logpath + name1 + name3 + '_' + name2 + '_dec.log')


		reader = open( enclog, 'r')
		for line in reader:
			words = line.split()
			if (('points' in words) and ('remained:' in words)) :
				points+= int(words[2])
			if (('points' in words) and ('(averaged):' in words)) :
				points+= int(words[5])
			if (('Geometry' in words) and ('bits:' in words)):
				positions+=int(words[2])
			if (('Attributes' in words) and ('bits:' in words)):
				attributes+=int(words[2])
			if (('Total' in words) and ('bitstream' in words)):
				total+=int(words[3])
			if ('D1_PSNR_F' in words):
				D1+=float(words[2])
			if ('D1_HausdorffPSNR_F' in words):
				D1h+=float(words[2])
			if ('rel_PSNR_Ave' in words):
				R=float(words[2])
			if ('rel_HausdroffPSNR_Ave' in words):
				Rh+=float(words[2])

			if (('Total' in words) and ('(user):' in words)):
				time+=float(words[4])
		reader.close()
		
		reader = open(declog)
		for line in reader:
			words = line.split()
			if (('Total' in words) and ('(user):' in words)):
				time2+=float(words[4])
		reader.close()

		mySheet.Cells(pc, 40).Value = points/2
		mySheet.Cells(pc, 41).Value = total
		mySheet.Cells(pc, 42).Value = positions
		mySheet.Cells(pc, 44).Value = attributes

		mySheet.Cells(pc, 48).Value = R
		mySheet.Cells(pc, 52).Value = Rh
		
		mySheet.Cells(pc, 53).Value = time
		mySheet.Cells(pc, 54).Value = time2
		pc=pc+1


myBook.save


myBook.close



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


mySheet = myBook.Worksheets("AVSC1 limit-lossyG,lossyA,intra")

logpath = homedir + '\\log\\'

cond = 'C1-limitlossyG-lossyA-ai'
name1 = cond + '_'

num_list=range(0,4,1)

C1_lst =  list([
'basketball_player_vox11',
'dancer_vox11',
'exercise_vox11',
'model_vox11'
])

C1_points =  [186907991,166028718,156840910,163936020]

r_lst = list([
		'r1',
		'r2',
		'r3',
		'r4',
		'r5',
		'r6',
])

pc=113

for num in num_list:
	name2=C1_lst[num]
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
		MSEh = 0

		enclog = (logpath + name1 + name3 + '_' + name2 + '_enc.log')
		declog = (logpath + name1 + name3 + '_' + name2 + '_dec.log')

		reader = open( enclog, 'r')
		for line in reader:
			words = line.split()
			if (('point' in words) and ('size:' in words)) :
				points+= int(words[3])
			if (('Geometry' in words) and ('bits:' in words)):
				positions+=int(words[2])
			if (('Attributes' in words) and ('bits:' in words)):
				attributes+=int(words[2])
			if (('Total' in words) and ('bitstream' in words)):
				total+=int(words[3])
			if ('D1_PSNR_Ave' in words):
				D1=float(words[2])
			if ('D1_HausdorffPSNR' in words):
				D1h=float(words[2])
			if ('c[0]_PSNR_Ave' in words):
				Y=float(words[2])
			if ('c[1]_PSNR_Ave' in words):
				U=float(words[2])
			if ('c[2]_PSNR_Ave' in words):
				V=float(words[2])
			if ('D1_Hausdorff_F' in words):
				MSEh+=float(words[2])
			if (('Total' in words) and ('(user):' in words)):
				time+=float(words[4])
		reader.close()
		
		reader = open(declog)
		for line in reader:
			words = line.split()
			if (('Total' in words) and ('(user):' in words)):
				time2+=float(words[4])
		reader.close()

		mySheet.Cells(pc, 38).Value = points-C1_points[num]
		mySheet.Cells(pc, 39).Value = total
		mySheet.Cells(pc, 40).Value = positions
		mySheet.Cells(pc, 41).Value = attributes
		mySheet.Cells(pc, 43).Value = D1
		mySheet.Cells(pc, 44).Value = D1h
		mySheet.Cells(pc, 45).Value = Y
		mySheet.Cells(pc, 46).Value = U
		mySheet.Cells(pc, 47).Value = V
		
		mySheet.Cells(pc, 49).Value = time
		mySheet.Cells(pc, 50).Value = time2
		
		mySheet.Cells(pc, 53).Value = MSEh/64
		
		pc=pc+1


myBook.save


myBook.close



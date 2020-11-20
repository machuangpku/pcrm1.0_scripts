import os 
import shutil

homedir = os.getcwd()
dirpath = homedir + '/'
cfgpath = dirpath + 'cfg/'
datasetpath = 'D:/AVS/dataset/'

encoder = dirpath + 'avs-pcc-encoder'
decoder = dirpath + 'avs-pcc-decoder'
logpath = dirpath + 'log/'
#每个线程不同的配置，参数表示为
#条件[0,4]，运行的数据集[0,9],
#C1运行的条件[0,6]，有损有损
#C2运行的条件[0,6]，无损有损
#C3运行的条件[0,5]，无损有限损
#C3运行的条件[0,1]，无损无损
#每行是一个线程
#目前默认设置是9线程，0.py-8.py
all_config=list([
[range(0,1),range(0,15),range(0,1)],
[range(0,1),range(0,15),range(1,2)],
[range(0,1),range(0,15),range(2,3)],
[range(0,1),range(0,15),range(3,4)],
[range(0,1),range(0,15),range(4,5)],
[range(0,1),range(0,15),range(5,6)],
[range(1,2),range(0,15),range(0,1)],
[range(1,2),range(0,15),range(1,2)],
[range(1,2),range(0,15),range(2,3)],
[range(1,2),range(0,15),range(3,4)],
[range(1,2),range(0,15),range(4,5)],
[range(1,2),range(0,15),range(5,6)],
[range(2,3),range(0,15),range(0,1)],
[range(2,3),range(0,15),range(1,2)],
[range(2,3),range(0,15),range(2,3)],
[range(2,3),range(0,15),range(3,4)],
[range(2,3),range(0,15),range(4,5)],
[range(3,4),range(0,15),range(0,1)],
])

cond_lst = list([
'C1-limitlossyG-lossyA-ai',
'C2-losslessG-lossyA-ai',
'C3-losslessG-limitlossyA-ai',
'C4-losslessG-losslessA-ai',
])

framenum_lst=list([
600,
600,
600,
387,
387,
64,
64,
64,
64,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
])

beginframe_lst=list([
[100,4],
[100,4],
[100,4],
[0,4],
[0,4],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[1,8],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
[0,0],
])

cfgtname_lst = list([
'Ford_01_AVS_1mm',
'Ford_02_AVS_1mm',
'Ford_03_AVS_1mm',
'Livox_01_all_in_one_1mm',
'Livox_02_all_in_one_1mm',
'basketball_player_vox11',
'dancer_vox11',
'exercise_vox11',
'model_vox11',
'intersection2_1mm',
'intersection1_1mm',
'T_section_1mm',
'bridge_1mm',
'double_T_section_1mm',
'straight_road_1mm',
#'stanford_area_2_vox20',
#'stanford_area_4_vox20',
#'Church_vox16',
#'Courthouse_vox16',
'Ignatius_vox11',
'QQdog_vox15',
'Truck_vox15',
])

datasetname_lst = list([
'Ford_01_1mm',
'Ford_02_1mm',
'Ford_03_1mm',
'Livox_01_all_1mm',
'Livox_02_all_1mm',
'basketball_player_vox11',
'dancer_vox11',
'exercise_vox11',
'model_vox11',
'intersection2_1mm',
'intersection1_1mm',
'T_section_1mm',
'bridge_1mm',
'double_T_section_1mm',
'straight_road_1mm',
#'stanford_area_2_vox20',
#'stanford_area_4_vox20',
#'Church_vox16',
#'Courthouse_vox16',
'Ignatius_vox11',
'QQdog_vox15',
'Truck_vox15',
])

r_lst = list([
'r1',
'r2',
'r3',
'r4',
'r5',
'r6',
])

def generateframestr(begin,count):
	framestr=str(begin).zfill(count)
	return framestr

def generateDataset(dataname,framenum,begin,count):
	datasetlst=list()
	for num in range(framenum):
		framestr=generateframestr(begin+num,count)
		datalst.append(dataname+framestr)
	return datasetlst

def copyexe(file,processnum):
	ori=file+'.exe'
	new=file+str(processnum)+'.exe'
	if(os.path.exists(new)):
		os.remove(new)
	shutil.copyfile(ori, new)
	return new


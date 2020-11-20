import os
from config import *

scriptsname=(os.path.basename(__file__))
processnum=int(scriptsname[0:1])
encoder=copyexe(encoder,processnum)
decoder=copyexe(decoder,processnum)


def run_exe(datasetpath,cfgpath,logpath,cond,datasetname,cfgname,qp,f_number,begin,count):
	if(count>0):
		framestr=generateframestr(begin,count)
		head='_' if count==8 else '-'
		seq=datasetpath+'/'+datasetname+head+framestr+'.ply'
	else:
		seq=datasetpath+'/'+datasetname+'.ply'
	cname=getcname(cond,datasetname,qp)
	encconfig=(cfgpath +cond+'/'+cfgname +'/'+qp+'/encoder.cfg')
	decconfig=(cfgpath +cond+'/'+cfgname +'/'+qp+'/decoder.cfg')
	if(cond=='C4-losslessG-losslessA-ai'):
		encconfig=(cfgpath +cond+'/'+cfgname +'/encoder.cfg')
		decconfig=(cfgpath +cond+'/'+cfgname +'/decoder.cfg')
	enc=(logpath+cname+'_enc.ply')
	dec=(logpath+cname+'_dec.ply')
	bin=(logpath+cname+'.bin')
	bin2=(logpath+cname+'-'+framestr+'.bin') if f_number>1 else bin
	md5_enc=(logpath+cname+'_md5enc.txt')
	md5_dec=(logpath+cname+'_md5dec.txt')
	enclog=(logpath+cname+'_enc.log')
	declog=(logpath+cname+'_dec.log')
	print(cname)
	os.system(encoder+' -c '+encconfig+' -i '+seq+' -b '+bin+' -ftbc '+str(f_number)+' -mdf '+md5_enc +' >'+enclog)
	os.system(decoder+' -c '+decconfig+' -b '+bin2+' -ftbc '+str(f_number)+' -mdf '+md5_enc+' >'+declog)
	if f_number>1:
		for num in range(f_number):
			framestr=generateframestr(begin+num,count)
			dec=(logpath+cname+'_dec-'+framestr+'.ply')
			bin=(logpath+cname+'-'+framestr+'.bin')
			#os.remove(dec)
			os.remove(bin)
	else:
		dec=(logpath+cname+'_dec.ply')
		bin=(logpath+cname+'.bin')
		#os.remove(dec)
		os.remove(bin)

def getcname(cond,datasetname,qp):
	cname=cond+'_'+qp+'_'+datasetname
	return cname

cond_cfg,name_cfg,qp_cfg=all_config[processnum]
for condnum in cond_cfg:
	cond=cond_lst[condnum]
	for namenum in name_cfg:
		datasetname=datasetname_lst[namenum]
		framenum=framenum_lst[namenum]
		begin,count=beginframe_lst[namenum]
		cfgname=cfgtname_lst[namenum]
		for qpnum in qp_cfg:
			qp=r_lst[qpnum]
			run_exe(datasetpath,cfgpath,logpath,cond,datasetname,cfgname,qp,framenum,begin,count)


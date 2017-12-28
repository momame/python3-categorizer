
import io,json,os

category_name={}
domain_dict={}
start = os.getcwd()
categories=[]

with io.open("global_usage",'r',encoding="utf8") as fp:
	for i,line in enumerate(fp):
		# for i,word in enumerate(line.split()):	
		# for word in enumerate(line.split()):
		if (line.find('NAME:')==0):
			befor_keyowrd, keyword, after_keyword = line.partition(":")
			# print(after_keyword.lstrip())
			category_name[""+after_keyword.lstrip().strip()+""]={}
		if (line.find('NAME EN:')==0):
			befor_kw, keyw, after_kw = line.partition(":")
			# print(after_kw.lstrip())
			category_name[""+after_keyword.lstrip().strip()+""]["name"]=after_kw.lstrip().strip()
		if (line.find('DESC EN:')==0):
			before, key, after = line.partition(":")
			# print(after.lstrip())
			category_name[""+after_keyword.lstrip().strip()+""]["description"]=after.lstrip().strip()		
		

with open('dic.json', 'w') as outfile:  
    json.dump(category_name, outfile)


with open('dic.json') as data_file:    
    data = json.load(data_file)   
    for key in data.keys():categories.append(key) 	

for dirpath, dirnames, filenames in os.walk(start):
	for category in categories:
		if category==os.path.basename(os.path.normpath(dirpath)): 
			# print(dirpath)
			if (os.path.isfile(dirpath+"/domains")):
				with io.open(dirpath+'/domains','r',encoding="utf8") as dom_file:
					for i,lin in enumerate(dom_file):
						if not hasattr(domain_dict,""+lin.lstrip().strip()+""):
							domain_dict[""+lin.lstrip().strip()+""]={}
						if not hasattr(domain_dict[""+lin.lstrip().strip()+""], "categories"):
							domain_dict[""+lin.lstrip().strip()+""]["categories"]=[]
						domain_dict[""+lin.lstrip().strip()+""]["categories"].append(category)

with open('domain_dict.json', 'w') as dom:  
	json.dump(domain_dict, dom)
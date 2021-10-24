

import df_val_set as dvs

import os

import pickle


#вывести текущий путь
curr_dir = os.getcwd();
print('curr_dir = ' + curr_dir);

#Получаем список файлов в переменную files
files = os.listdir(curr_dir);
print('cnt files: ', len(files));

#пробую вывести файлы
for file in files:
	print(file);

print('');
DATA_DIR = '/storage/emulated/0/data/Db'
DATA_DIR = 'D:/data/dbs/fox'
PY_DIR = '/storage/emulated/0/data/my_python'
PY_DIR = 'C:/Users/Sam/Documents/repo/pydroid_folder'
CHKPNT_FILE = 'chkpntfil.chp'

os.chdir(DATA_DIR)

curr_dir = os.getcwd();
print('curr_dir = ' + curr_dir);

files = os.listdir(curr_dir );
print('cnt files: ', len(files));

#пробую вывести файлы
for file in files:
	print(file);




filename = '2_5433639494983094589.csv';
filename = 'VK_128M.txt';

colname = 'last_name';
colnum = 0;
separator =',';
goon = 1;	# 0 - начать файл с начала.
# словарь, который должен описать, какие домены интересуют, в каких столбцах их искать, в каких файлах хранить.
dict_cols = {
	'surname': {
		'colname': 'last_name'
		, 'filename': 'secondnames.csv'
		, 'colnum' : 0
		}
	, 'name': {
		'colname': 'last_name'
		, 'filename': 'names.csv'
		, 'colnum' : 0
		}
	, 'phone': {
		'colname': 'phone'
		, 'filename': 'phones.csv'
		, 'colnum' : 0
		}
	, 'username': {
		'colname': 'username'
		, 'filename': 'username.csv'
		, 'colnum' : 0
		}
};

dfnam = dvs.Df_val_cnt(PY_DIR+'/'+'names.csv');
dfsur = dvs.Df_val_cnt(PY_DIR+'/'+'secondnames.csv', 'secondname');
dfmail = dvs.Df_val_cnt(PY_DIR+'/'+'emails.csv');
dfphon = dvs.Df_val_cnt(PY_DIR+'/'+'phones.csv');
dfnick = dvs.Df_val_cnt(PY_DIR+'/'+'nicks.csv');
dffio = dvs.Df_fio(PY_DIR+'/'+'fio.csv');
dfsrc = dvs.Df_val_cnt(PY_DIR+'/'+'src.csv');
lnk_fio_phone = dvs.Df_link(PY_DIR+'/'+'fio_phones.csv');
lnk_fio_nick = dvs.Df_link(PY_DIR+'/'+'fio_nick.csv');

# Добавляю файл-источник
src_id = dfsrc.get_index(filename);

print('');
#with open(DATA_DIR + '/' + filename, "r", encoding='cp1251') as txtf:
with open(DATA_DIR + '/' + filename, "r", encoding='utf8') as txtf:
	numrow = 1
	for line in txtf:
		line_split = line.split(separator);
		#по первой строке определю где что
		if numrow == 1:
			print(line);
			print('len: ', str(len(line.split(separator))));
			#разобью первую строку по столбцам
			
			for dict_el in dict_cols:
				colname = dict_cols[dict_el]['colname'];
				print('looking for colnane ', colname);
			
				# найти номер столбца поля colname
				for i in range(len(line_split)) :
					print(line_split[i]);
					if colname == line_split[i].strip():
						colnum = i;
						dict_cols[dict_el]['colnum'] = i;
						print('colnum:', colnum);
						
			# если продолжать,то загружаем словарь из файла
			if goon == 1 and os.path.isfile(CHKPNT_FILE):
				with open(CHKPNT_FILE, "rb") as fchp:
					d = pickle.load(fchp);
					print('checkpoint loading. numrow: ', d['numrow']);
				for _ in range(d['numrow']):
					next(txtf);
				numrow = d['numrow'];
				goon = 0;
		# numrow != 1
		else:
			#print('step 1');
			# фамилия
			surn_id = dfsur.get_index(line_split[dict_cols['surname']['colnum']]);
			#print('surn: ', surn_id, );
			
			# имя
			#print('step 2');
			nam_id = dfnam.get_index(line_split[dict_cols['name']['colnum']]);
			#print('name: ', nam_id);
			
			# телефон
			#print('step 3');
			phon_id = dfphon.get_index(line_split[dict_cols['phone']['colnum']]);
			#print('phon: ', phon_id);
			
			# username
			#print('step 4');
			unam_id = dfnick.get_index(line_split[dict_cols['username']['colnum']]);
		#	print('unam: ', unam);
			
            
			# фио: фамилия, имя
			#print('step 5');
			fio_id = dffio.get_index(str(surn_id), str(nam_id));
			#print('fio: ', fio_id);
			
			# lnk(фио, телефон)
			#print('step 6');
			lnk_fio_phone.ins_element(str(fio_id), str(phon_id));
			
			# lnk(фио, ник)
			lnk_fio_nick.ins_element(str(fio_id), str(unam_id));
			
			if colnum != 0:
				if dfsur.appended((line.split(separator)[i])):
					print(line.split(separator)[i]);
		
		numrow += 1;
		# сохранения и индикация
		if (numrow % 1000 == 0):
			#break
			print(numrow, ' - ' * 30)
			dfnam.save();
			dfsur.save();
			dfmail.save();
			dfphon.save();
			dfnick.save();
			dffio.save();
			lnk_fio_phone.save();
			lnk_fio_nick.save();
			# сохранить текущее состояние,чтобы можно было начать с того же места
			with open(CHKPNT_FILE, "wb") as fchp:
				d = {
				 	'file_name': filename
					, 'numrow' : numrow
					};
				pickle.dump(d, fchp);
				
			
dfnam.save();
dfsur.save();
dfmail.save();
dfphon.save();
dfnick.save();
dffio.save();
lnk_fio_phone.save();
lnk_fio_nick.save();

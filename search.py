
import df_val_set as dvs
import pandas as pd

PY_DIR = '/storage/emulated/0/data/my_python';
PY_DIR = 'C:/Users/Sam/Documents/repo/pydroid_folder'

print('искать ');
#inp = input('введите: ');
inp = 'самойлов';
print (inp);


dfnam = dvs.Df_val_cnt(PY_DIR+'/'+'names.csv');
dfsur = dvs.Df_val_cnt(PY_DIR+'/'+'secondnames.csv', 'secondname');
dfmail = dvs.Df_val_cnt(PY_DIR+'/'+'emails.csv');
dfphon = dvs.Df_val_cnt(PY_DIR+'/'+'phones.csv');
dfnick = dvs.Df_val_cnt(PY_DIR+'/'+'nicks.csv');
dffio = dvs.Df_fio(PY_DIR+'/'+'fio.csv');
lnk_fio_phone = dvs.Df_link(PY_DIR+'/'+'fio_phones.csv');
lnk_fio_nick = dvs.Df_link(PY_DIR+'/'+'fio_nick.csv');


# найти фио людей,у которых фамилия,имя или отчество совпадает с lf_string
def search_fio(lf_string):
	df_lf_nam = pd.DataFrame([], columns=['name', 'cnt']);
	if dfnam.in_list(lf_string):
		#nam_ind = dfnam.get_index(lf_string);
		df_lf_nam = dfnam.find_rows(lf_string);
		print(df_lf_nam);
	if dfsur.in_list(lf_string):
		#sur_ind = dfsur.get_index(lf_string);
		df_lf_sur = dfsur.find_rows(lf_string);
		print(df_lf_sur);
	#найти фио в которых содержатся такие имя или фамилия
	df_lf_fio = pd.DataFrame([], columns=['surname', 'name', 'secondname', 'md5']);
	print(df_lf_fio);
	if len(df_lf_nam.index) > 0:
		print(dffio.find_rows_like(df_lf_nam['name']));		

print();
search_fio(inp);





import csv

c_list = ["com_c", "cus_c", "emp_c", "inv_c", "sup_c", "soc_c", "pri_c", "env_c"]
p_list = ["com_p", "cus_p", "emp_p", "inv_p", "sup_p", "soc_p", "env_p"]
m_list = ["cus_m", "inv_m", "env_m", "sum_m"]


model_list = [['model_name', 'model_parms']]
cmd_str = ''
out_file1 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models.csv'
out_file2 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models.r'

c_mod_dic = {}
p_mod_dic = {}
m_mod_dic = {}

f_dic = {
    "n":"NPM",
    "a":"ROA",
    "e": "ROE",
    "o": ""
}

z_dic = {
    "r":"revt",
    "o": ""
}

e_dic = {
    "p":"PE",
    "o": ""
}

i_dic = {
    "i":"own_inst_p",
    "o": ""
}

b_dic = {
    "b":"own_block_p",
    "o": ""
}

g_dic = {
    "4":"GICS4",
    "6":"GICS6",
    "8": "GICS8",
    "o": ""
}

for c in c_list:
    for f_key, f_val in f_dic.items():
        for z_key, z_val in z_dic.items():
            for e_key, e_val in e_dic.items():
                for i_key, i_val in i_dic.items():
                    for b_key, b_val in b_dic.items():
                        for g_key, g_val in g_dic.items():

                            if f_key == 'o':
                                fb = ''
                                fi = ''
                            else:
                                fb = ' + ' + f_val
                                fi = ' + fy:' + f_val

                            if z_key == 'o':
                                zb = ''
                                zi = ''
                            else:
                                zb = ' + ' + z_val
                                zi = ' + fy:' + z_val

                            if e_key == 'o':
                                eb = ''
                                ei = ''
                            else:
                                eb = ' + ' + e_val
                                ei = ' + fy:' + e_val

                            if i_key == 'o':
                                ib = ''
                                ii = ''
                            else:
                                ib = ' + ' + i_val
                                ii = ' + fy:' + i_val

                            if b_key == 'o':
                                bb = ''
                                bi = ''
                            else:
                                bb = ' + ' + b_val
                                bi = ' + fy:' + b_val

                            if g_key == 'o':
                                gb = ''
                                gi = ''
                            else:
                                gb = ' + ' + g_val
                                gi = ' + fy:' + g_val

                            n = c + '_' + f_key + z_key + i_key + b_key + g_key + '.lm'
                            s = c + ' ~ fy ' + fb + zb + eb + ib + bb + gb + \
                                fi + zi + ei + ii + bi + gi + ', data = MSS'
                            print (n, s)
                            model_list.append([n,s])
                            os = n + ' <- ' + 'lm(' + s + ')\n'
                            print(os)
                            cmd_str = cmd_str + os


for p in p_list:
    for f_key, f_val in f_dic.items():
        for z_key, z_val in z_dic.items():
            for e_key, e_val in e_dic.items():
                for i_key, i_val in i_dic.items():
                    for b_key, b_val in b_dic.items():
                        for g_key, g_val in g_dic.items():

                            if f_key == 'o':
                                fb = ''
                                fi = ''
                            else:
                                fb = ' + ' + f_val
                                fi = ' + fy:' + f_val

                            if z_key == 'o':
                                zb = ''
                                zi = ''
                            else:
                                zb = ' + ' + z_val
                                zi = ' + fy:' + z_val

                            if e_key == 'o':
                                eb = ''
                                ei = ''
                            else:
                                eb = ' + ' + e_val
                                ei = ' + fy:' + e_val

                            if i_key == 'o':
                                ib = ''
                                ii = ''
                            else:
                                ib = ' + ' + i_val
                                ii = ' + fy:' + i_val

                            if b_key == 'o':
                                bb = ''
                                bi = ''
                            else:
                                bb = ' + ' + b_val
                                bi = ' + fy:' + b_val

                            if g_key == 'o':
                                gb = ''
                                gi = ''
                            else:
                                gb = ' + ' + g_val
                                gi = ' + fy:' + g_val


                            n = p + '_' + f_key + z_key + i_key + b_key + g_key + '.lm'
                            s = p + ' ~ fy ' + fb + zb + eb + ib + bb + gb + \
                                fi + zi + ei + ii + bi + gi + ', data = MSS'
                            print (n, s)
                            model_list.append([n,s])
                            os = n + ' <- ' + 'lm(' + s + ')\n'
                            print(os)
                            cmd_str = cmd_str + os

for m in m_list:
    for f_key, f_val in f_dic.items():
        for z_key, z_val in z_dic.items():
            for e_key, e_val in e_dic.items():
                for i_key, i_val in i_dic.items():
                    for b_key, b_val in b_dic.items():
                        for g_key, g_val in g_dic.items():

                            if f_key == 'o':
                                fb = ''
                                fi = ''
                            else:
                                fb = ' + ' + f_val
                                fi = ' + fy:' + f_val

                            if z_key == 'o':
                                zb = ''
                                zi = ''
                            else:
                                zb = ' + ' + z_val
                                zi = ' + fy:' + z_val

                            if e_key == 'o':
                                eb = ''
                                ei = ''
                            else:
                                eb = ' + ' + e_val
                                ei = ' + fy:' + e_val

                            if i_key == 'o':
                                ib = ''
                                ii = ''
                            else:
                                ib = ' + ' + i_val
                                ii = ' + fy:' + i_val

                            if b_key == 'o':
                                bb = ''
                                bi = ''
                            else:
                                bb = ' + ' + b_val
                                bi = ' + fy:' + b_val

                            if g_key == 'o':
                                gb = ''
                                gi = ''
                            else:
                                gb = ' + ' + g_val
                                gi = ' + fy:' + g_val

                            n = m + '_' + f_key + z_key + i_key + b_key + g_key + '.lm'
                            s = m + ' ~ fy' + fb + zb + eb + ib + bb + gb + \
                                fi + zi + ei + ii + bi + gi + ', data = MSS'
                            print (n, s)
                            model_list.append([n,s])
                            os = n + ' <- ' + 'lm(' + s + ')\n'
                            print (os)
                            cmd_str = cmd_str + os


print (model_list)
print (len(model_list))
print (cmd_str)

with open(out_file1, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(model_list)

text_file =  open(out_file2, 'w')
text_file.write (cmd_str)
text_file.close()

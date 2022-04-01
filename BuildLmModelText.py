# BuildLmModelText.py
# This file builds a script to run in R. It generates commands to build the following models:
#
# sss_m_y_fzeibg.lm
# where:
#   • sss_m_:
#     - com_c, cus_c, emp_c, inv_c, sup_c, soc_c, pri_c, env_c
#     - com_p, cus_p, emp_p, inv_p, sup_p, soc_p, env_p
#     - cus_m, inv_m, env_m, sum_m
#
#   • y: years in study, with the number in hex
#     - b: 2009 to 2019 (11 years)
#     - f: 2005 to 2019 (15 years)
#
#   • f: n = NPM, a = ROA, e=ROE, 0 - 4
#   • z: r = revt, 0 - 2
#   • e: p = PE, 0 - 2
#   • i: i = own_inst_p, 0 - 2
#   • b: b = own_block_p, 0 - 2
#   • g: 1 = GICS2, 2 = GICS4, 3 = GICS6, 4 = GICS8

import csv

c_list = ["com_c", "cus_c", "emp_c", "inv_c", "sup_c", "soc_c", "pri_c", "env_c"]
p_list = ["com_p", "cus_p", "emp_p", "inv_p", "sup_p", "soc_p", "env_p"]
m_list = ["cus_m", "inv_m", "env_m", "sum_m"]


model_list = [['model_name', 'model_parms']]
cmd_str = ''
#df_str = 'lm_df <- data.frame("mod_name" = character(), "adj_rsq" = double(), "f_stat" = double(), "stakeholder" = character, "measure" = factor(), "gics" = factor())\n'
df_str = 'lm_df <- data.frame("mod_name" = character(), "adj_rsq" = double(), "f_stat" = double(), "stakeholder" = character(), "measure" = character(), "gics" = character(), "years" = character())\n'
out_file1 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models.csv'
out_file2 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models.r'
out_file3 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/lm_df.r'

c_mod_dic = {}
p_mod_dic = {}
m_mod_dic = {}

y_dic = {
    "b":"MSS11",
    "d":"MSS9",
    "e": "MSS"
}

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
    "2":"GICS4",
    "3":"GICS6",
    "4": "GICS8",
    "1": ""
}

for c in c_list:
    for f_key, f_val in f_dic.items():
        for y_key, y_val in y_dic.items():
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

                                if g_key == '1':
                                    gb = ''
                                    gi = ''
                                else:
                                    gb = ' + ' + g_val
                                    gi = ' + fy:' + g_val

                                n = c + '_' + y_key + '_' + f_key + z_key + e_key + i_key + b_key + g_key + '.lm'
                                s = c + ' ~ fy ' + fb + zb + eb + ib + bb + gb + \
                                    fi + zi + ei + ii + bi + gi + ', data = ' + y_val
                                print (n, s)
                                model_list.append([n,s])
                                os = n + ' <- ' + 'lm(' + s + ')\n'
                                ds = 'lm_df[nrow(lm_df) +1 ,] <- c("' + n + '", summary(' + n + ')$adj.r.squared, summary(' + n + ')$fstatistic[1], "' + c[0:3] + '", "' + c[-1] + '", "' + g_key + '", "' + y_key + '")\n'
                                print(os)
                                cmd_str = cmd_str + os
                                df_str = df_str + ds


for p in p_list:
    for f_key, f_val in f_dic.items():
        for y_key, y_val in y_dic.items():
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

                                if g_key == '1':
                                    gb = ''
                                    gi = ''
                                else:
                                    gb = ' + ' + g_val
                                    gi = ' + fy:' + g_val


                                n = p + '_' + y_key + '_' + f_key + z_key + e_key + i_key + b_key + g_key + '.lm'
                                s = p + ' ~ fy ' + fb + zb + eb + ib + bb + gb + \
                                    fi + zi + ei + ii + bi + gi + ', data = ' + y_val
                                print (n, s)
                                model_list.append([n,s])
                                os = n + ' <- ' + 'lm(' + s + ')\n'
                                ds = 'lm_df[nrow(lm_df) +1 ,] <- c("' + n + '", summary(' + n + ')$adj.r.squared, summary(' + n + ')$fstatistic[1], "' + p[0:3] + '", "' + p[-1] + '", "' + g_key + '", "' + y_key + '")\n'
                                print(os)
                                print (ds)
                                cmd_str = cmd_str + os
                                df_str = df_str + ds

for m in m_list:
    for f_key, f_val in f_dic.items():
        for y_key, y_val in y_dic.items():
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

                                if g_key == '1':
                                    gb = ''
                                    gi = ''
                                else:
                                    gb = ' + ' + g_val
                                    gi = ' + fy:' + g_val

                                n = m + '_' + y_key + '_' + f_key + z_key + e_key + i_key + b_key + g_key + '.lm'
                                s = m + ' ~ fy' + fb + zb + eb + ib + bb + gb + \
                                    fi + zi + ei + ii + bi + gi + ', data = ' + y_val
                                print (n, s)
                                model_list.append([n,s])
                                os = n + ' <- ' + 'lm(' + s + ')\n'
                                ds = 'lm_df[nrow(lm_df) +1 ,] <- c("' + n + '", summary(' + n + ')$adj.r.squared, summary(' + n + ')$fstatistic[1], "' + m[0:3] + '", "' + m[-1] + '", "' + g_key + '", "' + y_key + '")\n'
                                print (os)
                                print (ds)
                                cmd_str = cmd_str + os
                                df_str = df_str + ds



print (model_list)
print (len(model_list))
print (cmd_str)
print (df_str)

df_str = df_str + "lm_df[,'stakeholder'] <- as.factor(lm_df[, 'stakeholder'])\n"
df_str = df_str + "lm_df[,'measure'] <- as.factor(lm_df[, 'measure'])\n"
df_str = df_str + "lm_df[,'gics'] <- as.factor(lm_df[, 'gics'])\n"
df_str = df_str + "lm_df[,'years'] <- as.factor(lm_df[, 'years'])\n"

with open(out_file1, 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write multiple rows
    writer.writerows(model_list)

text_file2 =  open(out_file2, 'w')
text_file2.write (cmd_str)
text_file2.close()

text_file3 =  open(out_file3, 'w')
text_file3.write (df_str)
text_file3.close()

# Need to structure commands like this too.
# lm_df[nrow(lm_df) +1 ,] <- c("inv_p_nrpib8.lm", summary(inv_p_nrpib8.lm)$adj.r.squared, summary(inv_p_nrpib8.lm)$fstatistic[1])
#ds = 'lm_df[nrow(lm_df) +1 ,] <- c("' + n + '", summary(' + n + ')$adj.r.squared, summary(' + n + ')$fstatistic[1])'

# BuildLmModelText2.py
# This file builds a script to run in R. It generates commands to build the following models.
# This second file is substantially improved over the first as it only has one loop instead of the three very repetitive ones.
#
# sss_m_y_fzeibg.lm
# where:
#   • sss_m_:
#     - com_m, cus_m, emp_m, inv_m, sup_m, soc_m, pri_m, env_m
#     - com_c, cus_c, emp_c, inv_c, sup_c, soc_c, pri_c, env_c
#     - com_p, cus_p, emp_p, inv_p, sup_p, soc_p, env_p
#
#   • y: years in study, with the number in hex
#     - b: 2009 to 2019 (11 years)
#
#   • f: n = NPM, or 0
#   • z: r = revt, or 0
#   • e: p = PE, or 0
#   • i: i = own_inst_p, or 0
#   • b: b = own_block_p, or 0
#   • t: t = Ticker, or 0
#   • g: 2 = GICS2, 4 = GICS4, 6 = GICS6, 8 = GICS8

import csv

m_list = ["com_m", "cus_m", "emp_m", "inv_m", "sup_m", "soc_m", "pri_m", "env_m"] # Mention
c_list = ["com_c", "cus_c", "emp_c", "inv_c", "sup_c", "soc_c", "pri_c", "env_c"] # Count
p_list = ["com_p", "cus_p", "emp_p", "inv_p", "sup_p", "soc_p", "env_p"] # Mix
s_list = m_list + c_list + p_list


model_list = [['model_name', 'model_parms']]
cmd_str = ''
#df_str = 'lm2_df <- data.frame("mod_name" = character(), "adj_rsq" = double(), "f_stat" = double(), "stakeholder" = character(), "measure" = character(), "gics" = character(), "years" = character())\n'
df_str = 'lm2_df <- data.frame("mod_name" = character(), "adj_rsq" = double(), "f_stat" = double(), "p_val" = double(), ' \
         '"stakeholder" = character(), "measure" = character(), "years" = character(), ' \
         '"fin_perf" = character(), "size" = character(), "stock_perf" = character(), ' \
         '"inst_own" = character(), "block_own" = character(), "ticker" = character(), "gics" = character())\n'
out_file1 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models2.csv'
out_file2 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/models2.r'
out_file3 = '/Users/moranmarkd/OneDrive/Academics/Illinois/Dissertation/Paper1/Scripts/lm2_df.r'

c_mod_dic = {}
p_mod_dic = {}
m_mod_dic = {}

y_dic = {
    "b":"EsgShort"
}

f_dic = {
    "n":"NPM",
    "0": ""
}

z_dic = {
    "r":"revt",
    "0": ""
}

e_dic = {
    "p":"PE",
    "0": ""
}

i_dic = {
    "i":"own_inst_p",
    "0": ""
}

b_dic = {
    "b":"own_block_p",
    "0": ""
}
t_dic = {
    "t":"Ticker",
    "0": ""
}

g_dic = {
    "1": "",
    "2": "GICS4",
    "3":"GICS6",
    "4": "GICS8"
}

# Previous version had three separate loops, one for each stakeholder group.
# I have now made a single pass by making all three of sthe stakeholder lists one by simply adding them.

for l in s_list:
    for f_key, f_val in f_dic.items():
        for y_key, y_val in y_dic.items():
            for z_key, z_val in z_dic.items():
                for e_key, e_val in e_dic.items():
                    for i_key, i_val in i_dic.items():
                        for b_key, b_val in b_dic.items():
                            for t_key, t_val in t_dic.items():
                                for g_key, g_val in g_dic.items():

                                    if f_key == '0':
                                        fb = ''
                                        fi = ''
                                    else:
                                        fb = ' + ' + f_val
                                        fi = ' + fy:' + f_val

                                    if z_key == '0':
                                        zb = ''
                                        zi = ''
                                    else:
                                        zb = ' + ' + z_val
                                        zi = ' + fy:' + z_val

                                    if e_key == '0':
                                        eb = ''
                                        ei = ''
                                    else:
                                        eb = ' + ' + e_val
                                        ei = ' + fy:' + e_val

                                    if i_key == '0':
                                        ib = ''
                                        ii = ''
                                    else:
                                        ib = ' + ' + i_val
                                        ii = ' + fy:' + i_val

                                    if b_key == '0':
                                        bb = ''
                                        bi = ''
                                    else:
                                        bb = ' + ' + b_val
                                        bi = ' + fy:' + b_val

                                    if t_key == '0':
                                        tb = ''
                                        ti = ''
                                    else:
                                        tb = ' + ' + t_val
                                        ti = ' + fy:' + t_val


                                    if g_key == '1':
                                        gb = ''
                                        gi = ''
                                    else:
                                        gb = ' + ' + g_val
                                        gi = ' + fy:' + g_val

                                    n = l + '_' + y_key + '_' + f_key + z_key + e_key + i_key + b_key + t_key + g_key + '.lm'
                                    s = l + ' ~ fy ' + fb + zb + eb + ib + bb + tb + gb + \
                                        fi + zi + ei + ii + bi + ti +  gi + ', data = ' + y_val
                                    print (n, s)
                                    model_list.append([n,s])
                                    os = n + ' <- ' + 'lm(' + s + ')\n'
                                    ds = 'lm2_df[nrow(lm2_df) +1 ,] <- c("' + n + '", summary(' + n + ')$adj.r.squared, summary(' + n + ')$fstatistic[1], ' + 'lmp(' + n + ')'
                                    ds = ds + ', ' + '"' + l[0:3] + '", "' + l[-1] + '", "' + y_key + '"'
                                    ds = ds + ', ' + '"' + f_key + '", "' + z_key + '", "' + e_key + '"'
                                    ds = ds + ', ' + '"' + i_key + '", "' + b_key + '", "' + t_key + '", "' + g_key + '"' + ')\n'
                                    print(os)
                                    cmd_str = cmd_str + os
                                    df_str = df_str + ds

# df_str = 'lm2_df <- data.frame("mod_name" = character(), "adj_rsq" = double(), "f_stat" = double(), "p_val" = double(), ' \
#          '"stakeholder" = character(), "measure" = character(), "years" = character(), ' \
#          '"fin_perf" = character(), "size" = character(), "stock_perf" = character(), ' \
#          '"inst_own" = character(), "block_own" = character(), "ticker" = character(), "gics" = character())\n'


print (model_list)
print (len(model_list))
print (cmd_str)
print (df_str)

df_str = df_str + "lm2_df[,'stakeholder'] <- as.factor(lm2_df[, 'stakeholder'])\n"
df_str = df_str + "lm2_df[,'measure'] <- as.factor(lm2_df[, 'measure'])\n"
df_str = df_str + "lm2_df[,'gics'] <- as.factor(lm2_df[, 'gics'])\n"
df_str = df_str + "lm2_df[,'years'] <- as.factor(lm2_df[, 'years'])\n"
df_str = df_str + "lm2_df[,'gics'] <- as.numeric(lm2_df[, 'gics'])\n"
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
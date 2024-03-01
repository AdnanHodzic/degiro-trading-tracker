#!/usr/bin/env python3
#
# Degiro trading tracker:
# Simplified tracking of your investments
# 
# Blog post: https://foolcontrol.org/?p=3614
#
# Copyleft: Adnan Hodzic <adnan@hodzic.org>
# License: GPLv3

import pandas as pd
import sys

sepup = "\n" + 6 * "----" + " Degiro trading tracker " + 6 * "---" + "\n"
sep = "\n" + 22 * "---" + "\n"

if len(sys.argv) <= 1:
    print(sepup)
    print("ERROR:\nSecond argument should be path to file you want to analyze\n")
    print("Example:\npython3 degiro-trading-tracker.py ~/Documents/Transactions.xls")
    print(sep)
    sys.exit()

# excel loc/file setup
excel_file = sys.argv[1]
df = pd.read_excel(excel_file)

# define Kosten column (fee cost init)
fc = df["Transactiekosten en/of "]

# replace , with . + convert str to
fc = fc.str.replace(",", ".").astype(float)

# turn negative into positive
df["AbsKosten"] = fc.abs()

# generate sum + round to 2 decimals
fc_sum = df["AbsKosten"].sum()
fcf = round(fc_sum, 2)

# set beginning & end date
dbeg = df["Datum"].tail(1).to_string(index=False).strip()
dend = df["Datum"].head(1).to_string(index=False).strip()

# define Totaal column (portofolio cost init)
pc = df["Totaal"]

# replace "." with "" & "," with "."
pc = pc.str.replace('.', '')
pc = pc.str.replace(',', '.')

# cherry pick positives (portofolio sale init)
poslst = []
for line in pc:
    if not line.startswith('-'):
        poslst.append(line)

# replace "." with "" & "," with "." in poslst
ps = [sub.replace(',', '').replace(',','.') for sub in poslst] 

# convert str + int to float (sales) 
import numpy as np
ps=np.array(ps,float)

ps = sum(ps)
ps = round(ps, 2)

# turn str to float (portofolio costs)
pc = pc.astype(float)

# turn negatives into positive
df["AbsTotaal"] = pc.abs()

# generate sum + round to 2 decimals
pc_sum = df["AbsTotaal"].sum()
pcf = pc_sum - ps
pcf = round(pcf - ps, 2)

# headings
hFee = "Fee costs"
hSell = "Stock sales"
hCosts = "Stock costs"

# output
print(sepup)
print("Analysis made by using:", excel_file, "\n")
print("\nTotal Degiro portofolio investment ...")
print("\nfrom:", dbeg, "\nto:  ", dend, "\n")
print("%-20s  %-20s  %s" %(hCosts, hSell, hFee))
print("€%-20s €%-20s €%s" %(pcf, ps, fcf))
print(sep)
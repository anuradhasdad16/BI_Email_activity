#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 22:59:59 2018

@author: anuradha
"""

import csv
from urllib.request import urlopen 
from bs4 import BeautifulSoup

quote_page = 'file:///home/anuradha/Downloads/Job Z_SAPMSM66_WEEKEND_1027-1028_Step 1.htm'

page = urlopen(quote_page)

soup = BeautifulSoup(page,'html.parser')

p = soup.find_all('p')
#p = blockquote.find_all('p')

cnt_tr = 0
cnt_nobr = 0
cnt_p = 1
cnt = 1
list_of_nobr = []  

for in_p in p:
    if cnt_p == 1:
        cnt_p+=1
    else:
        table = in_p.find_all('table')
        for in_table in table:
            tr = in_table.find_all('tr')
            for in_tr in tr:
                cnt_tr+=1 
                list_of_nobr.clear()
                nobr = in_tr.find_all('nobr')
                
                for in_nobr in nobr:
                    cnt_nobr+=1
                    name = in_nobr.text.strip()
                    list_of_nobr.append(name)
                    
#                print(list_of_nobr)
                if cnt==1:
                    cnt-=1
                    print(list_of_nobr)
                else:
                    pass
                
                file = open('/home/anuradha/spyder_codes/csvFile.csv', 'a')
                with file as csv_file:
                    writer = csv.writer(csv_file)
                    writer.writerow(list_of_nobr)
                file.close()    
              
               
#            print(cnt_tr)














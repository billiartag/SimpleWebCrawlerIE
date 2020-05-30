import xmltodict
import json
import xml.etree.ElementTree as ET
import time
 
path="/hasil"

import os,sys
semuaRaw=[]
print(json.dumps(semuaRaw))
semuaProc=[]
ctr=0

for filename in os.listdir(os.getcwd()+"\\baru\\"):
   print(ctr)
   with open(os.getcwd()+"\\baru\\"+filename, 'r', encoding="utf8") as f: 
      teks =ET.parse(f)
      root= teks.getroot()
      yes=False
      rawFile={}
      procFile={}
      for x in root:
         if(x.tag=="judul"):
            procFile['title']=x.text
         if(x.tag=="isi"):
            procFile['content']=x.text
         if(x.tag=="tanggalPost"):
            tanggal = x.text.split(", ")
            if(len(tanggal)!=1):
               tahun = tanggal[1]
               pecah = tanggal[0].split(" ")
               bulan = pecah[0]
               tanggal = pecah[1]
               bln = ""
               if(bulan=="January"): bln="01"
               elif(bulan=="February"): bln="02"
               elif(bulan=="March"): bln="03"
               elif(bulan=="April"): bln="04"
               elif(bulan=="May"): bln="05"
               elif(bulan=="June"): bln="06"
               elif(bulan=="July"): bln="07"
               elif(bulan=="August"): bln="08"
               elif(bulan=="September"): bln="09"
               elif(bulan=="October"): bln="10"
               elif(bulan=="November"): bln="11"
               elif(bulan=="December"): bln="12"
               tanggal = tahun+"-"+bln+"-"+tanggal+" "+"10:00:00"
               procFile['published_at']=tanggal
            procFile['published_at']=x.text
         if(x.tag=="tanggalFetch"):
            tanggal = x.text
            arrT = tanggal.split(" ")
            arrD = arrT[0].split("/")
            tanggal = arrD[2]+"-"+arrD[1]+"-"+arrD[0]+" "+arrT[1]
            tanggal = tanggal.replace("/","-")
            procFile['fetched_at']=tanggal
         if(x.tag=="url"):
            procFile['url']=x.text
            rawFile['url']=x.text
         if(x.tag=="body"):
            body = '<html>'+x.text+"</html>"
            body.replace("&lt;","<")
            body.replace("&gt;",">")
            body.replace("&nbsp;"," ")
            body.replace("&quot;","\"")
            body.replace("&amp;","&")
            rawFile['html']=body      
      hasil={}
      hasil['title']=procFile['title']
      hasil['content']=procFile['content']
      hasil['published_at']=procFile['published_at']
      hasil['fetched_at']=procFile['fetched_at']
      hasil['url']=procFile['url']
      hasil['topic']="Flora dan Fauna"
      semuaRaw.append(rawFile)
      semuaProc.append(hasil)
      ctr+=1

def writeToFile(raw, proc):
   teks = open("processed.json","w")
   json.dump(proc,teks)
   teks.close()
   teks = open("raw.json","w")
   json.dump(raw,teks)
   teks.close()

writeToFile(semuaRaw, semuaProc)
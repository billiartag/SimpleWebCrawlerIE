from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime
import xml.etree.ElementTree as ET
from xml.dom import minidom


list_link=[]
link_halaman_next = ""
keyword=["flora+fauna","binatang","hewan","tanaman","tumbuhan"]
url = ["https://www.faunadanflora.com/","https://klorofa.com/","https://www.mongabay.co.id/category/flora-fauna/","https://www.fauna.id/hewan-peliharaan/kucing/","https://www.fauna.id/serangga/","https://www.fauna.id/ikan/","https://hijaukan.com/","https://hewanpedia.com/category/edukasi/ilmiah/","https://www.trubus-online.co.id/","https://www.mongabay.co.id/tag/hutan/","https://www.greeners.co/flora-fauna/","https://infobinatang.com/blog/page/2/","https://hijauku.com/category/lingkungan/tumbuhan/page/1"]

iterasi = 0

def writeToFile(arr):
   print(arr)
   teks = open("link.txt","r")
   if(teks.read(1)):#ada isi
      teks = open("link.txt","a")
      for i in arr:
         teks.write(i+"\n")
      #append
   else:#kosong
      #write
      teks = open("link.txt","w")
      for i in arr:
         teks.write(i+"\n")
   teks.close()
def faunadanflora():
   arr= []
   driver.find_element_by_class_name("listrecent")#dikotaknya
   list_a = driver.find_elements_by_class_name("card-title")
   for r in list_a:
      ll = r.find_element_by_tag_name("a")
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanFF():
   lanjut = driver.find_element_by_xpath("//a[@title='next']")
   try:
      lanjut.click()
      return True
   except: 
      return False   
def klorofa():
   arr= []
   judul = driver.find_elements_by_tag_name("h2")
   for r in judul:
      ll = r.find_element_by_tag_name("a")
      print(ll.get_attribute("href"))
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanKloroflora():
   try:
      lanjut = driver.find_element_by_xpath("//li[@class='nav-previous']").find_element_by_tag_name("a")
      lanjut.click()
      return True
   except: 
      return False
def mongabay():
   arr= []
   judul = driver.find_elements_by_xpath("//h2[@class='post-title-news']")
   for r in judul:
      ll = r.find_element_by_tag_name("a")
      print(ll.get_attribute("href"))
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanmongabay():
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='next page-numbers']")
      lanjut.click()
      return True
   except:
      return False
def faunaID():
   arr= []
   judul = driver.find_elements_by_xpath("//h2[@class='entry-title']")
   for r in judul:
      ll = r.find_element_by_tag_name("a")
      print(ll.get_attribute("href"))
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanFaunaID():
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='next page-numbers']")
      lanjut.click()
      return True
   except:
      return False
def hijaukan():
   arr= []
   judul = driver.find_elements_by_xpath("//h2[@class='entry-title']")
   for r in judul:
      ll = r.find_element_by_tag_name("a")
      print(ll.get_attribute("href"))
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanHijaukan():
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='next page-numbers']")
      lanjut.click()
      return True
   except:
      return False
def hewanpedia(pageNumber):
   print('paginated_page paginated_page_'+str(pageNumber)+' active')
   arr= []

   page = driver.find_element_by_xpath("//div[@class='paginated_page paginated_page_"+str(pageNumber)+" active']")
   besar = page.find_elements_by_xpath("//div[@class='column size-1of3']")
   for r in besar:
      art = r.find_elements_by_xpath("//div[@class='header']")
      for n in art:
         ll = n.find_element_by_tag_name("a")
         # print(ll.get_attribute("href"))
         arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanHewanpedia():
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='next arrow']")
      lanjut.click()
      return True
   except:
      return False
def trubus():
   arr= []
   judul = driver.find_elements_by_xpath("//h2[@class='post-title']")
   for r in judul:
      ll = r.find_element_by_tag_name("a")
      print(ll.get_attribute("href"))
      arr.append(ll.get_attribute("href"))
   return arr
def pindahHalamanTrubus():
   try:
      lanjut = driver.find_element_by_xpath("//div[@class='navigation clearfix']")
      link = lanjut.find_elements_by_tag_name("a")
      for i in link:
         if(i.text=="Next Page »"):
            print(i.text)   
            i.click()
            break
      return True
   except:
      return False
def closeBoxTrubus():
   try:
      silang = driver.find_element_by_xpath("//a[@title='Close']")
      print(silang)
      if(silang!=""):
         silang.click()
   except:
      print("ok")
def greeners():
   arr=[]
   container = driver.find_element_by_xpath("//div[@class='left-content']")
   article = container.find_elements_by_tag_name("article")
   for i in article:
      link = i.find_element_by_tag_name("a")
      href = link.get_attribute("href")
      ada = False
      for x in arr:
         # print(x+"~"+href)
         if(x==href):
            ada=True
      # print("\n")
      if(ada == False):
         print(href)
         arr.append(href)
   return arr
def pindahHalamanGreeners():   
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='nextpostslink']")
      lanjut.click()
      return True
   except:
      return False
def infobinatang():
   arr=[]
   article = driver.find_elements_by_xpath("//div[@class='post-thumbnail']")
   for i in article:
      link = i.find_element_by_tag_name("a")
      href = link.get_attribute("href")
      print(href)
      arr.append(href)
   return arr
def pindahHalamanInfoBinatang():
   try:
      lanjut = driver.find_element_by_xpath("//a[@class='next page-numbers']")
      lanjut.click()
      return True
   except:
      return False
def hijauku():
   arr=[]
   article = driver.find_elements_by_xpath("//h2[@class='entry-title fusion-post-title']")
   for i in article:
      link = i.find_element_by_tag_name("a")
      href = link.get_attribute("href")
      print(href)
      arr.append(href)
   return arr
def pindahHalamanHijauku(pageNumber):
   driver.get("https://hijauku.com/category/lingkungan/page/"+str(pageNumber))
   time.sleep(3)
   try:
      lanjut = driver.find_elements_by_xpath("//h2[@class='entry-title fusion-post-title']")
      return True
   except:
      return False


def writeCrawl(hasil):
   xml = ET.Element("data")
   tanggal = ET.SubElement(xml,"tanggalPost")
   tanggalFetch = ET.SubElement(xml,"tanggalFetch")
   judul= ET.SubElement(xml,"judul")
   author= ET.SubElement(xml,"author")
   isi = ET.SubElement(xml,"isi")
   
   tanggal.text = hasil.tanggal
   tanggalFetch.text = hasil.fetchTime
   judul.text = hasil.judul
   author.text = hasil.author
   isi.text = hasil.isi

   ET.ElementTree(xml).write("hasil/"+hasil.filename+".xml", encoding="utf-8",xml_declaration=True)

class hasil:
   def __init__(self, filename, judul, isi, author, tanggal):
      self.filename=filename
      self.judul = judul
      self.isi = isi
      self.author = author
      self.tanggal = tanggal
      self.fetchTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
   def buatFile(self):
      writeCrawl(self)
   def print(self):
      print(self.judul+"-"+self.author+"-"+self.tanggal+"-"+self.filename)

def ubahNilai(nilai):
   file = open("config.txt","w")
   file.write(str(nilai))
   file.close()


driver = webdriver.Chrome('chromedriver.exe') 

mode = 1
index=12
if(mode==0):
   driver.maximize_window()
   while(index!=url.count):
      driver.get(url[index])
      driver.implicitly_wait(2)
      if(index==0):
         #faunadanflora
         arr = faunadanflora()
         while(arr!=""):
            arr = faunadanflora()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanFF()
               if not(pindah):
                  break
            else: 
               break
      elif(index==1):
         arr= klorofa()
         #KloroFlora
         while(arr!=""):
            arr= klorofa()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanKloroflora()
               if not(pindah):
                  break
            else: 
               break
      elif(index==2 or index==9):
         arr= mongabay()
         #Mongabay
         while(arr!=""):
            arr= mongabay()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanmongabay()
               if not(pindah):
                  break
            else: 
               break
      elif(index==4 or index==5 or index==3):
         arr= faunaID()
         #Fauna ID kucing Serangga ikan
         while(arr!=""):
            arr= faunaID()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanFaunaID()
               if not(pindah):
                  break
            else: 
               break
      elif(index==6):
         arr= hijaukan()
         #Hijaukan
         while(arr!=""):
            arr= hijaukan()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanHijaukan()
               if not(pindah):
                  break
            else: 
               break
      elif(index==7):
         pageNumber=1
         arr= hewanpedia(pageNumber)
         #Hewanpedia
         while(arr!=""):
            time.sleep(1)
            arr= hewanpedia(pageNumber)
            if(arr!=""):
               writeToFile(arr[-12:])
               pindah = pindahHalamanHewanpedia()
               time.sleep(1)
               if not(pindah):
                  break
            else: 
               break
            pageNumber+=1
      elif(index==8):
         time.sleep(5)
         closeBoxTrubus()
         arr= trubus()
         #Trubus
         while(arr!=""):
            arr= trubus()
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanTrubus()
               if not(pindah):
                  break
            else: 
               break
            time.sleep(2)
      elif(index==10):
         driver.maximize_window()
         arr= greeners()
         #greeners
         while(arr!=""):
            arr= greeners()
            print(arr)
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanGreeners()
               if not(pindah):
                  break
            else: 
               break
      elif(index==11):
         #infobinatang
         driver.maximize_window()
         arr= infobinatang()
         while(arr!=""):
            arr= infobinatang()
            print(arr)
            if(arr!=""):
               writeToFile(arr)
               pindah = pindahHalamanInfoBinatang()
               if not(pindah):
                  break
            else: 
               break     
      elif(index==12):
         #hijauku
         page = 1
         driver.maximize_window()
         arr= hijauku()
         while(arr!=""):
            arr= hijauku()
            print(arr)
            if(arr!=""):
               writeToFile(arr)
               page+=1
               pindah = pindahHalamanHijauku(page)
               if not(pindah):
                  break
            else: 
               break         
               
         time.sleep(3)
      index=index+1

elif(mode==1):
   fileLink = open("link.txt","r")
   arrLink = fileLink.read().split("\n")
   fileLink.close()
   try:
      statLink = open("config.txt","r")
      isiConfig = statLink.read()
      print(isiConfig)
      statLink.close()
   except:
      statLink= None

   startIndex=0
   if(statLink is not None and isiConfig!=""):
      startIndex = int(isiConfig)

   while(int(startIndex)<len(arrLink)):
      #get link
      link = arrLink[startIndex]
      
      arr_split = link.split("/")
      filename = arr_split[-2]
      domain = arr_split[2]
      driver.get(link)
      # print(arr_split)
      # print(arr_split[2])
      if(domain == "www.faunadanflora.com"):
         Ejudul = driver.find_element_by_xpath("//h1[@class='posttitle']")
         judul = Ejudul.text
         print(judul)
         EWaktu = driver.find_element_by_xpath("//time[@class='post-date']")
         waktu = EWaktu.text
         print(waktu)
         EIsi = driver.find_element_by_xpath("//article[@class='article-post']")
         isi = EIsi.text
         print(isi)
         author=""
      elif (domain == "klorofa.com"):
         Ejudul = driver.find_element_by_xpath("//h1[@class='title single-title entry-title']")
         judul = Ejudul.text
         Eauthor = driver.find_element_by_xpath("//a[@rel='author']")
         author = Eauthor.text
         print(author)
         EWaktu = driver.find_element_by_xpath("//span[@class='thetime date updated']")
         EWaktu = EWaktu.find_element_by_tag_name("span")
         waktu = EWaktu.text
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='thecontent']")
         isi = EIsi.text
         print(isi)
      elif (domain == "www.mongabay.co.id"):
         Ejudul = driver.find_element_by_xpath("//div[@class='article-headline']")
         Ejudul = Ejudul.find_element_by_tag_name("h1")
         judul = Ejudul.text
         Eauthor = driver.find_element_by_xpath("//div[@class='single-article-meta']")
         Eauthor = Eauthor.find_element_by_tag_name("a")
         author = Eauthor.text
         print(author)
         EWaktu = driver.find_element_by_xpath("//div[@class='single-article-meta']")
         teksWaktu = EWaktu.text
         arrWaktu = teksWaktu.split(" ")
         ambilWaktu = arrWaktu[-3:]
         print(ambilWaktu)
         waktu = ambilWaktu[0]+" "+ambilWaktu[1]+" "+ambilWaktu[2]
         print(waktu)
         EIsi = driver.find_element_by_tag_name("article")
         isi = EIsi.text
         print(isi)
      elif (domain == "www.fauna.id"):
         Ejudul = driver.find_element_by_xpath("//h1[@class='entry-title']")
         judul = Ejudul.text
         author = "-"
         print(author)
         waktu = "-"
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='entry-content']")
         isi = EIsi.text
         print(isi)
      elif (domain == "hijaukan.com"):         
         Ejudul = driver.find_element_by_xpath("//h1[@class='entry-title']")
         judul = Ejudul.text
         Eauthor = driver.find_element_by_xpath("//span[@class='author-name']")
         author = Eauthor.text
         print(author)
         EWaktu = driver.find_element_by_tag_name("time")
         waktu = EWaktu.text
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='entry-content']")
         isi = EIsi.text
         print(isi)
      elif (domain == "hewanpedia.com"):
         Ejudul = driver.find_element_by_xpath("//h1[@class='entry-title']")
         judul = Ejudul.text
         author = "-"
         print(author)
         waktu = "-"
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='post-content entry-content']")
         isi = EIsi.text
         print(isi)
         
      elif (domain == "www.trubus-online.co.id"):
         try:
            time.sleep(3)
            closeBoxTrubus()
            Ejudul = driver.find_element_by_xpath("//h1[@class='post-title single']")
            Ejudul = Ejudul.find_element_by_tag_name("a")
            judul = Ejudul.text
            Eauthor = driver.find_element_by_xpath("//span[@class='meta-author']")
            author = Eauthor.text
            print(author)
            EWaktu = driver.find_element_by_xpath("//span[@class='meta-date']")
            waktu=EWaktu.text
            print(waktu)
            EIsi = driver.find_element_by_xpath("//div[@class='entry']")
            isi = EIsi.text
            print(isi)
         except:
            print("gagal fetch")
            isi = None
      elif (domain == "www.greeners.co"):
         Ejudul = driver.find_element_by_xpath("//h1[@class='entry-title']")
         judul = Ejudul.text
         Eauthor = driver.find_element_by_xpath("//div[@class='entry-content']")
         Ep = Eauthor.find_elements_by_tag_name("p")
         parPenulis = Ep[-1]
         # for i in parPenulis:
         #    txt = i.text
         #    print(txt)
         isiAuthor = parPenulis.text
         arrAuthor = isiAuthor.split(" ")
         arrAuthor = arrAuthor[1:]
         author = ""
         for i in arrAuthor:
            author+=i+" "
         print("auth:"+author)
         EWaktu = driver.find_element_by_xpath("//div[@class='post-time']")
         EWaktu = EWaktu.find_element_by_tag_name("time")
         arrWaktu = (EWaktu.text).split(" ")
         waktu = ""
         for i in arrWaktu[-3:]:
            waktu+=i+" "
         print("Waktu:"+waktu)
         arrIsi = Ep[:-1]
         isi=""
         for i in arrIsi:
            isi+= i.text+"\n"
         print(isi)
      elif (domain == "infobinatang.com"):
         Ejudul = driver.find_element_by_xpath("//a[@class='post-title']")
         judul = Ejudul.text
         Eauthor = driver.find_element_by_xpath("//span[@class='post-auhor-date post-auhor-date-full']")
         tAuthor = Eauthor.text
         arrAuthor = tAuthor.split(",")
         author = arrAuthor[0]
         print(author)
         waktu = arrAuthor[-1]
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='post-content post-single-content']")
         isi = EIsi.text
         print(isi)
      elif(domain=="hijauku.com"):         
         Ejudul = driver.find_element_by_xpath("//h1[@class='entry-title fusion-post-title']")
         judul = Ejudul.text
         author = "-"
         print(author)
         EWaktu = driver.find_element_by_xpath("//div[@class='fusion-meta-info-wrapper']")
         teksWaktu = EWaktu.text
         arrWaktu = teksWaktu.split(" ")
         arrW = arrWaktu[:2]
         waktu = ""
         for i in arrW:
            waktu+=i+" "
         print(waktu)
         EIsi = driver.find_element_by_xpath("//div[@class='post-content']")
         isi = EIsi.text
         print(isi)
      if(isi is not None):
         temp = hasil(filename, judul, isi,author,waktu)
         temp.buatFile()
         temp.print()
      # break
      #ubah nilai config
      startIndex+=1
      ubahNilai(int(startIndex))

driver.quit()




# driver.get('https://www.google.com/search?q='+keyword[0])

# driver.implicitly_wait(10)

# driver.find_element_by_xpath('//*[contains(text(),"Berita")]').click()
# url = driver.current_url
# newurl = url+"&cr=countryID"
# driver.get(newurl)
# while  index< len(keyword):
#    if(index!=0):
#          #ganti di querybox nya
#    #loop sampe mentas
#    while(iterasi<=max_page):
#       arr_berita = getLinksGgl()
#       if(len(arr_berita)==0):
#          iterasi=max_page+1
#          break
#       list_link.append(arr_berita)
#       iterasi+=1
#       # get pos start
#       link = driver.current_url
#       pos_start = driver.current_url.find("&start=")
#       pos_end = driver.current_url.find("&",pos_start)
#       if(iterasi==1):
#          link_baru= link+"&start=10&"
#       else:
#          halaman = str(iterasi*10) 
#          ganti ="start=%s&"%halaman
#          link_baru = link[:pos_start+1]+ganti#+link[pos_end+1:]
#       print(link_baru)
#       link_halaman_next = link_baru

#       pindahHalaman()
#       driver.implicitly_wait(5)
# simpenFile(list_link)

# driver.quit()


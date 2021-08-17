## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page
# web_address = 'https://polisci.wustl.edu/people/88/all'


from bs4 import BeautifulSoup
import urllib.request
import csv 
import os, time, random

os.chdir("/Users/ysui/Documents/GitHub/python_summer2021/Day4/Lab")

with open("washu_faculty.csv", "w") as f:
    # 
    w = csv.DictWriter(f, fieldnames= ("Name", "Title", "E-mail", "Webpage", "Specialization") )
    w.writeheader()
    web_address = 'https://polisci.wustl.edu/people/88/all'
    web_page = urllib.request.urlopen(web_address)
    soup = BeautifulSoup(web_page.read(), features="lxml") 
    s = soup.find_all("a", class_="card")
    faculty = {} # dict
    for i in s:
        faculty["Name"] = i.h3.text
        faculty["Title"] = i.find(class_ = "dept").text
        if i["href"][0] == '/':
            webpage = "https://polisci.wustl.edu" + i["href"]
        else: 
            webpage = i["href"]
        new_page = urllib.request.urlopen(webpage)
        new_soup = BeautifulSoup(new_page.read(), features = "lxml")
        try: 
            faculty["E-mail"] = new_soup.find(class_ = "detail contact").find("a").text
        except: 
            faculty["E-mail"] = "N/A"
        try: 
            faculty["Webpage"] = new_soup.find(class_ = "links").find("a")["href"]
        except:
            faculty["Webpage"] = "N/A"
        try: 
            faculty["Specialization"] = new_soup.find(class_ = "post-excerpt").text
        except: 
            faculty["Specialization"] =  "N/A"
        w.writerow(faculty)
        time.sleep(random.uniform(1, 5))





"""
<div class="container filtered-cards faculty-cards flex js-load-container"><a href="/people/deniz-aksoy" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Deniz Aksoy" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Aksoy_D_P1044482.jpg?itok=w_EDKFzN"><h3><div><span>Deniz</span>&nbsp;</div><div><span>Aksoy</span></div></h3></div><div class="dept">Associate Professor of Political Science</div></article></a><a href="/people/michael-m-bechtel" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Michael M. Bechtel" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Bechtel_M_IMG_0920.jpg?itok=AdDbF-xX"><h3><div><span>Michael M.</span>&nbsp;</div><div><span>Bechtel</span></div></h3></div><div class="dept">Associate Professor of Political Science<div class="addtitles">Director of Environmental Policy
Swiss Institute for International Economics and Applied Economic Research Fellow</div></div></article></a><a href="/people/daniel-butler" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Daniel  Butler" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/dmbutler19.jpg?itok=jCyJREOF"><h3><div><span>Daniel </span>&nbsp;</div><div><span>Butler</span></div></h3></div><div class="dept">Associate Professor of Political Science</div></article></a><a href="/people/randall-calvert" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Randall Calvert" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Calvert_R_IMG_0960.jpg?itok=RvL37jkA"><h3><div><span>Randall</span>&nbsp;</div><div><span>Calvert</span></div></h3></div><div class="dept">Thomas F. Eagleton University Professor of Public Affairs and Political Science</div></article></a><a href="/people/taylor-carlson" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Taylor Carlson" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/PoliSci_Carlson_T_P1322772.jpg?itok=sZD5AZpt"><h3><div><span>Taylor</span>&nbsp;</div><div><span>Carlson</span></div></h3></div><div class="dept">Assistant Professor of Political Science</div></article></a><a href="/people/david-carter" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of David Carter" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Carter_D_P1044474.jpg?itok=s0k5djSC"><h3><div><span>David</span>&nbsp;</div><div><span>Carter</span></div></h3></div><div class="dept">Associate Professor of Political Science<div class="addtitles">Director of Graduate Studies in Political Science</div></div></article></a><a href="/people/dino-christenson" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Dino  Christenson" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/thumbnail_18-1858-DINO-024.jpg?itok=1cpFo7Pk"><h3><div><span>Dino </span>&nbsp;</div><div><span>Christenson</span></div></h3></div><div class="dept">Associate Professor of Political Science</div></article></a><a href="/people/brian-crisp" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Brian Crisp" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/PoliticalScience_Crisp_B-1277761.jpg?itok=IRltJ2oo"><h3><div><span>Brian</span>&nbsp;</div><div><span>Crisp</span></div></h3></div><div class="dept">Professor of Political Science</div></article></a><a href="/people/ted-enamorado" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Ted Enamorado" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/enamorado-2019.jpg?itok=GOiqXjVX"><h3><div><span>Ted</span>&nbsp;</div><div><span>Enamorado</span></div></h3></div><div class="dept">Assistant Professor of Political Science</div></article></a><a href="http://epstein.wustl.edu/" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Lee Epstein" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Epstein-Lee-760x760.jpg?itok=MXU8PBMZ"><h3><div><span>Lee</span>&nbsp;</div><div><span>Epstein</span></div></h3></div><div class="dept">Ethan A.H. Shepley Distinguished University Professor, Professor of Political Science</div></article></a><a href="/people/justin-fox" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Justin Fox" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Fox_J_IMG_0968.jpg?itok=2Jsf8ntZ"><h3><div><span>Justin</span>&nbsp;</div><div><span>Fox</span></div></h3></div><div class="dept">Associate Professor of Political Science</div></article></a><a href="/people/matthew-gabel" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Matthew Gabel" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Gabel_M_IMG_0944.jpg?itok=As1876fj"><h3><div><span>Matthew</span>&nbsp;</div><div><span>Gabel</span></div></h3></div><div class="dept">Professor of Political Science<div class="addtitles">Charles F. and Joanne Knight Alzheimer's Disease Research Center Faculty</div></div></article></a><a href="/people/james-l-gibson" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of James L. Gibson" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Screen-Shot-2020-02-19-at-9.42.09-AM-768x760.png?itok=C5btvqRY"><h3><div><span>James L.</span>&nbsp;</div><div><span>Gibson</span></div></h3></div><div class="dept">Sidney W. Souers Professor of Government</div></article></a><a href="/people/clarissa-rile-hayward" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Clarissa Rile Hayward" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/headshot%202017.jpg?itok=iW18kDKP"><h3><div><span>Clarissa Rile</span>&nbsp;</div><div><span>Hayward</span></div></h3></div><div class="dept">Dean’s Fellow for Policies<div class="addtitles">Professor of Political Science, Philosophy (By Courtesy), and Urban Studies (Affiliate)</div></div></article></a><a href="/people/frank-lovett" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Frank Lovett" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Polisci_Lovett_F_P1344020.jpg?itok=J7uHFATQ"><h3><div><span>Frank</span>&nbsp;</div><div><span>Lovett</span></div></h3></div><div class="dept">Professor of Political Science<div class="addtitles">Professor of Philosophy, by courtesy 
Director of Undergraduate Studies in Political Science
Director of Legal Studies</div></div></article></a><a href="/people/christopher-lucas" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Christopher Lucas" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Christopher-Lucas.jpg?itok=PIYPsMhO"><h3><div><span>Christopher</span>&nbsp;</div><div><span>Lucas</span></div></h3></div><div class="dept">Assistant Professor of Political Science</div></article></a><a href="/people/andrew-martin" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Andrew Martin" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/180713_jwb_andrew_martin_001-1-rdqqu6.jpg?itok=JpVsZTGe"><h3><div><span>Andrew</span>&nbsp;</div><div><span>Martin</span></div></h3></div><div class="dept">Chancellor<div class="addtitles">Professor of Political Science and Law</div></div></article></a><a href="/people/jacob-montgomery" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Jacob Montgomery" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Polisci__Montgomery_J_P1333918.jpg?itok=53_h_S_B"><h3><div><span>Jacob</span>&nbsp;</div><div><span>Montgomery</span></div></h3></div><div class="dept">Associate Professor of Political Science<div class="addtitles">Chair of the Political Science track for Division of Computational and Data Sciences
Director of the Weidenbaum Center's The American Social Survey (TASS)</div></div></article></a><a href="/people/lucia-motolinia" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Lucia Motolinia" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Lucia.jpg?itok=Ux-MVoYt"><h3><div><span>Lucia</span>&nbsp;</div><div><span>Motolinia</span></div></h3></div><div class="dept">Assistant Professor of Political Science<div class="addtitles">In January 2022, Lucia will be joining the Department of Political Science.</div></div></article></a><a href="/people/william-nomikos" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of William Nomikos" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/nomikos_new.jpeg?itok=A3hNMUig"><h3><div><span>William</span>&nbsp;</div><div><span>Nomikos</span></div></h3></div><div class="dept">Assistant Professor of Political Science</div></article></a><a href="/people/michael-olson" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Michael Olson" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Olson_0.jpg?itok=pANMN_GS"><h3><div><span>Michael</span>&nbsp;</div><div><span>Olson</span></div></h3></div><div class="dept">Assistant Professor of Political Science</div></article></a><a href="/people/sunita-parikh" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Sunita Parikh" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/Polisci_Parikh_S_P1344026.jpg?itok=exwu21Hz"><h3><div><span>Sunita</span>&nbsp;</div><div><span>Parikh</span></div></h3></div><div class="dept">Associate Professor of Political Science</div></article></a><a href="/people/andrew-reeves" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Andrew Reeves" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/PoliSci_Reeves_A.jpg?itok=LE1dzaTI"><h3><div><span>Andrew</span>&nbsp;</div><div><span>Reeves</span></div></h3></div><div class="dept">Professor of Political Science<div class="addtitles">Associate Chair in Political Science
Research Fellow at the Weidenbaum Center on the Economy, Government, and Public Policy</div></div></article></a><a href="/people/guillermo-rosas" class="card"><article class="faculty-post"><div class="image"><img alt="Headshot of Guillermo Rosas" src="https://polisci.wustl.edu/files/polisci/styles/testimonial_desktop/public/People/Polisci_Rosas_G_IMG_0953.jpg?itok=UhYFPcBJ"><h3><div><span>Guillermo</span>&nbsp;</div><div><span>Rosas</span></div></h3></div><div class="dept">Professor of Political Science<div class="addtitles">Associate Director of the Weidenbaum Center on the Economy, Government, and Public Policy</div></div></article></a><div class="load-more flex"><a title="Load more" class="js-load-more" href="/people/88/all?page=1">Load more</a></div></div>
"""



"""
with open('iceland_test.csv', 'w') as f: # set up with the writer
  w = csv.DictWriter(f, fieldnames = ("name", "party", "phone")) # define column names
  w.writeheader() # write the header
  web_address='https://www.althingi.is/altext/cv/en/' # the web address
  web_page = urllib.request.urlopen(web_address) # open the web page
  soup = BeautifulSoup(web_page.read()) # soup the web page
  all_members = soup.find_all('tr') # find the list of names and parties
  for i in range(1,3): # for members 1 and 2 (member 0 is just the table heading)
    try:
      member = {} ## empty dictionary to fill in
      member_i = all_members[i].find_all('td') # subset lower to each individual item
      member["name"] = member_i[0].text # member's name
      member['party'] =  member_i[1].text # member's party
      inner_page_url = web_address + member_i[0].a['href'] # get the extension to their personal page
      inner_page = urllib.request.urlopen(inner_page_url) # open the personal page
      inner_soup = BeautifulSoup(inner_page.read()) # soup the personal page
      member['phone'] = inner_soup.find('a', {'class' : 'tel'}).text # get phone number
    except:
      member['name'] = 'NA'
      member['party'] = 'NA'
      member['phone'] = 'NA'
    w.writerow(member) # write the row for this specific member
    time.sleep(random.uniform(1, 5)) # be polite, sleep!
"""
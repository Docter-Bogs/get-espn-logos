import os
import urllib

# Put the names of the text files containing the team IDs here.
# For example, if the data is in text files named "ncaa_fbs.txt" and "ncaa_d1nonfbs.txt", then the line
#
#     leagues = ["ncaa_fbs","ncaa_nonfbs"]
#
# would grab the logos from both text files.
#
leagues = ["ncaa_fbs","ncaa_nonfbs"]

# Size of the logos in pixels
size = 500

# Directory where the logos will be saved
directory = "D:\Pictures\Sports Logos\get_espn_logos"

baseurl = "http://a.espncdn.com/combiner/i?img=/i/teamlogos/"

for league in leagues:
    
    if "ncaa" in league:
        type = "ncaa"
    else:
        type = league
    
    reader = open(league+".txt",'r')
    lines = reader.readlines()
    
    for line in lines:
        teamdata = line.split(' - ')
        abbrev = teamdata[0]
        teamname = teamdata[1].strip('\n')
    
        img = baseurl+type+"/500/"+abbrev+".png?w="+str(size)+"&h="+str(size)+"&transparent=true"
        dir = directory+"\\"+teamname+".png"
        urllib.urlretrieve(img,dir)
        print teamname
        
    reader.close

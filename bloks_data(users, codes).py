'''
Created on 30-Jan-2019

@author: SureshBabu
'''

from bs4 import BeautifulSoup as soup
from getMyURLContent import getMyURLContent;
import code


def main():
    pageLink = "https://bloks.io/account/eosknightsio";
    folderPath = "C:\\My_Folder\\Eclipse_Neon\\Workspace\\bloks_data\\src\\";
    
    htmlData = getMyURLContent(pageLink, "ui selectable very basic stackable table");
    htmlContent = soup(htmlData, "html.parser");
    f = open("blocks.csv","w");
    #CSV header to file
    f.write("Names,code\r\n");
    
    name = '';code = "";
    #First look for the table tag with attribute <table class="ui selectable very basic stackable table">
    for outerTag in htmlContent.findAll("table", {"class" : "ui selectable very basic stackable table"}):
        #Under table, look for a td which has class attribute = special-td-3
        for personTags in outerTag.findChildren("td", {"class" : "special-td-3"}):
            name = ''; code = "";
            #Under the <td> there is an anchor tag in which the name is specified -> Look for child a tags
            for nameTags in personTags.findChild("a"):
                #Once the <a> tag is parsed, get the string value within that tag
                name = str(nameTags.string).strip();
                #f.write(str(nameTags.string).strip() + ",");
            
            #Code to scrape ID
            #For the same <td>, we have other values like code, checksum etc specified within div tag. so get all div tags
            for idTags in personTags.findChildren("div"):
                #Find all <b> child tags
                for bTags in idTags.findChildren("b"):
                    #Check if the <b> tag has value code: The code value is specied in next coming div tag                   
                    if "code:" in bTags.string:
                        #Find the child div tag with the given attributes
                        for span in idTags.findChildren("div", {"style": "display: inline-block;"}):
                            code = str(span.string).strip()
                            f.write(name + "," + code + "\r\n");
                            #Scraped the span value for code
                            #print("code Value: " + span.string.strip());
                            
    
    f.close();
    
    
    

if __name__ == '__main__':
    main();
    
    
    
    
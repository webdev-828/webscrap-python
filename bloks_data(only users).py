'''
Created on 30-Jan-2019

@author: SureshBabu
'''

from bs4 import BeautifulSoup as soup
from getMyURLContent import getMyURLContent;


def main():
    pageLink = "https://bloks.io/account/eosknightsio";
    folderPath = "C:\\My_Folder\\Eclipse_Neon\\Workspace\\bloks_data\\src\\";
    
    htmlData = getMyURLContent(pageLink, "ui selectable very basic stackable table");
    htmlContent = soup(htmlData, "html.parser");
    f = open("blocks.csv","w");
    f.write("Names\r\n");
    
    for outerTag in htmlContent.findAll("table", {"class" : "ui selectable very basic stackable table"}):
        for personTags in outerTag.findChildren("td", {"class" : "special-td-3"}):
            #print(personTags);
            for nameTags in personTags.findChild("a"):
                print(nameTags.string);
                f.write(str(nameTags.string).strip() + "\r\n");
            for idTags in personTags.findChild("div"):
                for bTags in idTags.findChild("b"):
                    print(bTags);
    f.close();
    
    
    

if __name__ == '__main__':
    main();
    
    
    
    
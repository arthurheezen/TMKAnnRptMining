import urllib.request
import shutil

def download_as(url, file_name):
    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)

download_as('http://www.torchmarkcorp.com/Resources/reports/1998/1998tmkannualreport.pdf', 'Reports\\AR1998.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/1999/1999tmkannual.pdf', 'Reports\\AR1999.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/2000/2000tmkannualreport.pdf', 'Reports\\AR2000.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/2001/Narrative.pdf', 'Reports\\AR2001.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/2002/2002Narrative.pdf', 'Reports\\AR2002.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/2003/2003Narrative.pdf', 'Reports\\AR2003.pdf')
download_as('http://www.torchmarkcorp.com/Resources/reports/2004/2004%20Narrative_FINAL.pdf', 'Reports\\AR2004.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2005%20Annual%20Report.pdf', 'Reports\\AR2005.pdf')
download_as('http://www.torchmarkcorp.com/Resources/59162_056_Torch_PrintReady.pdf', 'Reports\\AR2006.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2007%20Annual%20Report%20and%2010K.pdf', 'Reports\\AR2007.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2008%20Annual%20Report%20and%2010-K.pdf', 'Reports\\AR2008.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2009%20Annual%20Report%20and%2010-K.pdf', 'Reports\\AR2009.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2010%20Annual%20Report.pdf', 'Reports\\AR2010.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2011%20Annual%20Report_Torch_BMK.pdf', 'Reports\\AR2011.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2012%20Torchmark%20Annual%20Report.pdf', 'Reports\\AR2012.pdf')
download_as('http://www.torchmarkcorp.com/Resources/2013%20Torchmark%20Annual%20Report.pdf', 'Reports\\AR2013.pdf')
download_as('https://www.torchmarkcorp.com/Resources/2014%20Torchmark%20Annual%20Report.pdf', 'Reports\\AR2014.pdf')
download_as('https://www.torchmarkcorp.com/Resources/Annual%20Rpt%20Shdrs%202015%20website%2070393_002_web_bmk1.pdf', 'Reports\\AR2015.pdf')


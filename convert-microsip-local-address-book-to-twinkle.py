from xml.dom import minidom
import csv

# you should will be configure this parameters before run the script
srcFile = '/tmp/Contacts.xml'
outFile = '/tmp/adresBok_Test.csv'
domainOfContact = '@sip.somepublicsipserver.pl'

def main():
	file = minidom.parse(srcFile)
	contact = file.getElementsByTagName('contact')
	with open(outFile, mode='w', newline='', encoding="utf-8") as adressBook:
		adresBookWriter = csv.writer(adressBook, delimiter='|',  lineterminator='\n', quotechar='"', quoting=csv.QUOTE_NONE, escapechar='\\')
		for entry in contact:
			lista = [entry.attributes['name'].value, "", "",  entry.attributes['number'].value + domainOfContact, ""]
			adresBookWriter.writerow(lista)

if __name__ == "__main__":
	main()
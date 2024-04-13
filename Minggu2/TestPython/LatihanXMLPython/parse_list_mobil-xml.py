import xml.dom.minidom as minidom

def main():
    
    doc = minidom.parse(r'C:\Users\Masahiro benz\Kuliah\S4\PMesin\Minggu2\LatihanXMLPython\list_mobil.xml')

    print(doc.nodeName)
    print("Experiment XML Python")
    print("List mobil supercar")

    no = doc.getElementsByTagName("no")[0].firstChild.data
    merek = doc.getElementsByTagName("merek")[0].firstChild.data
    model = doc.getElementsByTagName("model")[0].firstChild.data
    tahun = doc.getElementsByTagName("tahun")[0].firstChild.data
    mesin = doc.getElementsByTagName("mesin")[0].firstChild.data
    
    print ("\nNo: {}\nMerek: {}\nModel: {}\nTahun: {}\nMesin: {}\n".format(no, merek, model, tahun, mesin))

    no = doc.getElementsByTagName("no")[1].firstChild.data
    merek = doc.getElementsByTagName("merek")[1].firstChild.data
    model = doc.getElementsByTagName("model")[1].firstChild.data
    tahun = doc.getElementsByTagName("tahun")[1].firstChild.data
    mesin = doc.getElementsByTagName("mesin")[1].firstChild.data
    
    print ("No: {}\nMerek: {}\nModel: {}\nTahun: {}\nMesin: {}\n".format(no, merek, model, tahun, mesin))

    no = doc.getElementsByTagName("no")[2].firstChild.data
    merek = doc.getElementsByTagName("merek")[2].firstChild.data
    model = doc.getElementsByTagName("model")[2].firstChild.data
    tahun = doc.getElementsByTagName("tahun")[2].firstChild.data
    mesin = doc.getElementsByTagName("mesin")[2].firstChild.data
    
    print ("No: {}\nMerek: {}\nModel: {}\nTahun: {}\nMesin: {}\n".format(no, merek, model, tahun, mesin))

    no = doc.getElementsByTagName("no")[3].firstChild.data
    merek = doc.getElementsByTagName("merek")[3].firstChild.data
    model = doc.getElementsByTagName("model")[3].firstChild.data
    tahun = doc.getElementsByTagName("tahun")[3].firstChild.data
    mesin = doc.getElementsByTagName("mesin")[3].firstChild.data
    
    print ("No: {}\nMerek: {}\nModel: {}\nTahun: {}\nMesin: {}\n".format(no, merek, model, tahun, mesin))

    no = doc.getElementsByTagName("no")[4].firstChild.data
    merek = doc.getElementsByTagName("merek")[4].firstChild.data
    model = doc.getElementsByTagName("model")[4].firstChild.data
    tahun = doc.getElementsByTagName("tahun")[4].firstChild.data
    mesin = doc.getElementsByTagName("mesin")[4].firstChild.data

    print ("No: {}\nMerek: {}\nModel: {}\nTahun: {}\nMesin: {}".format(no, merek, model, tahun, mesin))

if __name__ == "__main__":
    main()

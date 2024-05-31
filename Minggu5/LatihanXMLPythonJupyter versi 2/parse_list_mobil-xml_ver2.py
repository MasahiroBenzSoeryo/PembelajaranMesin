import xml.dom.minidom as minidom

def main():
    
    doc = minidom.parse(r'C:\Users\Masahiro benz\Kuliah\S4\PMesin\Minggu4\LatihanXMLPythonJupyter versi 2\list_mobil.xml')

    print(doc.nodeName)
    print("Experiment XML Python")
    print("List mobil supercar, hypercar, dan luxury car")

    mobil_list = doc.getElementsByTagName("mobil")

    for i, mobil in enumerate(mobil_list):
        no = mobil.getElementsByTagName("no")[0].firstChild.data
        merek = mobil.getElementsByTagName("merek")[0].firstChild.data
        model = mobil.getElementsByTagName("model")[0].firstChild.data
        tahun = mobil.getElementsByTagName("tahun")[0].firstChild.data
        mesin = mobil.getElementsByTagName("mesin")[0].firstChild.data

        print(f"\nNo: {no}")
        print(f"Merek: {merek}")
        print(f"Model: {model}")
        print(f"Tahun: {tahun}")
        print(f"Mesin: {mesin}")

if __name__ == "__main__":
    main()

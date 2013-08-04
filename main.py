import MURequirement
import MUTest
from RequirementParser import *
# python script to read an excel file with requirements



def playWithRequirements():
    test1 = Test("test1", "desc1")
    test2 = Test("test2", "desc2")

    req1 = Requirement("req1", "desc1", 222, [test1, test2])
    req1.printRequirement()




if __name__ == "__main__":

    print "Hello Python"
    fileNameXls = "/mnt/hgfs/My_Shared_VM_Folder/Requirements.xlsx"
    parser = RequirementParser(fileNameXls)
    #parser.printWorkSheet2()
    parser.parseRequirements()
    parser.printAllRequirements()
    
    #playWithRequirements()

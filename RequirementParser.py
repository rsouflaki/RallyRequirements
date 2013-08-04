import xlrd
from MURequirement import *
from MUTest import *

class RequirementParser:
    """Parses an xsl file anAcceptance Test IDAcceptance Test IDd generates a list of requirements"""

    ColumnsDict = {
            'ID': 0, 
            'Acceptance Test ID': 1, 
            'Description': 2, 
            'Date Added': 3, 
            'Naxos Story': 4
    }

    def __init__(self, fileName):
        self.currentRow = 0
        self.reqs = {}
        wb = xlrd.open_workbook(fileName)

        #Check the sheet names
        wb.sheet_names()

        #Get the first sheet either by index or by name
        self.worksheet = wb.sheet_by_index(0)
        #sh = wb.sheet_by_name(u'Sheet1')
        
    
    def printWorkSheet(self):
        #Iterate through rows, returning each as a list that you can index:
        for rownum in range(self.worksheet.nrows):
            print self.worksheet.row_values(rownum)

    def printWorkSheet2(self):
        for rownum in range(self.worksheet.nrows):
            row = self.worksheet.row(rownum)
            print 'Parsing Row:', rownum
            for colnum in range(self.worksheet.ncols):
                # Cell Types: 0=Empty, 1=Text, 2=Number, 3=Date, 4=Boolean, 5=Error, 6=Blank
                cell_type = self.worksheet.cell_type(rownum, colnum)
                cell_value = self.worksheet.cell_value(rownum, colnum)
                print ' ', cell_type, ':', cell_value

    def validateHeader(self, headerStr):
        #TODO: check that the header is as expected
        print headerStr


    def getRequirementIdColumnNumber(self):
        return self.ColumnsDict['ID']
    def getDescriptionColumnNumber(self):
        return self.ColumnsDict['Description']
    def getTestIdColumnNumber(self):
        return self.ColumnsDict['Acceptance Test ID']
    def getDateColumnNumber(self):
        return self.ColumnsDict['Date Added']


    def getColumnNumber(self, identifier):
        return self.ColumnsDict[identifier]

    def getRequirementIdCell(self):
        return self.worksheet.cell_value(self.currentRow, self.getRequirementIdColumnNumber())

    def getDescriptionCell(self):
        return self.worksheet.cell_value(self.currentRow, self.getDescriptionColumnNumber())

    def getTestIdCell(self):
        return self.worksheet.cell_value(self.currentRow, self.getTestIdColumnNumber())
   
    def getDateCell(self):
        return self.worksheet.cell_value(self.currentRow, self.getDateColumnNumber())
    
    EMPTY_CELL = 0
    TEXT_CELL = 1
    NUMBER_CELL = 2
    DATE_CELL = 3
    def isRequirementRow(self):
        if (self.TEXT_CELL == self.worksheet.cell_type(self.currentRow, self.getRequirementIdColumnNumber()) 
                and self.TEXT_CELL == self.worksheet.cell_type(self.currentRow, self.getDescriptionColumnNumber()) 
                and self.DATE_CELL == self.worksheet.cell_type(self.currentRow, self.getDateColumnNumber())):
            print 'Found requirement row with ID: ' + self.getRequirementIdCell()
            return True
        return False

    def isTestRow(self):
        if (self.TEXT_CELL == self.worksheet.cell_type(self.currentRow, self.getTestIdColumnNumber()) 
                and self.TEXT_CELL == self.worksheet.cell_type(self.currentRow, self.getDescriptionColumnNumber())):
            print 'Found test row with ID: ' + self.getTestIdCell()
            return True
        return False
    
    def parseRequirements(self):
        currReqId = None
        for rownum in range(self.worksheet.nrows):
            self.currentRow = rownum
            if rownum == 0:
                self.validateHeader('need to validate headers')
                continue
            if self.isRequirementRow():
                currReqId = self.getRequirementIdCell()
                self.reqs[currReqId] = MURequirement(currReqId, self.getDescriptionCell(), self.getDateCell())
            elif self.isTestRow():
                test = MUTest(self.getTestIdCell(), self.getDescriptionCell())
                if currReqId != None:
                    print 'Tests for this requirement, up to now: ' + str(len(self.reqs[currReqId].tests))
                    self.reqs[currReqId].tests.append(test)
            else:
               print 'Unknown row found, assume new requirement'
               currReqId = None

    def printAllRequirements(self):
        for req in self.reqs.values():
            req.printRequirement()


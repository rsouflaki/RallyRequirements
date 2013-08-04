class MURequirement:
    """A MU requirement"""

    def __init__(self, id, description, dateAdded):
        self.id = id
        self.description = description
        self.dateAdded = dateAdded
        #self.tests = tests 
        self.tests = []
        self.projects = []

    def validForProject(storyId):
        self.projects.append(MUProjectData(self.id, storyId))

    def printRequirement(self):
        print "Requirement id is: " + self.id + ", Description: " + self.description + ", Date added: " + str(self.dateAdded)
        print "->Valid for " + str(len(self.projects)) + " projects:"
        for project in self.projects:
            print "  " + project.projectName + ", with User Story:" + project.storyId
        print "->with " + str(len(self.tests)) + " tests:"
        for test in self.tests:
            print "  Requirement id: " + self.id + ", Test id: " + test.id

class MUProjectData:
    """A relationship between a requirement and a project"""

    def __init___(self, reqId, projectName, storyId):
        seld.reqId = reqId
        seld.storyId = storyId
        self.projectName = projectName

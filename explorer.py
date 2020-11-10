import click
import psutil
import os

"""
Основной смысл чтобы можно было потом в пикл захреначить и использовать в качестве кэша
"""

"Priority draw parameters"
PRIORITY_DRAW_HIGH = 1
PRIORITY_DRAW_MIDDLE = 2
PRIORITY_DRAW_LOW = 3

"Decode message parameter in fileobject"
INFO_DICT_PARAMS_DECODE_RU = {
    "file": {
        "name": "Файл",
        "priorityDraw": PRIORITY_DRAW_HIGH
    }
}


class Node(object):
    """
    This is a fileobject node. Laizy
    """

    def __init__(self, path):
        self.path = path
        self.basename = self.path.split(os.sep)[-1] if len(self.path.split(os.sep)[-1]) else self.path.split(os.sep)[-2]
        self.children = {}
        self.parrent = None
        self.type = None
        self.parameters = {}

        # loadParams()

    def browse(self):
        pass

    def setParrent(self):
        pass

    def appendChild(self, node):
        """Add the children in current node"""
        self.children[node.basename] = node

    def getObjectforJsonify(self):
        return {
            "text": self.basename,
            # "children": [self.children[x].getObjectforJsonify() for x in self.children],
            "fullpath": self.path,
            "isLeaf": False # раскрывающийся список - False
        }


class TreeExplore(object):
    def __init__(self):
        self.generalNodeDict = {}
        self.loadAvaliableDisk()

    def loadAvaliableDisk(self):
        """This is a multiplatform get disk function"""
        for d in psutil.disk_partitions():
            node = Node(d.device)
            self.generalNodeDict[node.basename] = node

    def generateObjectForJsonify(self):
        return [self.generalNodeDict[key].getObjectforJsonify() for key in self.generalNodeDict]

    def getNodeByPath(self, path):
        generalNodeNameList = path.split(os.sep)
        node = self.generalNodeDict[generalNodeNameList[0]]
        for path in generalNodeNameList[1:]:
            if len(path) == 0:
                continue
            node = node.children[path]
        return node

    def click(self, fullpath):
        lastNode = self.getNodeByPath(fullpath)
        returnedInNode = []
        for p in os.listdir(fullpath):
            nextNodePath = os.path.join(fullpath, p)
            nextNode = Node(nextNodePath)
            # TODO coding it
            nextNode.parameters["fileobject_type"] = ""

            lastNode.appendChild(nextNode)
            returnedInNode.append(nextNode.getObjectforJsonify())
        return returnedInNode


if __name__ == "__main__":
    te = TreeExplore()

    print("Start..")
    print(te.generateObjectForJsonify())

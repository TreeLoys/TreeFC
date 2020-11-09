import click
import psutil
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
        self.iconPath = ""
        self.children = []
        self.parrent = None
        self.type = None
        self.infoDict = {}

        # loadParams()

    def browse(self):
        pass

    def setParrent(self):
        pass

    def appendChild(self, node):
        """Add the children in current node"""
        self.children.append(node)

    def getObjectforJsonify(self):
        return {
            "text": self.path,
            "children": [x.getObjectforJsonify() for x in self.children]
        }


class TreeExplore(object):
    def __init__(self):
        self.generalNodeList = []
        self.loadAvaliableDisk()

    def loadAvaliableDisk(self):
        """This is a multiplatform get disk function"""
        for d in psutil.disk_partitions():
            self.generalNodeList.append(Node(d.device))

    def getFileobjects(self):
        pass

    def generateObjectForJsonify(self):
        return [x.getObjectforJsonify() for x in self.generalNodeList]


if __name__ == "__main__":
    te = TreeExplore()

    print("Start..")
    print(te.generateObjectForJsonify())
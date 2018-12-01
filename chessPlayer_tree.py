class tree:
        def __init__(self,x):
                self.store = [x,[]]
                self.indent = ""

        def AddSuccessor(self,x):
                self.store[1] = self.store[1] + [x]
                return True

        def Print_DepthFirst(self):
                print self.indent + str(self.store[0])
                for i in range (0, len(self.store[1])):
                        self.store[1][i].indent = self.indent + "   "
                        self.store[1][i].Print_DepthFirst()
                self.indent = ""
                return True
        
        def Get_LevelOrder(self):
                levelList = [self]
                i = 0
                while i < len(levelList):
                        levelList = levelList[i].Traverse_LevelOrder(levelList)
                        i = i + 1
                for i in range (0, len(levelList)):
                        levelList[i] = levelList[i].store[0]
                return levelList

        def Traverse_LevelOrder(self,levelList):
                #note this function only processes the branches of the node, not the node itself. that's why the root note is printed in Get_LevelOrder
                for i in (self.store[1]):
                        levelList = levelList + [i]
                return levelList
            
        

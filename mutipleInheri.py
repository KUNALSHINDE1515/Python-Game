                #    Multiple Inheritance Python

class Kunal:
    Back="Oracle DB & JAva"
    def Backend(self):
        print("BAckend Task implemented using:",self.Back)
class Omkar:
    Front="HTML CSS & JAVASCRIPT"
    def Frontend(self):
        print("Fronted Task implemented using:",self.Front)
class TeamLead(Kunal,Omkar):
    def Show(self):
        print("Dynamic Website created .........")


T=TeamLead()
T.Backend()
T.Frontend()
T.Show()

class Home:
    def room(self):
        width = 100
        breadth = 100
        print(f"Area of room (cm),{width * breadth}")

    def kitchen(self):
        width = 1222
        breadth = 4888
        print(f"Area of kitchen (cm),{width * breadth}")

class firstHome(Home):
    def study(self):
        width = 2500
        breadth = 4000
        print(f"Area of study room (cm),{width * breadth}")

class secondHome(Home):
    def work_area(self):
        width = 2500
        breadth = 4000
        print(f"Area of work area (cm),{width * breadth}")


first = firstHome()
second = secondHome()
first.study()
second.work_area()
second.kitchen()
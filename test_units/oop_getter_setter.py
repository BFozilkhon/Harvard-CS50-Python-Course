class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @property
    def house(self):
        return self._house
    
    @house.setter
    def house(self, house):
        if house not in ['Gryffindor', 'Hufflepuff', 'RavenClaw','Slytherin' ]:
            raise ValueError('Invalid house!')
        self._house = house
          
 
def main():
    student = get_student()
    student.house = 'Fozili uyi'
    print(student)

def get_student():
    name = input('Name: ')
    house = input('House: ')
    student = Student(name, house)
    return student


if __name__ == '__main__':
    main()        
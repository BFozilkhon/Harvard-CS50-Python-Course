class Student:
    def __init__(self, name, house, patronous):
        if not name: 
            raise ValueError('Missing Name!!')
        if house not in ['Gryffindor', 'Hufflepuff', 'RavenClaw','Slytherin' ]:
            raise ValueError('Invalid house name') 
        self.name = name
        self.house = house
        self.patronous = patronous
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronous:
            case 'Stag':
                return '🐴'
            case 'Otter':
                return '😂'
            case _:
                return 'Default Value'

def main():
    student = get_student()
    print('Expecto Patronum!')
    print(student.charm())

def get_student():
    name = input('Name: ')
    house = input('House: ')
    partonous = input('Partonous ')
    student = Student(name, house, partonous)
    return student

if __name__ == '__main__':
    main()

# class Vehicle:
#     def __init__(self, reg_num, type_, owner):
#         self.registration_number = reg_num
#         self.type = type_
#         self.owner = owner

#     def update_owner(self):
#         updated_owner=input("Enter the name of the new owner: ")
#         self.owner=updated_owner
#         print(f"Your new owner is {self.owner}")

        
# mustang=Vehicle(1,"ford","Anthony")
# print(mustang.owner)
# mustang.update_owner()

class Event:
    def __init__(self,name,date,added_people):
        self.name = name
        self.date = date
        self.new_participants=added_people
        
    def add_participant(self):
        updated_participant=input("How many participants would you like to add: ")
        self.new_participants=updated_participant
        print(f"Your new participant is {updated_participant}")
  


Members=Event("Larry","December","new_participant")
Members.add_participant()


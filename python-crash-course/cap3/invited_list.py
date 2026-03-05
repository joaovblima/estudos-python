invited_list = ['jon snow', 'daemon targaryen', 'tyrion lannister']
    
message = " you have been invited to dinner"

print(invited_list[0].title() + "" + message)
print(invited_list[1].title() + "" + message)
print(invited_list[2].title() + "" + message)
drop_out_invited = invited_list.pop(1)
print("======================================================")
print(drop_out_invited.title()+ " " + "drop out for dinner")
new_invited = "daenerys targaryen"

invited_list.insert(1, new_invited)
print(invited_list[1].title() + "" + message)
invited_list.append('lord varys')
print(invited_list[-1].title() + "" + message)
invited_list.insert(0, 'arya stark')
print(invited_list[0].title() + "" + message)
invited_list.insert(2, 'Robby Stark')
print(invited_list[2].title() + "" + message)
invited_list.append('cersei lannister')
print(invited_list[-1].title() + "" + message)
print("======================================================")
print("disinvited peoples: ")
print("======================================================")
unfollow_message = "unfortunaly you were disinvited"
person_desinvited = invited_list.pop()
print(person_desinvited.title() + " " + unfollow_message)
person_desinvited = invited_list.pop()
print(person_desinvited.title() + " " + unfollow_message)
person_desinvited = invited_list.pop()
print(person_desinvited.title() + " " + unfollow_message)
print("Invited list: ")
print(invited_list)
person_desinvited = invited_list.pop()
print(person_desinvited.title() + " " + unfollow_message)
person_desinvited = invited_list.pop()
print(person_desinvited.title() + " " + unfollow_message)
del invited_list[-1]
del invited_list[0]
print(invited_list)

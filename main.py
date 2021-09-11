import numpy as np
import cv2
import matplotlib.pyplot as plt

Total = int(input("Please enter the total expense: "))
people_money = {'A':0,'Su':0,'Sa':0,'B':0,'Sh':0,'D':0,'K':0, 'U':0, 'J':0}

exclude_person= input("Are there people to exclude from the list? (y/n): ")

exclude_name2 = 'y'
while exclude_name2 == 'y' or exclude_name2 == 'Y':
    if exclude_person == 'y' or exclude_person == 'Y':
        exclude_name = input('Enter the name of person: ')
        del people_money[exclude_name]
        exclude_name2 = input('Are there more people to exclude from the list? (y/n): ')
    else:
        pass

people = list(people_money.keys())
money = list(people_money.values())

no_donor = int(input('Enter the number of donor: '))
donor_name = []
donor_money = []
for i in range(no_donor):
    donor_name_ask= input('Enter the name of donor: ')
    donor_name.append(donor_name_ask)
    donor_money_ask= int(input('Enter the amount given: '))
    donor_money.append(donor_money_ask)
    people_money[donor_name_ask]= donor_money_ask

ask_changes= input('Did anyone keep the changes? (y/n): ')
if ask_changes == 'y' or ask_changes == 'Y':
    ask_changes_name = input('Who keeps the changes?: ')
    changes_amount = sum(donor_money) - Total
    people_money[ask_changes_name] = abs(donor_money[donor_name.index(ask_changes_name)]-changes_amount)
else:
    pass


expense_per_head = Total/len(people_money)
print('Total expenses per person: ',expense_per_head)

confirm_expense_per_head = input('Do you want to proceed with this expenses per head? (y/n): ')
if confirm_expense_per_head == 'y' or confirm_expense_per_head == 'Y':
    pass
else:
    expense_per_head = int(input('Enter the approx. expenses per head: '))
    print('Approx. expenses per person: ', expense_per_head)


people = list(people_money.keys())
money = list(people_money.values())


final_giver_name= []
final_giver_amount= []
final_receiver_name= []
final_receiver_amount= []
final_neutral_name= []
for j in range(len(people_money)):
    if money[j] < expense_per_head:
        final_giver_name.append(people[j])
        final_giver_amount.append(abs(money[j]-expense_per_head))
    elif money[j] == expense_per_head:
        final_neutral_name.append(people[j])
    else:
        final_receiver_name.append(people[j])
        final_receiver_amount.append(abs(money[j] - expense_per_head))

Final_text= []
while not(final_receiver_name == [] or final_giver_name == []):
    n = final_receiver_amount[0] // expense_per_head
    for l in range(n + 1):
        if final_giver_amount == []:
            pass
        else:
            if final_receiver_amount[0] < final_giver_amount[0]:
                Final_text.append(final_receiver_name[0] + ' receives ' + str(final_receiver_amount[0]) + ' from ' + final_giver_name[0])
                print(final_receiver_name[0] + ' receives ' + str(final_receiver_amount[0]) + ' from ' + final_giver_name[0])
                final_receiver_name.pop(0)
                final_giver_amount[0] = final_giver_amount[0] - final_receiver_amount[0]
                final_receiver_amount.pop(0)
            else:
                Final_text.append(final_receiver_name[0] + ' receives ' + str(final_giver_amount[0]) + ' from ' + final_giver_name[0])
                print(final_receiver_name[0] + ' receives ' + str(final_giver_amount[0]) + ' from ' + final_giver_name[0])
                final_receiver_amount[0] = final_receiver_amount[0] - final_giver_amount[0]
                final_giver_name.pop(0)
                final_giver_amount.pop(0)

print(np.array(Final_text))





# create figure
fig = plt.figure(figsize=(10, 20))

plt.ylim([0,5])
# setting values to rows and column variables
rows = 4
columns = 3

# reading images
Image1 = cv2.imread('Image1_B.jpg')
Image2 = cv2.imread('Image2_Sa.jpg')
Image3 = cv2.imread('Image3_Sh.jpg')
Image4 = cv2.imread('Image4_Su.jpg')
Image5 = cv2.imread('Image5_D.jpg')
Image6 = cv2.imread('Image6_K.jpg')
Image7 = cv2.imread('Image7_A.jpg')
Image8 = cv2.imread('Image8_U.jpg')
Image9 = cv2.imread('Image9_J.jpg')

for r in range(len(Final_text)):
    plt.text(0.1, 4.9-(r/6), Final_text[r], fontsize=12)


plt.title("Expenses Calculation",
          fontsize='20',
          backgroundcolor='green',
          color='white',loc='right')
# Adds a subplot at the 1st position
fig.add_subplot(rows, columns, 4)

# showing image
plt.imshow(Image1)
plt.axis('off')
plt.title("Bhupendra(B)")

# Adds a subplot at the 2nd position
fig.add_subplot(rows, columns, 5)

# showing image
plt.imshow(Image2)
plt.axis('off')
plt.title("Sarita(Sa)")

# Adds a subplot at the 3rd position
fig.add_subplot(rows, columns, 6)

# showing image
plt.imshow(Image3)
plt.axis('off')
plt.title("Shikheb(Sh)")

# Adds a subplot at the 4th position
fig.add_subplot(rows, columns, 7)

# showing image
plt.imshow(Image4)
plt.axis('off')
plt.title("Sulav(Su)")


fig.add_subplot(rows, columns, 8)

# showing image
plt.imshow(Image5)
plt.axis('off')
plt.title("Dibesh(D)")


fig.add_subplot(rows, columns, 9)

# showing image
plt.imshow(Image6)
plt.axis('off')
plt.title("Kritika(K)")


fig.add_subplot(rows, columns, 10)

# showing image
plt.imshow(Image7)
plt.axis('off')
plt.title("Aabhash(A)")


fig.add_subplot(rows, columns, 11)

# showing image
plt.imshow(Image8)
plt.axis('off')
plt.title("Urmila(U)")


fig.add_subplot(rows, columns, 12)

# showing image
plt.imshow(Image9)
plt.axis('off')
plt.title("Jitendra(J)")







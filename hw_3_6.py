## staer
id_user1: int = int(input("Enter your ID: "));
first_name1: str = str(input("Enter your first name: "));
last_name1: str = str(input("Enter your last name: "));
height1: float = float(input("Enter your height: "));
year_of_birth1: int = int(input("Enter your year of birth: "));
id_user2: int = int(input("Enter your ID: "));
first_name2: str = str(input("Enter your first name: "));
last_name2: str = str(input("Enter your last name: "));
height2: float = float(input("Enter your height: "));
year_of_birth2: int = int(input("Enter your year of birth: "));
id_user3: int = int(input("Enter your ID: "));
first_name3: str = str(input("Enter your first name: "));
last_name3: str = str(input("Enter your last name: "));
height3: float = float(input("Enter your height: "));
year_of_birth3: int = int(input("Enter your year of birth: "));
user1_details = f"#: {id_user1:<5} name: {last_name1[:10]:<10} {first_name1[:10]:<10} height: {height1:.2f} year-of-birth: {year_of_birth1:<4}"
user2_details = f"#id: {id_user2:<5} name: {last_name2[:10]:<10} {first_name2[:10]:<10} height: {height2:.2f} year-of-birth: {year_of_birth2:<4}"
user3_details = f"#id: {id_user3:<5} name: {last_name3[:10]:<10} {first_name3[:10]:<10} height: {height3:.2f} year-of-birth: {year_of_birth3:<4}"
print ("\nDetails of users in a formatted table:");
print (f"#id: {'ID':<5} name: {'Last Name':<10} {'First Name':<10} height: {'Height':<6} year-of-birth: {'Year':<4}");
print (user1_details);
print (user2_details);
print (user3_details);
## End
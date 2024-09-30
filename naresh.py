''''
MS Dhoni aged X years, is a Cancerian, born with very strong Mars in his birth chart. Notably, Mars is the ruling planet for sports. Write a program to get the age of Dhoni as an integer and display the same.
Input Format:
Input is an integer that corresponds to the age of Dhoni.
Output Format: 
Display the age.
Refer sample Input and Output for formatting specifications.
[All the text in bold corresponds to the Input]
Sample Input and Output:
Enter the age:
35
Age of Dhoni is 35
''''
Ans:
a=int(input())
print("Age of Dhoni is",a)
''''
2)After Dhoni made it to the pinnacle of Success as Indian Captain, Mr. Banerjee was once invited by the Media to recall his association with Dhoni. Mr. Banerjee quoted one important moment that complemented the traits of Dhoni. It was when he approached Dhoni and asked him if he would play cricket for the school team saying "Will you be a wicketkeeper?" and was taken aback by Dhoni's confident reply "I will if I get a chance". Write a program to display the answers of Dhoni that impressed his master.
Input and Output Format:
Refer Sample input and output for formatting specifications.
All text in bold corresponds to input and the rest corresponds to output.
Sample Input and Output:
Banerjee's Question:
Will you be a wicketkeeper?
Dhoni's Reply:
I will if i get a chance.
For Banerjee's question "Will you be a wicketkeeper?" Dhoni's confident reply was "I will if I get a chance."
''''
Ans:
p=input("Banerjee's Question:\n")
r=input("Dhoni's Reply:\n")
print("For Banerjee's Question \"{}\" Dhoni's Confident reply was \"{}\"".format(p,r))

'''''
3)It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
Sample Input and Output:
Team 1:
Team Name:
DAV Jawahar Vidhya Mandir
Score:
150
Overs played:
20
Team 2:
Team name:
Kendriya School
Score:
110
Overs played:
18
Match Details:
Team 1:
Name: DAV Jawahar Vidhya Mandir
Score: 150
Overs played: 20
Team 2:
Name:  Kendriya School
Score: 110
Overs played: 18

''''
OPERATORS
1)Assume Dhoni's current age is 6. After 3 years, Dhoni's mother Devki Devi would be 4 times Dhoni's age. What is Devki Devi's current age? Write a program to determine the same.
Input Format:
First line of input consists of one integer value as age of Dhoni.
Output Format:
Output should display an integer that specifies Devki Devi's current age.
Sample Input and Output1:
6
33
Sample Input and Output2:
3
21
Note: Bold highlighted is the output value.

''''
Ans:
cAge=int(input())
deviAge =((cAge+3)*4)-3
print(deviAge)
'''
2) Dhoni once wished to join a  reputed Cricket Coaching Camp to be held at a place "X" kms away from his house. He told about this to his father and got his consent to use his friend's bike for the Camp. The Camp was to be held on all days of the month. His friend's bike provides a mileage of Y km/litre and the cost of petrol was Rs. Z. Dhoni's father now wanted to know the total amount that was needed by Dhoni to spend on his travel to the Camp. Help him find the same and assume number of days in a month as 30 days.
Input Format:
First line of the input is an integer "X" in kms that specifies the distance of the Camp from Dhoni's house.
Second line is an integer "Y" in km/litre that specifies the mileage of his friend's bike.
Third line is a float "Z" that specifies the cost of petrol in rupees.
Output Format:
Output should display a float that gives the total amount that is needed by Dhoni to spend on his travel in rupees. The float value is displayed correct to 2 decimal places.
Sample Input and Output 1:
75
55
63
2577.27
Sample Input and Output 2:
35
78
65.0
875.00
Note: Bold highlighted is the output
x=float(input())
y=float(input())
z=float(input())
a=(x*z*30)/y
print("%.2f"%a)
''''

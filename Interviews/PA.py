# CODE Link: https://app.codility.com/test/CL-FMZUPH-K6S/

Question:
The task here is to query an API for organizational data and print out a org chart. The resulting output should be user with any direct reports listed under them indented by 2 spaces.



Output:

Rick Sanchez
  Beth Smith
    Summer Smith
    Morty Smith
      Snowball
  Jerry Smith


Map: 
{
   " Beth" : [Summer, Morty],
    "Morty": [Snowball]
    "Snowball": []
}

TIME COMPLEXITY SPACE COMPLEXITY: O(K) : k 




Processing 1 entry: "Rick"




APPROACH 1:
============
http.get(API)

Structure data....

Map {"USERNAME" : [report1, report2, ....]}
report1 : "USERNAME"

print it out
for key, lreportees in map.items():
	if len(lreportees):
		add spaces

SPACES = LevelOfList * 2


{"Jigar Shah" : [] }
 
[user1, [user2, user3]]
listOfReportees = map["Rick Sanchez"]
walk through listOfReportees:
   STR or  LIST

   isInstance() -- ENTRY (string) or LIST


  O(1)
  STACK :  
  
  [ user, report1 report2, PROCESSING HERE]


  Recursion(user, tab)
    http call to get direct reports
    ofr report
      Recursion(report, tab+2)

	LEVEL 1 : RICK
		LEVEL 2: (2*Level)
			LEVEL 3: 

   1st level list: 2 * " "
	2nd level list: 2 * 1st levellistSpaces


API -> 

https response sample 
{
    "username": "rsanchez",
    "firstName": "Rick",
    "lastName": "Sanchez",
    "directReports": [
        "jsmith",
        "bsmith"
    ]
}


{
    "username": "bsmith",
    "firstName": "Beth",
    "lastName": "Smith",
    "directReports": [
        "ssmith",
        "msmith"
    ]
}
 
{
    "username": "jsmith",
    "firstName": "Jerry",
    "lastName": "Smith",
    "directReports": []
}  


Rick Sanchez
  Beth Smith <- direct report to Rick
    Summer Smith <- direct report to Beth
    Morty Smith <- direct report to Beth
  Jerry Smith <- direct report to Rick
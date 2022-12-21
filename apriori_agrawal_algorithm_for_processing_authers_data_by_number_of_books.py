import pickle


File = open('T_hashR_07_Concepts_Only.dat', 'rb')

data = pickle.load(File)

#data = { "A":["X","Y","Z"], "B":["X","S","S"] }

seperate_data = []

authers = []
for key, value in data.items():
  for auther in value:
    if auther not in authers:
      authers.append(auther)



auther_Thierbooks = dict()
for auther in authers:
  books = []

  for key,value in data.items():
    if auther in value:
      books.append(key)

  auther_Thierbooks[auther]= books


minimum_number_of_books = 115

auther_superier_then_percentege = dict()
for key, value in auther_Thierbooks.items():
  if len(value)>=minimum_number_of_books:
    auther_superier_then_percentege[key] = value

auther_superier_then_percentege_list = []
for key,value in auther_superier_then_percentege.items():
  auther_superier_then_percentege_list.append(key)



two_auther_superier_then_percentege = dict()
for item in range(len(auther_superier_then_percentege_list)):
    
    for i in range(item+1,len(auther_superier_then_percentege_list)):
      books = []
      for j in auther_superier_then_percentege[auther_superier_then_percentege_list[i]]:
        if j in auther_superier_then_percentege[auther_superier_then_percentege_list[item]]:
          books.append(j)

      if len(books) >= minimum_number_of_books:
         tuple_str = tuple([auther_superier_then_percentege_list[item],auther_superier_then_percentege_list[i]])
         two_auther_superier_then_percentege[tuple_str] = len(books)
      

print("10 sets of authors among the most frequent sets by specifing the number of shared books")    
for key,value in two_auther_superier_then_percentege.items():
  print(f'{key} === {value}')

print("\n\n")

print("the rules of association with the highest degrees of confidence::")
for key, value in two_auther_superier_then_percentege.items():
    print(key[0],"----->",key[1])
    print(key[1],"----->",key[0])

x = ("a","b")
x[1]

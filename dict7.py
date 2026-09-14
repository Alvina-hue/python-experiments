students={"Aju":96,"kuttu":75,"manu":85}
print("Dictionary:",students)
sorted_students=dict(sorted(students.items(),key=lambda x:x[1]))
print("Sorted Dictionary:",sorted_students)
dict1={"a":10,"b":20}
dict2={"c":30,"d":40}
merged={**dict1,**dict2}
print("Merged Dictionary:",merged)
text=input("Enter text:")
words=text.split()
frequency={}
for word in words:
    frequency[word]=frequency.get(word,0)+1
print("Word Frequency:",frequency)


set1={1,2,3,4,5}
set2={4,5,6,7,8}
common=set1 & set2
print("Common Elements:",common)
unique_set1=set1-set2
print("Unique Elements in Set1:",unique_set1)
unique_both=set1^set2
print("Unique Elements in Both Sets:",unique_both)
all_elements=set1 | set2
print("All Elements:",all_elements)


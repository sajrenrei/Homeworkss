my_dictionary = {"key": "Ключ", "mother": "мама", "key1":1, "key2":2, "father": "тато", "brother": "брат", 45: "World"}

word = my_dictionary.pop("key2")           #видаляє і вставляє ключ що ми вказали

print(my_dictionary)
print(word)

my_dictionary.update({"key3":3, "key4":4}) #додає нові ключі в словник
print(my_dictionary)

if "key4" in my_dictionary:           #Шукає в словнику потрібний ключ якщо ми не впечнені що він є
    print(my_dictionary["key4"])

if "World" in my_dictionary.values(): #Шукає значення і видає Yes якщо воно є
    print("Yes")
else:
    print("No")

print(my_dictionary.get("key5"))      #Видає None якщо такого ключа немає в словнику
print(my_dictionary.get("key"))       #Видає значення ключа якщо він є в словнику
#ЗАУВАЖЕННЯ!!! Якщо, в ключі записане значення None, то може виникнути непорозуміння:

dictionary_1 = {"key6":None}
print(dictionary_1.get("key6"))

#Щоб такого не відбулось, ми пишемо що завгодно після ключа, і тоді, якщо такого ключа не існує
#Ми отримаєио значення яке ми вказали:

print(dictionary_1.get("key6", "Not found"))
print(dictionary_1.get("key7", "Not found"))

print("-" * 20)
for item in my_dictionary:
    print(item)

print("-" * 20)
for item in my_dictionary.values():
    print(item)

print("-" * 20)
for item in my_dictionary.items():
    print(item)

print("-" * 20)
for item in my_dictionary.items():
    print(f"Ключ: {item[0]}, Значення: {item[1]}")

print("-" * 20)
for key, value in my_dictionary.items():
    print(f"Ключ: {key}, Значення: {value}")


mashing = open('C:\\Users\\arthu\\Desktop\\MDS\\2022-2-Squad03\\data\\raw\\mashing.txt', 'a')
naturals = open('C:\\Users\\arthu\\Desktop\\MDS\\2022-2-Squad03\\data\\raw\\large-2014.txt', 'a')

add_text = input("Write what you want to add: ")
choice = input("mashing or naturals? (M/N) ")

if choice == "M":
    text = add_text.replace(' ', '\n')
    mashing.write('\n' + text)
elif choice == "N":
    naturals.write('\n' + add_text)


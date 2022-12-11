# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# 12A11B10C6D5E4FG python is s7o c7ol
print("Если хотите кодировать первый файл и записать его в второй, введите 1")
print("Если хотите декодировать второй файл и записать его в первый, введите 2")

mode = input("Выбранный режим: ")

if mode=="1":
    file_decoded = open("for5-1.txt",'r',encoding='UTF-8')
    file_coded = open("for5-2.txt",'w',encoding='UTF-8')
    coded_result = ''
    for line in file_decoded:
        digit=0
        while digit<len(line):
            qty_same=1
            if ((digit)<len(line)-1) and (line[digit+1]==line[digit]):
                while (digit<len(line)-1) and (line[digit+1]==line[digit]):
                    qty_same+=1
                    digit+=1
                coded_result+=str(qty_same)
                coded_result+=str(line[digit])
                # digit+=qty_same-1
                digit+=1
            else:
                coded_result+=str(line[digit])
                qty_same=1
                digit+=1
    file_decoded.close
    file_coded.writelines(str(coded_result))

if mode == '2':
    file_decoded = open("for5-1.txt",'w',encoding='UTF-8')
    file_coded = open("for5-2.txt",'r',encoding='UTF-8')
    decoded_result = ''
    for line in file_coded:
        digit=0       
        while digit<len(line):
            qty_letters_str=''
            if line[digit].isdigit()==True:
                qty_letters_str=line[digit]
                while line[digit+1].isdigit()==True:
                    qty_letters_str+=line[digit+1]
                    digit+=1
                print(qty_letters_str)
                while int(qty_letters_str)>1:
                    decoded_result+=line[digit+1]
                    qty_letters_str=int(qty_letters_str)-1
            else:
                decoded_result+=line[digit]
            digit+=1
    file_coded.close
    file_decoded.writelines(str(decoded_result))

                

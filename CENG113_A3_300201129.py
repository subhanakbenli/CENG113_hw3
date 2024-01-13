## Sübhan Akbenli 300201129 ##
import os 

def create_database_file():
    if not os.path.exists("database"):
        open("database","w")
  
def update_database_file(file_name,identifiers,id_number=0):
    with open("database","r") as f:
        lines=f.readlines()
    with open("database","w") as f:
        exists=False
        for line in lines:
            if line.split(",")[0]==file_name:
                exists=True
                f.write(file_name+",")
                f.write((",".join(identifiers)).strip("\n"))
                f.write(","+str(id_number))
                f.write("\n")
            else:
                f.write(line)            
        if not exists:
                f.write(file_name+",")
                f.write((",".join(identifiers)).strip("\n"))
                f.write(","+str(id_number))
                f.write("\n")

def check_database_file(file_name):
    with open("database","r") as f:
        lines=f.readlines()
    for line in lines:
        if line.split(",")[0]==file_name:
            return True
    return False

def create_file(file_name,identifiers):

    if "id" in identifiers:
        print("You cannot create a file with attribute 'id'.")
        return None
    with open(file_name,"w") as f:
        f.write("id,")
        f.write(",".join(identifiers))
        f.write("\n")
        
    if  check_database_file(file_name):
        print("There was already such a file. It is removed and then created again.")
    else:        
        print("Corresponding file was successfully created.")
        
    update_database_file(file_name,identifiers)

def remove_file(file_name):
    
    with open("database","r") as f:     lines=f.readlines()
    if check_database_file(file_name):
        try:        os.remove(file_name)
        except:     pass
        print("Corresponding file was successfully deleted.")
    else:       print("There is no such file.")
    with open("database","w") as f:
        for line in lines:
            if line.split(",")[0]!=file_name:
                f.write(line)

def add_line(file_name,values):
        check_database_file(file_name)
        if not check_database_file(file_name):
            print("There is no such file.")
            return None
        with open(file_name,"r+") as f:
            lines=f.readlines()
            identifiers=lines[0].split(",")[1:]
            number_of_identifiers=len(identifiers)
            if len(values)!=number_of_identifiers:
                print("Numbers of attributes do not match.")
                return None
            
            with open("database","r") as database:        liste=database.readlines()
            id_number=0
            for line in liste:
                if line.split(",")[0]==file_name:
                    id_number=int(line.split(",")[-1])+1
            
            f.write(str(id_number)+","+",".join(values))
            f.write("\n")
            print(f"New line was successfully added to {file_name.strip('.txt')} with  id= {id_number}.")
            
            update_database_file(file_name,identifiers,id_number)

def display_files():
    with open("database","r") as f:
        lines=f.readlines()
    print("Number of files: ",len(lines))
    for counter,line in enumerate(lines,start=1):
        liste=line.split(",")[:-1]
        print(f"{counter}) {liste[0]}: {','.join(liste[1:])}")

def remove_lines(file_name,filters,equal=True):
    check_database_file(file_name)
    if not check_database_file(file_name):
        print("There is no such file.")
        return None
    with open(file_name,"r") as f:
        lines=f.readlines()
    headers=(lines[0].strip("\n").split(","))
    lines=lines[1:] if len(lines)>1 else []
    number_of_lines=len(lines)
    
    for keys in filters.keys():
        if keys not in headers:
            print("Your query contains an unknown attribute.")
            return None
        else:
            index=headers.index(keys)
            if equal: # burada mantık ters çünkü silme yapıyoruz
                lines=[line for line in lines if line.split(",")[index]!=filters[keys]]
            else:
                lines=[line for line in lines if line.split(",")[index]==filters[keys]]
    lines.insert(0,",".join(headers))
    with open(file_name,"w") as f:
        for line in lines:
            f.write(line)
    last_number_of_lines=len(lines)-1
    print(f"{number_of_lines-last_number_of_lines} lines were successfully removed.")

def modify_lines(file_name,filters,attribute,value,equal=True):
    if not check_database_file(file_name):
        print("There is no such file.")
        return None
    lines2=[]
    with open(file_name,"r") as f:
        lines=f.readlines()
    number_of_modify=0
    headers=(lines[0].strip("\n").split(","))
    if attribute not in headers:
        print("Your query contains an unknown attribute.")
        return None
    elif attribute == "id":
        print("Id values cannot be changed.")
        return None
    for keys in filters.keys():
        if keys not in headers:
            print("Your query contains an unknown attribute.")
            return None

        else:
            index=headers.index(keys)
            lines = lines[1:] if len(lines) > 1 else []
            for line in lines:
                control=line.split(",")
                if equal:
                    if control[index]==filters[keys]:
                        index2=headers.index(attribute)
                        control.pop(index2)
                        control.insert(index2,value)
                        lines2.append(",".join(control))
                        number_of_modify+=1
                        
                    else:           lines2.append(line)
                
                else:
                    if control[index]!=filters[keys]:
                        index2=headers.index(attribute)
                        control.pop(index2)
                        control.insert(index2,value)
                        lines2.append(",".join(control))
                        number_of_modify+=1
                        
                    else:           lines2.append(line)
    lines2.insert(0,",".join(headers))                
    with open(file_name,"w") as f:
        for line in lines2:
            f.write(line.strip("\n"))
            f.write("\n")
    print(f"{number_of_modify} lines were successfully modified.")

def fetch_lines(file_name,filters,equal=True):
        if not check_database_file(file_name):
            return "!!",None
        with open(file_name,"r") as f:
            lines=f.readlines()
        number_of_lines=len(lines)-1
        
        headers=(lines[0].strip("\n").split(","))
        lines=lines[1:] if len(lines)>1 else []
        for keys in filters.keys():
            if keys not in headers:
                return None,None
            else:
                index=headers.index(keys)
                if equal:
                    lines=[line for line in lines if line.split(",")[index]==filters[keys]]
                else:
                    lines=[line for line in lines if line.split(",")[index]!=filters[keys]]
        lines.insert(0,",".join(headers))
        return lines,number_of_lines


def display_lines(file_name,filters,columns,equal=True):
    lines,number_of_lines=fetch_lines(file_name,filters,equal)
    if lines==None:
        print("Your query contains an unknown attribute.")
        return None
    if lines=="!!":
        print("There is no such file.")
        return None
    headers=(lines[0].strip("\n").split(","))
    attributes=[line.strip("\n").split(",") for line in lines]
    aligns=[max([len(line[counter]) for line in attributes]) for counter in range(len(headers))]
    sagdan_sola=[]
    for col in columns:
        if col not in headers:
            print("Your query contains an unknown attribute.")
            return None
        else:
            index=headers.index(col)
            sagdan_sola.append(index)
    
    print(f"Number of lines in file {file_name.strip('.txt')}: {number_of_lines}")
    
    print(f"Number of lines that hold the condition: {len(lines)-1}")
    
    
    
    for indeks,line in enumerate(attributes):
        for i in sagdan_sola:
            print(line[i].ljust(aligns[i]),end=" | ")      
        print("\n"+"-"*(sum(aligns[c] for c in sagdan_sola)+3*len(columns)-1))    if indeks==0 or indeks==len(attributes)-1 else print()
    
    
def main():
    create_database_file()
    while True:
        query=input("\nWhat is your query?\n").strip()
        words=query.split(" ")
        command=words[0]
        if command=="create":
            "create file songs with title,album,artist,genre,year"
            if words[1]!="file" or words[3]!="with" or len(words)!=5:
                print("Invalid query.")
                continue
            identifiers=words[-1].split(",")
            create_file(words[2]+".txt",identifiers)
            
        elif command=="delete":
            "delete file CENG_Students"
            if words[1]!="file" or len(words)!=3:
                print("Invalid query.")
                continue
            remove_file(words[2]+".txt")
        
        elif command=="add":
            "add Cristiano_Ronaldo,Real_Madrid into Players"
            if words[2]!="into" or len(words)!=4:
                print("Invalid query.")
                continue
            add_line(words[-1]+".txt",words[1].split(","))
            
        elif command=="display":
            if words[1]!="files":
                print("Invalid query.")
                continue
            display_files()
        
        elif command=="remove":
            "remove lines from movies where id != -1"
            if words[1]!="lines" or words[2]!="from" or words[4]!="where" or \
                    (words[-2]=="!=" and words[-2]=="==") or len(words)!=8:
                print("Invalid query.")
                continue
            equal=True if words[-2]=="==" else False
            remove_lines(words[3]+".txt",
                        filters={words[-3]:words[-1]},equal=equal)
        
        elif command=="modify":
            "modify type in publications as conference_paper where type == conference"
            if words[2]!="in" or words[4]!="as" or words[6]!="where" or \
                    (words[-2]=="!=" and words[-2]=="==") or len(words)!=10:
                print("Invalid query.")
                continue
            modify_lines(words[3]+".txt",
                         filters={words[-3]:words[-1]},
                         attribute=words[1],
                         value=words[5],
                         equal=True if words[-2]=="==" else False)
            
        elif command=="fetch":
            "fetch id,salary from employees where department == software_development"
            
            if words[2]!="from" or words[4]!="where" or \
                    (words[-2]=="!=" and words[-2]=="==") or len(words)!=8:
                print("Invalid query.")
                continue
            display_lines(words[3]+".txt",
                          filters={words[-3]:words[-1]},
                          columns=words[1].split(","),
                          equal=True if words[-2]=="==" else False)
        
        elif command=="x":
            break
        
        else:
            print("Invalid query.")
            
            
main()
# create_database_file()
# remove_lines("test.txt",{"name": "JohAAAAAAAAAAAAAAAAAn"})

# display_lines("test.txt",{"name":"J"},False)

# modify_lines("test.txt",{"name":"John"},"Sübhan")
# create_file("test2.txt",["name","surname","age"])
# add_line("test.txt",["Nane","Doe","24"])
# add_line("test.txt",["Supie","Doe","23"])
# add_line("test.txt",["ssa","asdoke","9"])




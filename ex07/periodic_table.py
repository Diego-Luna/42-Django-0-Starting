import sys

class Table_element:
    def __init__(self, name, number, small, molar, electron):
        if "=" in name:
            self.name = name.split("=")[0].strip()
            self.position = name.split("=")[1].strip().split(':')[1].strip()

        self.number = number.split(':')[1].strip()
        self.small = small.split(':')[1].strip()
        self.molar = molar.split(':')[1].strip()
        self.electron = electron.split(':')[1].strip()
    
    def get_name(self):
        return self.name
    def get_position(self):
        return self.position
    def get_number(self):
        return self.number
    def get_small(self):
        return self.small
    def get_molar(self):
        return self.molar
    def get_electron(self):
        return self.electron

    def print_element(self):
        print("--------------------")
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Number: {self.number}")
        print(f"Small: {self.small}")
        print(f"Molar: {self.molar}")
        print(f"Electron: {self.electron}")
        print("--------------------")
        return 

    def create_html(self):
        return f''' 
            <td style="border: 1px solid black; padding:10px">
                <h4>{self.name}</h4>
                <ul>
                    <li>No {self.number}</li>
                    <li>{self.small}</li>
                    <li>{self.molar}</li>
                    <li>{self.electron} electron</li>
                </ul>
            </td>
        '''

def group_elements_by_position(elements):
    groups = [[] for _ in range(18)]
    for element in elements:
        try:
            pos = int(element.get_position())
        except ValueError:
            continue 
        if 0 <= pos < 18:
            groups[pos].append(element)
    return groups

def crete_table_elements_in_html(table): 

    # todo : filter the data form table for position, 0 to 17
    filtered_table = group_elements_by_position(table)

    # Todo : sort each group by number
    for group in filtered_table:
        group.sort(key=lambda x: int(x.get_number()))

    # Todo: create de html with <tr> for each row 
    html = ""
    
    value = 0
    for group in filtered_table:
        html += f"\t\t<tr class='column group-{value}'>\n"

        length = len(group)


        if 8 - length > 0 and length != 2:
            for _ in range(7 - length):
                html += '<td class="empty" style="border: 1px solid black; padding:10px"></td>\n'
        else:
            for _ in range(3):
                html += '<td class="empty" style="border: 1px solid black; padding:10px"></td>\n'

        for element in group:
            html += element.create_html()
        if length == 2:
            for _ in range(2):
                html += '<td class="empty" style="border: 1px solid black; padding:10px"></td>\n'
        html += "</tr>\n\n"
        value += 1


    # Todo: rerturn the html

    return html


def crete_html():
    try:
        # Todo: have a list of objects
        table = []

        # Todo : Rad de file and create a list of objects
        with open("periodic_table.txt") as file:
            data = file.readlines()
            for line in data:
                # table.append(line)
                data = line.strip().split(",")
                element = Table_element(*data)
                table.append(element)
        
        html = f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Periodic Table</title>
  <link rel="stylesheet" href="periodic_table.css">
</head>
<body>
  <h1>Periodic Table</h1>
  <h2>Dluna-lo</h2>
  <h3>Diego Luna 🤟</h3>
  <section>
    <div class="table-container">
      <table>
        <caption>The Beatles</caption>
        <tbody>
            <!-- 1 -->
{"".join(crete_table_elements_in_html(table))}
            <!-- 18 -->
        </tbody>
      </table>
    </div>
  </section>
</body>
</html>
        '''

        # Todo: Write the html to a file
        with open("periodic_table.html", "w") as file:
            file.write(html)
        

    except FileNotFoundError:
        print("File not found")
    except:
        print("An error occurred")


if __name__ == '__main__':
    crete_html()
import csv

# Open the input CSV file for reading
with open('raw_data.csv', 'r') as infile:
    with open('output.csv', 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        for row in reader:
            for i in range(len(row)):
                if row[i].startswith('"'):
                    row[i] = row[i][1:]
                if row[i].endswith('"'):
                    row[i] = row[i][:-1]
            writer.writerow(row)


# Function to read CSV file and return data as list of rows
def read_csv_file(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader]
        return rows

# Function to create HTML 4-up signage


def create_html_4_up_signage(rows):
    html = "<html>\n<head>\n<title>4-Up Signage</title>\n"
    html += '<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">\n'
    html += '<link rel="stylesheet" href="style.css">\n'
    html += '<link href="https://fonts.googleapis.com/css2?family=Permanent+Marker&display=swap" rel="stylesheet">'
    html += '<style>.card {width: 18rem; margin-bottom: 1rem;}</style>\n'
    html += "</head>\n<body>\n"
    html += '<div class="container-fluid main-box">\n'
    html += '<div class="row">\n'
    for i in range(0, len(rows), 4):
        for j in range(4):
            if i + j < len(rows):
                # Extract the title, price, and part number from each row
                title = rows[i + j][0]
                part_number = rows[i + j][1]
                regular = rows[i + j][2]
                sale = rows[i + j][3]
                cents = sale[-2:]
                sale = sale[1:]
                sale = sale[:-3]

                # Add the title, price, and part number to the HTML cell
                html += f'<div class="col-6 fourupbox">\n'
                html += f'<div class="card-title">Instore Special</div>\n'
                html += f'<div class="content">\n'
                html += f'<div class="title">{title}</div>\n'
                html += f'<div class=""><div class="part_number text-start">{part_number}</div>\n<div class="regular text-end">Reg. {regular}</div></div>\n'
                html += f'<div class="sale"><sup>$</sup>{sale}<sup>{cents}</sup></div>'
                html += "</div>\n"
                html += "</div>\n"
    html += "</div>\n"
    html += "</div>\n"
    html += '<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>\n'
    html += '<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>\n'
    html += '<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>\n'
    html += "</body>\n</html>"
    return html

# Main function to read CSV file and create HTML 4-up signage


def main(csv_file_path):
    rows = read_csv_file(csv_file_path)
    html = create_html_4_up_signage(rows)
    with open('4-up_signage.html', 'w') as file:
        file.write(html)
    print('4-up_signage.html file created successfully!')


if __name__ == '__main__':
    main('output.csv')

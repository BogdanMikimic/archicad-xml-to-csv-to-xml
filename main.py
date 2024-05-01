# import xmltodict
# import json
#
#
# def xml_to_dict(xml_file: str) -> dict:
#     # Open and read the XML file
#     with open(xml_file, 'r') as file:
#         xml_content = file.read()
#
#     # Convert XML to a Python dictionary
#     dict_data = xmltodict.parse(xml_content)
#
#     return dict_data
#
# the_dict = xml_to_dict('just building materials.xml')
#
# for k, v in the_dict.items():
#     for k1, v1 in v.items():
#         print(k1, v1, '\n\n')
# with open ('atribute.xml', 'r', encoding='utf-8') as my_xml:
#     count = 0
#     max_t = 0
#     for line in my_xml:
#         for char in line:
#             if char == '\t':
#                 count += 1
#         if count > max_t:
#             max_t = count
#         if count==2:
#             print(line)
#         count = 0
#     print(max_t)

def count_t(line: str) -> int:
    """
    Counts \t characters in a string

    :param line: string - a line of text
    :return:integer - count of \t found in the line
    """
    count = 0
    for char in line:
        if char == '\t':
            count += 1
    return count

def check_item_is_closing_tag(item):
    """
    Strips the line and check if it's a html closing tag - meaning it stars with </
    :param item: item is a string
    :return: returns True if item closing tag is
    """
    if item.strip().startswith('</'):
        return True
    else:
        return False

def compare_number_of_t_and_indicate_direction(old_count: int, new_count: int, line: str) -> str:
    if new_count > old_count:
        return 'child'
    elif new_count == old_count:
        if check_item_is_closing_tag(line):
            return 'closing tag'
        elif check_item_is_closing_tag(line) is False:
            return 'sibling'
    elif new_count < old_count:
        return 'parent'

def parse_document_two_lines(document):
    with open(document, 'r', encoding='utf-8') as doc:
        old_line = None
        for new_line in doc:
            if old_line is None:
                old_line = new_line.strip()
            else:
                t_old = count_t(old_line)
                t_new = count_t(new_line)
            old_line = new_line.strip()



parse_document_two_lines('test.xml')
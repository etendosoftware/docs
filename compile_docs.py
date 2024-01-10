# This file is a script to compile the entire mkdocs documentation into a single file.

import yaml


def mkdocs_nav_to_json(lines):
    # Find and extract the 'nav' section
    nav_content = []
    nav_section_found = False
    for line in lines:
        if line.strip().lower() == 'nav:':
            nav_section_found = True
        elif nav_section_found:  # Assuming indentation is important
            nav_content.append(line.rstrip())

    # Convert to YAML and then to a data structure
    nav_yaml = 'nav:\n' + '\n'.join(nav_content)
    nav_data = yaml.safe_load(nav_yaml)

    # Internal function to convert to JSON structure
    def convert_to_json_structure(nav_list):
        json_structure = []
        for item in nav_list:
            if isinstance(item, dict):
                for key, value in item.items():
                    if isinstance(value, list):
                        # Element with sub-elements
                        json_structure.append({key: convert_to_json_structure(value)})
                    else:
                        # Simple element
                        json_structure.append({key: value})
            elif isinstance(item, str):
                # Simple element
                key_value = item.split(':')
                if len(key_value) == 2:
                    json_structure.append({key_value[0].strip(): key_value[1].strip()})
                else:
                    json_structure.append({"title": item})
        return json_structure

    # Convert the 'nav' structure to JSON
    json_structure = convert_to_json_structure(nav_data['nav'])

    return json_structure


def run():
    # read the mkdocs.yml file
    with open("mkdocs.yml", "r") as f:
        lines = f.readlines()
        # advance to nav section
        json_hierarchy = mkdocs_nav_to_json(lines)
        # get the content of the files
        content = get_content(json_hierarchy)
        # Write the content to a file
        with open("compiled_docs.md", "w") as f:
            f.write(content)
            f.close()


def get_file_content(value, level):
    if value.endswith(".md"):
        with (open("docs/" + value, "r") as f):
            lines = f.readlines()

            content = ""
            start = False
            for line in lines:
                if line.startswith("#"):
                    start = True
                if start:
                    if line.startswith("#"):
                        content += "#" * level + line.lstrip()
                    else:
                        content += line

            ## add the source link, this links is for check the same info in the online
            # Wiki of etendo
            content += "\n"
            content += "Source: [https://docs.etendo.software/" + value + "](https://docs.etendo.software/" + value + ")"
            content += "\n"
    else:  # link to an url
        content = "Source: [" + value + "](" + value + ")"
        content += "\n"
    return content




def get_content(json_hier, level=1):
    content = ""
    for element in json_hier:
        for key, value in element.items():
            if isinstance(value, list):
                content += "#" * level + " " + key + "\n"
                content += get_content(value, level + 1)
            else:
                content += "#" * level + " " + key + "\n"
                content += get_file_content(value, level)
    return content


run()

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
        content = get_content(json_hierarchy, path='', title='', content='')
        # Write the content to a file
        with open("compiled_docsTEMP.md", "w") as f:
            f.write(content)
            f.close()
        # Clean the file, removing lines with only #, ##, ###, ####, #####, ######, #######, ######## and no text
        with open("compiled_docsTEMP.md", "r") as f2:
            lines = f2.readlines()
            with open("compiled_docs.md", "w") as f:
                for line in lines:
                    if line.strip() != "#" and line.strip() != "##" and line.strip() != "###" and line.strip() != "####" and line.strip() != "#####" and line.strip() != "######" and line.strip() != "#######" and line.strip() != "########":
                        f.write(line)
                f.close()
            f2.close()
        # Remove the temporary file
        import os
        os.remove("compiled_docsTEMP.md")


def get_file_content(value, level):
    content = ""
    if value.endswith(".md"):
        value_without_extension = value[:-3] if value.endswith('.md') else value
        content += "## Article URL: \n https://docs.etendo.software/" + value_without_extension + "\n"
        content += "## Article Content: \n"
        with (open("docs/" + value, "r") as f):
            lines = f.readlines()

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

    else:  # link to an url
        content = "Article URL: " + value + "\n"
        content += "\n"
    content += "==ARTICLE_END==\n"
    # Clean the relative links
    prefix_for_relative_links = "https://docs.etendo.software/"
    while content.find("](../../") != -1:  # first reduce the ../../ or bigger to ../
        content = content.replace("](../../", "](../")
    while content.find("](../") != -1:  # then reduce the ../ to /
        content = content.replace("](../", "](/")
    while content.find("](/") != -1:  # then add the prefix
        content = content.replace("](/", "](" + prefix_for_relative_links)

    return content


def get_content(json_hier, path, title='', content=''):
    content = ""
    for element in json_hier:
        for key, value in element.items():
            path_r = path + "/" + key
            if isinstance(value, list):
                content += get_content(value, path_r, title=key, content='')
            else:
                content += "==ARTICLE_START==\n"
                content += "# Article Title: " + key + "\n"
                content += "## Article Path: " + path_r + "\n"
                content += get_file_content(value, level=2)
    return content


run()

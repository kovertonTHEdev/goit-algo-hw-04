def get_cats_info(cats_file):
    try:
        with open(cats_file, "r", encoding="UTF-8") as file:
            cats_list = []
            for line in file:
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue
                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    continue
                cat_id = parts[0]
                name = parts[1]
                age_text = parts[2]
                try:
                    age = int(age_text)
                    cats_dict = {"id": cat_id, "name": name, "age": age}
                    cats_list.append(cats_dict)
                except ValueError:
                    continue
    except FileNotFoundError:
        return []
    return cats_list

def deduplicate(file_path, save_file_path):
    with open(file_path, "r") as f:
        data = f.readlines()

    cleaned_data = list(set(data))
    with open(save_file_path, "w") as f:
        for line in cleaned_data:
            f.write(f"{line}")


deduplicate('E:\yes-no-maybe-intent\data\\no.md',
            'E:\yes-no-maybe-intent\data\\no_clean.md')

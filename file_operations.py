import re
from tkinter import filedialog
from utils import update_status, open_folder_label_fn, create_folder


def browse_file(file_entry):
    filename = filedialog.askopenfilename(title="Select a File")
    if filename:
        file_entry.delete(0, "end")
        file_entry.insert(0, filename)


def search_strings(main, label, status_label, search_strings_value, file_entry):
    if len(search_strings_value.get()) == 0:
        update_status(
            status_label,
            f"Error: Enter valid search string(s) delimited with comma",
            "red",
        )
    else:
        # Clear the previous status before starting the new search
        update_status(status_label, "", "black")
        main.update_idletasks()  # Update the GUI immediately

        # # Remove any previous clickable link
        open_folder_label_fn(label, main, None, "")

        # Update the status label to show "Search in progress"
        status_label.config(text="Search in progress...", foreground="orange")
        main.update_idletasks()  # Update the GUI immediately

        try:
            file_path = file_entry.get()
            search_values = search_strings_value.get().split(
                ","
            )  # split values per comma
            search_values_strip = [
                item.strip() for item in search_values
            ]  # trim leading and trailing blanks from the string

            # Search for the strings in the exported dsx file
            search_dsx_file(file_path, search_values_strip)

            # Update status for success
            update_status(status_label, "Process finished successfully!", "green")

            open_folder_label_fn(
                label,
                main,
                file_path,
                "Click here to open the folder with output file(s)",
            )

        except Exception as e:
            # Update status for error
            update_status(status_label, f"Error: {str(e)}", "red")


def search_dsx_file(file_path, list_of_search_strings):
    with open(file_path, "r") as file:
        dsx_file = file.read()

    target_folder_path = create_folder(file_path)

    list_of_all_jobs = dsx_file.split("BEGIN DSJOB")

    for search_string in list_of_search_strings:
        jobs_found = []

        for jobs in list_of_all_jobs:
            # if search_string in jobs:
            if re.search(search_string, jobs, re.IGNORECASE):
                match = re.search(r'Identifier\s+"([^"]+)"', jobs)
                if match:
                    result = match.group(1)
                    jobs_found.append(result + "\n")

        # Write data into new file
        final_file = f"{target_folder_path}/{search_string}.txt"
        with open(final_file, "w") as file:
            file.writelines(jobs_found)

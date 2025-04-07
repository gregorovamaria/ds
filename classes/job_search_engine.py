import os, re


class JobSearchEngine:
    # Function to open the exported file
    def load_file(self, filepath):
        with open(filepath, "r") as file:
            return file.read()

    # Function to split keywords into list and trim leading/trailing 0
    def prepare_keywords(self, keywords):
        return [keyword.strip() for keyword in keywords.split(",")]

    # Function which search for jobs, in which keywords are used
    def search_keywords(self, input_file, keywords):
        jobs = input_file.split("BEGIN DSJOB")

        found_jobs = {kw.strip(): [] for kw in keywords}

        for keyword in keywords:
            for job in jobs:
                # if search_string in jobs:
                if re.search(keyword, job, re.IGNORECASE):
                    match = re.search(r'Identifier\s+"([^"]+)"', job)
                    if match:
                        result = match.group(1)
                        found_jobs[keyword].append(result)
        return found_jobs

    # Function to create target folder for search results
    def create_target_folder(self, filepath):
        folder = os.path.dirname(filepath)

        folder_path = f"{folder}/SearchResults"
        os.makedirs(folder_path, exist_ok=True)
        return folder_path

    # Function to write results into target txt files per keyword
    def write_results(self, target_folder, found_jobs):
        for keyword, matches in found_jobs.items():
            filename = f"{keyword.replace(' ', '_')}.txt"
            full_path = os.path.join(target_folder, filename)
            with open(full_path, "w", encoding="utf-8") as f:
                for match in matches:
                    f.write(match + "\n")

# INTELLIGENT CANDIDATE PRIORITIZATION & RETRIEVAL ENGINE

# JOB REQUIREMENT
print("JOB REQUIREMENT")
position = input("Position: ")
required_skills = input("Required Skills (comma separated): ")
required_skills = [skill.strip().lower() for skill in required_skills.split(",")]


# PERCEPTION - COLLECT CANDIDATES
candidates = []
num = int(input("\nNumber of candidates: "))
for i in range(num):
    candidate = {}
    candidate_id = f"C{i+1:03d}"
    print("\nEnter Candidate", candidate_id, "Details")
    name = input("Name: ")
    skills = input("Skills (comma separated): ")
    skills = [skill.strip().lower() for skill in skills.split(",")]
    experience = int(input("Experience (years): "))
    score = int(input("Test Score: "))
    priority = input("Priority (High/Medium/Low): ").strip().title()

    candidate = {
        "id": candidate_id,
        "name": name,
        "skills": skills,
        "experience": experience,
        "score": score,
        "priority": priority
    }
    candidates.append(candidate)


# ---------------------------------
# DISPLAY CANDIDATES
# ---------------------------------

print("\nCANDIDATES RECEIVED")
print("--------------------------------")

for candidate in candidates:

    print(candidate["id"], "->", candidate["name"])
    print("Skills:", ", ".join(candidate["skills"]))
    print("Experience:", candidate["experience"], "years")
    print("Score:", candidate["score"])
    print("Priority:", candidate["priority"])
    print()


# ---------------------------------
# SORT BY SCORE - BUBBLE SORT
# ---------------------------------

score_list = candidates.copy()

for i in range(len(score_list)):

    for j in range(len(score_list) - i - 1):

        if score_list[j]["score"] < score_list[j+1]["score"]:

            score_list[j], score_list[j+1] = score_list[j+1], score_list[j]


print("\nSORT BY SCORE")
print("--------------------------------")

for i, candidate in enumerate(score_list, 1):

    print(i, candidate["id"], "->", candidate["score"])


# ---------------------------------
# SORT BY PRIORITY
# ---------------------------------

priority_list = candidates.copy()

priority_order = {
    "High": 1,
    "Medium": 2,
    "Low": 3
}

for i in range(len(priority_list)):

    for j in range(len(priority_list) - i - 1):

        if priority_order[priority_list[j]["priority"]] > priority_order[priority_list[j+1]["priority"]]:

            priority_list[j], priority_list[j+1] = priority_list[j+1], priority_list[j]


print("\nSORT BY PRIORITY")
print("--------------------------------")

for i, candidate in enumerate(priority_list, 1):

    print(i, candidate["id"], "->", candidate["priority"])


# ---------------------------------
# LINEAR SEARCH
# ---------------------------------

print("\nLINEAR SEARCH")

search_name = input("Enter candidate name to search: ").strip().lower()

found = False

for candidate in candidates:

    if candidate["name"].lower() == search_name:

        print("Candidate Found:", candidate["id"])
        found = True
        break

if not found:

    print("Candidate Not Found")


# ---------------------------------
# DICTIONARY LOOKUP
# ---------------------------------

candidate_lookup = {}

for candidate in candidates:

    candidate_lookup[candidate["id"]] = candidate


print("\nDICTIONARY LOOKUP")

search_id = input("Search Candidate ID: ").strip().upper()

if search_id in candidate_lookup:

    print("Candidate", search_id, "found")

    print("Name:", candidate_lookup[search_id]["name"])

else:

    print("Candidate Not Found")


# ---------------------------------
# SIMILARITY SEARCH
# ---------------------------------

print("\nSIMILARITY SEARCH")

print("Required Skills:", required_skills)

match_results = []

for candidate in candidates:

    matched_skills = []

    for skill in required_skills:

        if skill in candidate["skills"]:

            matched_skills.append(skill)

    match_percentage = (len(matched_skills) / len(required_skills)) * 100

    if match_percentage == 100:
        match_level = "High Match"

    elif match_percentage >= 50:
        match_level = "Partial Match"

    else:
        match_level = "Low Match"

    match_results.append({
        "candidate": candidate,
        "percentage": match_percentage,
        "level": match_level
    })

    print(candidate["id"], "->", match_level)


# ---------------------------------
# AGENT DECISION
# ---------------------------------

print("\nAGENT DECISION")

best_candidate = None
highest_score = -1

for result in match_results:

    candidate = result["candidate"]

    if result["percentage"] == 100:

        if candidate["score"] > highest_score:

            highest_score = candidate["score"]
            best_candidate = candidate


if best_candidate:
    print("Recommended Candidate:", best_candidate["id"])
    print("Name:", best_candidate["name"])
    print("Reason: Strong skill match + Highest test score")
else:
    print("No candidate meets all required skills.")
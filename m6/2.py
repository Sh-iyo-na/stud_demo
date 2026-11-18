# Intelligent Candidate Prioritization & Retrieval Engine
def job_requirements():
    print("\nJob Requirements")
    position = input("Position: ")
    required_skills = list(map(str,input("Required Skills: ").lower().split(",")))
    return position, required_skills

def read_candidates():
    candidates = []
    num = int(input("\nNumber of candidates: "))
    for i in range(num):
        candidate_id = f"C{i+1:03d}"
        print("\nEnter Candidate", candidate_id, "Details")
        name = input("Name: ")
        skills = list(map(str,input("Skills: ").lower().split(",")))
        score = int(input("Test Score: "))
        priority = input("Priority (High/Medium/Low): ").title()
        candidate = {
            "id": candidate_id,
            "name": name,
            "skills": skills,
            "score": score,
            "priority": priority
        }
        candidates.append(candidate)
    return candidates

def display_candidates(candidates):
    print("\nCandidates Received")
    for candidate in candidates:
        print(candidate["id"], "->", candidate["name"])
        print("Skills:", ", ".join(candidate["skills"]))
        print("Score:", candidate["score"])
        print("Priority:", candidate["priority"])
        print()

def sort_by_score(candidates):
    score_list = candidates.copy()
    score_list.sort(key=lambda x: x["score"],reverse=True)
    print("\nSort by score:")
    i = 1
    for candidate in score_list:
        print(i, candidate["id"], "->", candidate["score"])
        i += 1

def sort_by_priority(candidates):
    priority = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }
    priority_list = candidates.copy()
    priority_list.sort(key=lambda x: (priority.get(x["priority"], 4),-x["score"]))
    print("\nSort by priority")
    i = 1
    for candidate in priority_list:
        print(i, candidate["id"], "->", candidate["priority"])
        i += 1
    
def dictionary_lookup(candidates):
    lookup = {}
    for candidate in candidates:
        lookup[candidate["id"]] = candidate
    print("\nDictionary Lookup")
    cid = input("Search Candidate ID: ").upper()
    if cid in lookup:
        print("Candidate", cid, "found")
    else:
        print("Candidate Not Found")

def similarity_search(candidates, required_skills):
    results = []
    print("\nSIMILARITY SEARCH")
    print("Required Skills:", required_skills)
    for candidate in candidates:
        matched = 0
        for skill in required_skills:
            if skill in candidate["skills"]:
                matched += 1
        percentage = (matched / len(required_skills) * 100
                      if required_skills else 0)
        if percentage == 100:
            level = "High Match"
        elif percentage >= 50:
            level = "Partial Match"
        else:
            level = "Low Match"
        results.append({
            "candidate": candidate,
            "matched_count": matched,
            "level": level
        })
    results.sort(key=lambda x:( x["matched_count"],x["candidate"]["score"]),reverse=True)
    print("\nBest Matches:")
    for result in results:
        print(result["candidate"]["id"], "->", result["level"])
    return results

def recommend_candidate(match_results):
    if not match_results:
        print("Agent Decision")
        print("No candidates available.")
        return
    priority_points = {
        "High": 3,
        "Medium": 2,
        "Low": 1
    }
    for result in match_results:
        candidate = result["candidate"]
        result["total"] = (candidate["score"] + priority_points[candidate["priority"]] * 10 + result["matched_count"] * 20)
    best = max(match_results, key=lambda result: result["total"])
    print("\nAgent Decision:")
    print("Recommended Candidate ->", best["candidate"]["id"])

print("Intelligent Candidate Prioritization & Retrieval Engine")
position, required_skills = job_requirements()
print("\nPosition:", position)
print("Required Skills:", ", ".join(required_skills))
candidates = read_candidates()
display_candidates(candidates)
sort_by_score(candidates)
sort_by_priority(candidates)
dictionary_lookup(candidates)
match_results = similarity_search(candidates, required_skills)
recommend_candidate(match_results)
# NEXORA-OPS
# Multiple Request Handling and State Management


# 1. PERCEPTION
def perception(request):
    print("\n[1] PERCEPTION")
    print("Request received successfully.")


# 2. REASONING
def reasoning(request):
    print("\n[2] REASONING")

    # Category Detection
    if any(word in request for word in ["laptop", "computer", "software", "network"]):
        category = "Technical Support"

    elif any(word in request for word in ["leave", "salary", "attendance"]):
        category = "HR Request"

    elif any(word in request for word in ["payment", "account", "refund", "complaint"]):
        category = "Customer Support"

    else:
        category = "General Inquiry"

    # Urgency Detection
    if any(word in request for word in ["urgent", "immediately", "one hour", "emergency"]):
        urgency = "High"

    elif category == "HR Request":
        urgency = "Low"

    else:
        urgency = "Medium"

    print("Detected Category:", category)
    print("Detected Urgency:", urgency)

    return category, urgency


# 3. DECISION
def decision(category, urgency):
    print("\n[3] DECISION")

    priority = urgency.upper()

    if category == "Technical Support":
        department = "IT Support"

    elif category == "HR Request":
        department = "Human Resources"

    elif category == "Customer Support":
        department = "Customer Service"

    else:
        department = "General Department"

    print("Priority Assigned:", priority)
    print("Department Selected:", department)

    return priority, department


# 4. ACTION
def action(category, priority):
    print("\n[4] ACTION")

    if priority == "HIGH":
        agent_action = "Create Support Request"
        status = "Processing"
        result = "Immediate Escalation"

    elif category == "HR Request":
        agent_action = "Create Leave Request"
        status = "Awaiting Approval"
        result = "Route to HR"

    elif category == "Customer Support":
        agent_action = "Create Complaint Ticket"
        status = "Assigned"
        result = "Create Service Ticket"

    else:
        agent_action = "Create General Request"
        status = "Processing"
        result = "Route to Department"

    print("Action:", agent_action)
    print("Status:", status)

    return agent_action, status, result


# 5. STATE MANAGEMENT
def update_state(request_data, status):
    request_data["status"] = status


# 6. PROCESS REQUEST
def process_request(request_id):
    print("\n" + "-" * 45)
    print("Processing Request:", request_id)

    request = input("Enter your request: ").lower()

    perception(request)

    category, urgency = reasoning(request)

    priority, department = decision(category, urgency)

    agent_action, status, result = action(category, priority)

    # Store request information
    request_data = {
        "id": request_id,
        "request": request,
        "category": category,
        "priority": priority,
        "department": department,
        "action": agent_action,
        "decision": result
    }

    update_state(request_data, status)

    return request_data


# 7. DISPLAY ALL REQUESTS
def display_requests(requests):
    print("\n" + "=" * 45)
    print("             ALL REQUESTS")
    print("=" * 45)

    for request in requests:
        print("\nRequest ID:", request["id"])
        print("Category:", request["category"])
        print("Priority:", request["priority"])
        print("Department:", request["department"])
        print("Action:", request["action"])
        print("Decision:", request["decision"])
        print("Status:", request["status"])

    print("\n" + "=" * 45)


# MAIN AGENT
def nexora_agent():

    print("=" * 45)
    print("       NEXORA-OPS AGENT SYSTEM")
    print("=" * 45)

    requests = []

    number = int(input("\nNumber of requests: "))

    for i in range(number):
        request_id = f"NX-{1001+i}"

        request_data = process_request(request_id)

        requests.append(request_data)

    display_requests(requests)


# RUN AGENT
nexora_agent()



# # NEXORA-OPS
# # Autonomous Business Request Intelligence Agent


# # 1. PERCEPTION
# def perception():
#     print("\n[1] PERCEPTION")

#     request = input("Enter your request: ").lower()

#     print("Request received successfully.")

#     return request


# # 2. REASONING
# def reasoning(request):
#     print("\n[2] REASONING")

#     # Category Detection
#     if any(word in request for word in ["laptop", "computer", "software", "network"]):
#         category = "Technical Support"

#     elif any(word in request for word in ["leave", "salary", "attendance"]):
#         category = "HR Request"

#     elif any(word in request for word in ["payment", "account", "refund", "complaint"]):
#         category = "Customer Support"

#     else:
#         category = "General Inquiry"

#     # Urgency Detection
#     if any(word in request for word in ["urgent", "immediately", "one hour", "emergency"]):
#         urgency = "High"

#     elif category == "HR Request":
#         urgency = "Low"

#     else:
#         urgency = "Medium"

#     print("Detected Category:", category)
#     print("Detected Urgency:", urgency)

#     return category, urgency


# # 3. DECISION
# def decision(category, urgency):
#     print("\n[3] DECISION")

#     # Priority Assignment
#     priority = urgency.upper()

#     # Department Selection
#     if category == "Technical Support":
#         department = "IT Support"

#     elif category == "HR Request":
#         department = "Human Resources"

#     elif category == "Customer Support":
#         department = "Customer Service"

#     else:
#         department = "General Department"

#     print("Priority Assigned:", priority)
#     print("Department Selected:", department)

#     return priority, department


# # 4. ACTION
# def action(category, priority):
#     print("\n[4] ACTION")

#     if priority == "HIGH":
#         agent_action = "Create Support Request"
#         status = "Processing"
#         decision_result = "Immediate Escalation"

#     elif category == "HR Request":
#         agent_action = "Create Leave Request"
#         status = "Awaiting Approval"
#         decision_result = "Route to HR"

#     elif category == "Customer Support":
#         agent_action = "Create Complaint Ticket"
#         status = "Assigned"
#         decision_result = "Create Service Ticket"

#     else:
#         agent_action = "Create General Request"
#         status = "Processing"
#         decision_result = "Route to Department"

#     print("Action:", agent_action)
#     print("Status:", status)

#     return agent_action, status, decision_result


# # MAIN AGENT
# def nexora_agent():

#     print("=" * 45)
#     print("       NEXORA-OPS AGENT SYSTEM")
#     print("=" * 45)

#     request = perception()

#     category, urgency = reasoning(request)

#     priority, department = decision(category, urgency)

#     agent_action, status, decision_result = action(category, priority)

#     print("\n" + "=" * 45)
#     print("             FINAL RESULT")
#     print("=" * 45)

#     print("Request ID     : NX-1001")
#     print("Category       :", category)
#     print("Priority       :", priority)
#     print("Department     :", department)
#     print("Agent Decision :", decision_result)
#     print("Action         :", agent_action)
#     print("Status         :", status)

#     print("=" * 45)


# # Run Agent
# nexora_agent()
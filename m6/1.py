class SchoolAdmissionAgent:
    def __init__(self):
        self.state = {
            "class": None,
            "percentage": None,
            "batch": None,
            "eligible": False,
            "seat_available": False,
            "fee_paid": False,
            "status": "Pending"
        }

    def perceive(self, student_class, percentage, batch):
        print("\nAgent: Receiving admission request")
        self.state["class"] = student_class
        self.state["percentage"] = percentage
        self.state["batch"] = batch
        print("Agent: Application details received")

    def reason(self):
        print("\nAgent: Checking application requirements")
        if self.state["percentage"] >= 75:
            print("Agent: Student is eligible")
            return True
        else:
            print("Agent: Student is not eligible")
            return False

    def display_details(self):
        print("\nADMISSION DETAILS")
        print("Class:", self.state["class"])
        print("Percentage:", self.state["percentage"], "%")
        print("Preferred Batch:", self.state["batch"])
        print("Eligibility:", self.state["eligible"])
        print("Seat Available:", self.state["seat_available"])
        print("Fee Paid:", self.state["fee_paid"])
        print("Final Admission Status:", self.state["status"])

    def eligibility_tool(self):
        print("\nTool: Checking eligibility")
        if self.state["percentage"] >= 75:
            return True
        else:
            return False

    def seat_check_tool(self):
        print("Tool: Checking seat availability")
        available_seats = {
            "morning": 5,
            "afternoon": 3
        }
        batch = self.state["batch"]
        if available_seats.get(batch, 0) > 0:
            return True
        else:
            return False

    def fee_check_tool(self):
        print("Tool: Checking admission fee")
        return True

    def decide(self):
        print("\nAgent: Making admission decision")
        self.state["eligible"] = self.eligibility_tool()
        if not self.state["eligible"]:
            self.state["status"] = "Rejected"
            return
        self.state["seat_available"] = self.seat_check_tool()
        if not self.state["seat_available"]:
            self.state["status"] = "Waiting"
            return
        self.state["fee_paid"] = self.fee_check_tool()
        if self.state["fee_paid"]:
            self.state["status"] = "Admitted"
        else:
            self.state["status"] = "Fee Pending"

    def feedback(self):
        print("\nAgent: Receiving tool feedback")
        print("Eligibility:", self.state["eligible"])
        print("Seat Available:", self.state["seat_available"])
        print("Fee Paid:", self.state["fee_paid"])

    def update_state(self):
        print("\nAgent: Updating application state")
        print("Application Status:", self.state["status"])

    def run(self, message):

        print("\nAgent: Understanding the message")
        words = message.split()

        if not any(word in ["admission", "admit", "apply"] for word in words):
            print("Agent: No admission request found.")
            return

        student_class = None
        for i in range(len(words)):
            if words[i] in ["class", "grade"]:
                student_class = int(words[i + 1])
                break

        percentage = None
        for word in words:
            if word.endswith("%"):
                percentage = int(word.replace("%", ""))
                break

        batch = None
        if "morning" in words:
            batch = "morning"
        elif "afternoon" in words:
            batch = "afternoon"

        if student_class is None or percentage is None or batch is None:
            print("Agent: Some application details are missing.")
            return

        self.perceive(student_class, percentage, batch)

        result = self.reason()

        if result:
            self.decide()
            self.feedback()
            self.update_state()
        else:
            self.state["status"] = "Rejected"
            self.update_state()

        print("\nADMISSION DETAILS ")
        print("Class:", self.state["class"])
        print("Percentage:", self.state["percentage"], "%")
        print("Batch:", self.state["batch"])
        print("Eligibility:", self.state["eligible"])
        print("Seat Available:", self.state["seat_available"])
        print("Fee Paid:", self.state["fee_paid"])
        print("Final Status:", self.state["status"])

agent = SchoolAdmissionAgent()

message = input("Enter the message: ").lower()

agent.run(message)